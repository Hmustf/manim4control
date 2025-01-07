from manim import *
from manim import config

config.pixel_width = 3840
config.pixel_height = 2160
config.frame_rate = 30  # Set your desired FPS


class DynamicSuperpositionPrinciple(Scene):
    def construct(self):
        # Parameters
        func = lambda x:  2*x  # The function to plot
        points = [2, 5]  # Points to evaluate
        colors = {
            "line": MAROON,
            "point_1": BLUE,
            "point_2": YELLOW,
            "result_point": GREEN
        }

        # Axes setup
        xlim = (0, 10)
        ylim = (0, 20)
        y_range = 2
        ax = Axes(
            x_range=[xlim[0], xlim[1]], y_range=[ylim[0], ylim[1], y_range], axis_config={"include_tip": False},
            x_axis_config={"numbers_to_include": list(range(xlim[0], xlim[1], 1))},
            y_axis_config={"numbers_to_include": list(range(ylim[0], ylim[1], y_range))},
        )
        labels = ax.get_axis_labels(x_label="x", y_label="f(x)")

        t = ValueTracker(0)
        graph = ax.plot(func, color=colors["line"], x_range=[xlim[0],9])

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
        self.play(Create(ax), Create(labels), Create(graph), Create(dot), Create(v_line), Create(h_line))

        for idx, point in enumerate(points):
            color = colors[f"point_{idx + 1}"]

            # Animate the point to the target value
            self.play(t.animate.set_value(point))
            self.wait(1)

            # Create static copies of the lines and dots
            static_v_line = ax.get_vertical_line(ax.c2p(point, func(point)), color=color)
            static_h_line = ax.get_horizontal_line(ax.c2p(point, func(point)), color=color)
            static_dot = Dot(ax.c2p(point, func(point)), color=color)

            # Add labels for f(point)
            label_f_part1 = MathTex(f"f({point})", color=color).next_to(static_h_line, RIGHT)
            label_f_part2 = MathTex(f"= {func(point)}",  # Changed back to simple equals
                               color=color).next_to(label_f_part1, RIGHT)

            self.add(static_v_line, static_h_line, static_dot, label_f_part1, label_f_part2)
            self.play(
                Create(static_v_line),
                Create(static_h_line),
                Create(static_dot),
                Write(label_f_part1),
                Write(label_f_part2)
            )
            self.wait(1)

            # Save labels and points for the final result
            if idx == 0:
                label_f1_part1, label_f1_part2 = label_f_part1, label_f_part2
            elif idx == 1:
                label_f2_part1, label_f2_part2 = label_f_part1, label_f_part2

        # Calculate the result point and its actual value
        result_point = sum(points)
        sum_of_individual_values = sum(func(p) for p in points)
        actual_result_value = func(result_point)  # This is f(x₁ + x₂)
        is_superposition = actual_result_value == sum_of_individual_values

        # First animate the dot to the result point
        self.play(t.animate.set_value(result_point))
        self.wait(1)

        # Then create and show the static elements
        static_v_line_result = ax.get_vertical_line(ax.c2p(result_point, func(result_point)), color=colors["result_point"])
        static_h_line_result = ax.get_horizontal_line(ax.c2p(result_point, func(result_point)), color=colors["result_point"])
        static_dot_result = Dot(ax.c2p(result_point, func(result_point)), color=colors["result_point"])

        # Create the final label in separate parts for animation
        left_side = MathTex(
            f"\\overbrace{{f({points[0]}+{points[1]})}}",
            f"^{{{actual_result_value}}} ",
            color=RED if not is_superposition else colors["result_point"]
        ).next_to(static_h_line_result, UP)

        equals_sign = MathTex(
            "\\neq" if not is_superposition else "=",
            color=RED if not is_superposition else colors["result_point"]
        ).next_to(left_side, RIGHT)

        right_side_f1 = MathTex(
            f"\\overbrace{{f({points[0]})}}",
            f"^{{{func(points[0])}}}",
            color=colors["point_1"]
        )

        plus_sign = MathTex(
            "+",
            color=RED if not is_superposition else colors["result_point"]
        )

        right_side_f2 = MathTex(
            f"\\overbrace{{f({points[1]})}}",
            f"^{{{func(points[1])}}}",
            color=colors["point_2"]
        )

        # Position the right side elements
        right_group = VGroup(right_side_f1, plus_sign, right_side_f2).arrange(RIGHT)
        right_group.next_to(equals_sign, RIGHT)

        # Add outer overbrace to right side
        right_brace = MathTex(
            f"\\overbrace{{\\phantom{{ABC}}}}^{{{sum_of_individual_values}}}",
            color=RED if not is_superposition else colors["result_point"],
            font_size=14  # Reduce font size from default 48 to 24
        ).next_to(right_group, UP, buff=0.5)
        # Get original dimensions before stretching
        original_width = right_brace.width
        original_height = right_brace.height
        # Calculate scale factor and apply it proportionally
        scale_factor = right_group.width / original_width
        right_brace.scale(scale_factor)

        # Animate the transformations
        self.add(static_v_line_result, static_h_line_result, static_dot_result)
        self.play(Create(static_v_line_result), Create(static_h_line_result), Create(static_dot_result))
        
        # First write the left side
        self.play(Write(left_side))  # Write f(2+5) without the result
                
        self.play(Write(equals_sign))
        
        # Transform both the function expressions and their results
        self.play(
            ReplacementTransform(label_f1_part1[0].copy(), right_side_f1[0]),  # Transform f(2) to f(2)
            ReplacementTransform(label_f1_part2[0][1].copy(), right_side_f1[1]),  # Transform just the "4" to ^4
            ReplacementTransform(label_f2_part1[0].copy(), right_side_f2[0]),  # Transform f(5) to f(5)
            ReplacementTransform(label_f2_part2[0][1:].copy(), right_side_f2[1]),  # Transform just the "10" to ^10
        )
        self.play(Write(plus_sign))
        
        # Add the final overbrace with sum
        self.play(Write(right_brace.scale(0.6)))
        
        self.wait(2)
