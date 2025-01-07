from manim import *
from manim import config

config.pixel_width = 3840
config.pixel_height = 2160
config.frame_rate = 30  # Set your desired FPS

class DynamicHomogeneityPrinciple(Scene):
    def construct(self):
        # Parameters
        func = lambda x: 2*x  # The function to plot
        scale_factor = 3       # Scale factor 'a'
        point = 4             # Point to evaluate
        colors = {
            "line": MAROON,
            "point_original": BLUE,
            "point_scaled": GREEN,
        }

        # Axes setup
        xlim = (0, 20)
        ylim = (0, 40)
        y_range = 4
        ax = Axes(
            x_range=[xlim[0], xlim[1]], y_range=[ylim[0], ylim[1], y_range], axis_config={"include_tip": False},
            x_axis_config={"numbers_to_include": list(range(xlim[0], xlim[1], 2))},
            y_axis_config={"numbers_to_include": list(range(ylim[0], ylim[1], y_range))},
        )
        labels = ax.get_axis_labels(x_label="x", y_label="f(x)")

        t = ValueTracker(0)
        graph = ax.plot(func, color=colors["line"], x_range=[xlim[0],16])

        # Initial dot
        initial_point = ax.coords_to_point(0, 0)
        dot = Dot(point=initial_point)

        # Add vertical and horizontal lines
        v_line = always_redraw(
            lambda: ax.get_vertical_line(ax.c2p(t.get_value(), func(t.get_value())))
        )
        h_line = always_redraw(
            lambda: ax.get_horizontal_line(ax.c2p(t.get_value(), func(t.get_value())))
        )

        dot.add_updater(lambda x: x.move_to(ax.c2p(t.get_value(), func(t.get_value()))))

        self.add(ax, labels, graph, dot, v_line, h_line)

        # Animate the original point
        self.play(t.animate.set_value(point))
        self.wait(1)

        # Create static copies of the lines and dot
        static_v_line = ax.get_vertical_line(ax.c2p(point, func(point)), color=colors["point_original"])
        static_h_line = ax.get_horizontal_line(ax.c2p(point, func(point)), color=colors["point_original"])
        static_dot = Dot(ax.c2p(point, func(point)), color=colors["point_original"])

        # Add labels for f(point)
        label_f_original = MathTex(f"f({point})", f"= {func(point)}", color=colors["point_original"])
        label_f_original.next_to(static_h_line, RIGHT)

        self.add(static_v_line, static_h_line, static_dot, label_f_original)
        self.play(
            Create(static_v_line),
            Create(static_h_line),
            Create(static_dot),
            Write(label_f_original)
        )
        self.wait(1)

        # Animate the scaled point
        scaled_point = scale_factor * point
        self.play(t.animate.set_value(scaled_point))
        self.wait(1)

        # Create static copies for the scaled point
        static_v_line_scaled = ax.get_vertical_line(ax.c2p(scaled_point, func(scaled_point)), color=colors["point_scaled"])
        static_h_line_scaled = ax.get_horizontal_line(ax.c2p(scaled_point, func(scaled_point)), color=colors["point_scaled"])
        static_dot_scaled = Dot(ax.c2p(scaled_point, func(scaled_point)), color=colors["point_scaled"])

        # Add labels for f(scaled_point)
        label_f_scaled = MathTex(f"f({scaled_point})", f"= {func(scaled_point)}", color=colors["point_scaled"])
        label_f_scaled.next_to(static_h_line_scaled, RIGHT)

        self.add(static_v_line_scaled, static_h_line_scaled, static_dot_scaled, label_f_scaled)
        self.play(
            Create(static_v_line_scaled),
            Create(static_h_line_scaled),
            Create(static_dot_scaled),
            Write(label_f_scaled)
        )
        self.wait(1)

        # Verify homogeneity: f(ax) vs. a * f(x)
        actual_result = func(scaled_point)
        expected_result = scale_factor * func(point)
        is_homogeneous = actual_result == expected_result

        # Final result labels
        left_side = MathTex(
            f"\\overbrace{{f({scale_factor} \\cdot {point})}}", f"^{{{actual_result}}}",
            color=RED if not is_homogeneous else colors["point_scaled"]
        ).next_to(static_h_line_scaled, UP)

        equals_sign = MathTex(
            "\\neq" if not is_homogeneous else "=",
            color=RED if not is_homogeneous else GOLD
        ).next_to(left_side, RIGHT)

        right_side = MathTex(
            f"\\overbrace{{{scale_factor} \\cdot f({point})}}", f"^{{{expected_result}}}",
            color=colors["point_original"]
        ).next_to(equals_sign, RIGHT)

        # Animate the final result
        self.play(Write(left_side))
        self.play(Write(equals_sign))
        self.play(Write(right_side))
        self.wait(2)
