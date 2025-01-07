from manim import *

class PiCreatureDemo(Scene):
    def construct(self):
        # Create a Pi creature
        pi = SVGMobject("assets/PiCreatures_plain.svg")
        pi.scale(2)
        pi.set_stroke(width=3)  # Set initial stroke width

        # Initial animation
        self.play(Create(pi))
        self.wait()

        # Move animation
        self.play(
            pi.animate.shift(RIGHT * 2),
            run_time=2
        )
        self.wait()

        # Color change animation
        self.play(
            pi.animate.set_color(BLUE),
            run_time=1
        )
        self.wait()
            
        # Transform to thinking
        thinking_pi = SVGMobject("assets/PiCreatures_thinking.svg")
        thinking_pi.scale(2)
        thinking_pi.set_stroke(width=3)
        thinking_pi.set_color(BLUE)  # Match the current color
        thinking_pi.move_to(pi)
        self.play(Transform(pi, thinking_pi))
        self.wait()
            
        # Transform to surprised
        surprised_pi = SVGMobject("assets/PiCreatures_surprised.svg")
        surprised_pi.scale(2)
        surprised_pi.set_stroke(width=3)
        surprised_pi.set_color(BLUE)  # Match the current color
        surprised_pi.move_to(pi)
        self.play(Transform(pi, surprised_pi))
        self.wait()

class PiCreatureEmotions(Scene):
    def construct(self):
        # Create different Pi creatures
        pi_plain = SVGMobject("assets/PiCreatures_plain.svg")
        pi_happy = SVGMobject("assets/PiCreatures_happy.svg")
        pi_confused = SVGMobject("assets/PiCreatures_confused.svg")

        # Set consistent styles
        for pi in [pi_plain, pi_happy, pi_confused]:
            pi.set_stroke(width=3)

        # Position them
        pi_group = Group(pi_plain, pi_happy, pi_confused).arrange(RIGHT, buff=1)
        
        self.play(Create(pi_group))
        self.wait(2)