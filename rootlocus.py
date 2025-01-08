from manim import *
import numpy as np
import control

class RootLocusScene(Scene):
    def construct(self):
        # Create axes with new limits
        axes = Axes(
            x_range=[-50, 0, 5],
            y_range=[-15, 15, 5],
            axis_config={"color": BLUE},
            x_length=8,
            y_length=6,
            tips=False
        ).add_coordinates()
        
        # Add labels
        x_label = axes.get_x_axis_label("Re(s)")
        y_label = axes.get_y_axis_label("Im(s)")
        labels = VGroup(x_label, y_label)
        
        # Define transfer function using control library
        num = [0.075, 1, 1]  # coefficients of s^2, s^1, s^0
        den = [1, 3, 5, 0]  # coefficients of s^3, s^2, s^1, s^0
        sys = control.TransferFunction(num, den)
        
        # Calculate root locus points with fewer points
        kvec = np.logspace(-1, 5, 100)  # 100 points from 0.1 to 1000, logarithmically spaced
        print("K values range:", kvec[0], "to", kvec[-1])
        
        # Calculate root locus using the older method for now
        rlist, klist = control.root_locus(sys, kvec=kvec, plot=False)
        rlist = np.array(rlist)  # Convert to numpy array for easier handling
        print("Number of K values:", len(kvec))
        print("Number of poles:", len(rlist[0]))
        print("Initial poles (K=0):", rlist[0])
        
        # Convert complex arrays to list of points for each branch
        branches = []
        for i in range(len(rlist[0])):  # For each pole
            branch = []
            for j in range(len(rlist)):  # For each k value
                branch.append(rlist[j][i])
            branches.append(branch)
        
        # Define branch colors
        BRANCH1_COLOR = BLUE
        BRANCH2_COLOR = GREEN
        BRANCH3_COLOR = "#FF0000"  # Pure red
        
        # Create branches with animation groups
        branch_animations = []
        points_per_step = 50  # Number of points to show in each animation step
        
        for branch_idx, branch in enumerate(branches):
            color = [BRANCH1_COLOR, BRANCH2_COLOR, BRANCH3_COLOR][branch_idx]
            branch_points = []
            
            # Split branch into animation steps
            for i in range(0, len(branch), points_per_step):
                step_points = branch[i:i + points_per_step]
                step_group = VGroup(*[
                    Cross(stroke_width=1)
                    .scale(0.05)
                    .set_color(color)
                    .move_to(axes.coords_to_point(point.real, point.imag))
                    for point in step_points
                ])
                branch_points.append(step_group)
            
            branch_animations.append(branch_points)
        
        # Create crosses for initial poles
        initial_poles = rlist[0]
        pole_crosses = VGroup(*[
            Cross(stroke_width=2)
            .scale(0.15)
            .set_color([BRANCH1_COLOR, BRANCH2_COLOR, BRANCH3_COLOR][i])
            .move_to(axes.coords_to_point(pole.real, pole.imag))
            for i, pole in enumerate(initial_poles)
        ])
        
        # Calculate zeros
        zeros = np.roots(num)
        
        # Create circles for zeros
        zero_circles = VGroup(*[
            Circle(radius=0.1, color=YELLOW, fill_opacity=0)
            .move_to(axes.coords_to_point(zero.real, zero.imag))
            for zero in zeros
        ])
        
        # Create transfer function and K value display
        def get_display_text(k):
            if isinstance(k, str):  # For infinity case
                num_text = "3s^2 + 40s + 40"
                den_text = "40s^3 + (120 + 3K)s^2 + (200 + 40K)s + 40K"
            else:
                # Calculate actual coefficients for current K
                s2_coeff = 120 + 3*k
                s1_coeff = 200 + 40*k
                s0_coeff = 40*k
                den_text = f"40s^3 + {s2_coeff:.0f}s^2 + {s1_coeff:.0f}s + {s0_coeff:.0f}"
                num_text = "3s^2 + 40s + 40"
            
            # Create separate MathTex objects for better alignment
            tf_top = MathTex(num_text).scale(0.7)
            tf_bottom = MathTex(den_text).scale(0.7)
            tf_equals = MathTex("T(s) = ").scale(0.7)
            tf_frac_line = Line(LEFT, RIGHT).match_width(VGroup(tf_top, tf_bottom).arrange(DOWN))
            
            # Group the fraction parts
            frac = VGroup(tf_top, tf_frac_line, tf_bottom)
            
            # Create complete transfer function
            tf = VGroup(tf_equals, frac).arrange(RIGHT)
            
            k_val = MathTex(f"K = {k}").scale(0.7)
            
            # Group them vertically with fixed spacing
            group = VGroup(tf, k_val).arrange(DOWN, buff=0.3, aligned_edge=LEFT)
            group.to_corner(UL, buff=0.5)
            return group
        
        display_text = get_display_text(0)
        
        # Animation sequence
        self.play(Create(axes), Create(labels))
        self.wait()
        
        # Show initial poles and zeros
        self.play(Create(pole_crosses), Create(zero_circles))
        self.wait()
        
        # Show initial transfer function and K value
        self.play(Write(display_text))
        
        # Use the actual K values from root locus calculation
        k_values = kvec[::10]  # Take every 10th value instead of every 100th
        print("K values for animation:", k_values)
        print("Number of animation steps:", len(k_values))
        
        for i, k in enumerate(k_values):
            if i > 0:
                old_display = display_text
                display_text = get_display_text(f"{k:.1f}")
                
                # Create animations for this step
                animations = [ReplacementTransform(old_display, display_text)]
                for branch_points in branch_animations:
                    if i < len(branch_points):
                        animations.append(Create(branch_points[i]))
                
                self.play(*animations, run_time=0.3)
        
        # Show final state (K → ∞)
        final_display = get_display_text("\\infty")
        self.play(ReplacementTransform(display_text, final_display))
        
        # Final pause
        self.wait(2)
