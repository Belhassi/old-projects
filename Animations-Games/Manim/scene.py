from manim import *


class CreateCircle(Scene):
    def construct(self):
        circle = Circle().set_color(RED_D)  # create a circle
        circle.set_fill(RED, opacity=0.5)  # set the color and transparency
        self.play(Create(circle), run_time=2)  # show the circle on screen

class SquareToCircle(Scene):
    def construct(self):
        square = Square().set_fill(BLUE, opacity=0.5)
        square.rotate(PI/4)

        circle = Circle().set_fill(PINK, opacity=0.5)

        self.play(Create(square))
        self.play(Transform(square, circle), run_time=2)
        self.play(FadeOut(square))

class SquareAndCircle(Scene):
    def construct(self):
        circle = Circle()
        circle.set_fill(PINK, opacity=0.5)

        square = Square()
        square.set_fill(BLUE, opacity=0.5)
        square.next_to(circle, UP, buff=0.5)

        self.play(Create(square), Create(circle))
        
        self.next_section()
        self.play(Transform(square, circle), Transform(circle, square))
        self.play(FadeOut(square), FadeOut(circle))


### Not working
class SquareRotation(Scene):
    def construct(self):
        square = Square()
        square.set_fill(BLUE)

        self.play(Create(square))
        for i in range(10, 1, -1):
            square.rotate(PI/i)

            self.play(Create(square))
### Not working

class AnimateSquareRotation(Scene):
    def construct(self):
        square = Square().set_fill(BLUE)

        self.play(Create(square))
        self.play(Rotate(square, PI), run_time=10)

class AnimateSquareToCircle(Scene):
    def construct(self):
        circle = Circle()
        square = Square()
        
        self.play(Create(square))
        self.play(square.animate.rotate(PI/4))
        self.play(Transform(square, circle))
        self.play(square.animate.set_fill(PINK, opacity=0.5))
        self.play(FadeOut(square))

class FlipAndShift(Scene):
    def construct(self):
        circle = Circle().set_fill(PINK)
        square = Square().set_fill(BLUE)

        self.play(Create(circle))
        self.play(circle.animate.flip())
        self.play(Transform(circle, square))
        self.play(circle.animate.shift(2*UP))

class DifferentRotations(Scene):
    def construct(self):
        left_square = Square(color=BLUE, fill_opacity=0.7).shift(2 * LEFT, 2 * UP)
        right_square = Square(color=GREEN, fill_opacity=0.7).shift(2 * RIGHT, 2 * DOWN)
        self.play(
            left_square.animate.rotate(PI), Rotate(right_square, angle=PI), run_time=2
        )
        self.wait()

class ToyExample(Scene):
    def construct(self):
        orange_square = Square(color=ORANGE, fill_opacity=0.5)
        blue_circle = Circle(color=BLUE, fill_opacity=0.5)
        self.add(orange_square)
        self.play(ReplacementTransform(orange_square, blue_circle, run_time=3))
        small_dot = Dot()
        small_dot.add_updater(lambda mob: mob.next_to(blue_circle, DOWN))
        self.play(Create(small_dot))
        self.play(blue_circle.animate.shift(RIGHT))
        self.wait()
        self.play(FadeOut(blue_circle, small_dot))