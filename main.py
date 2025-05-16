from manim import *

class MainVideo(Scene):
    def construct(self):
        func = MathTex(r"f(x) = \frac{1}{x}")
        self.play(Write(func), run_time=2)
        self.wait(2)

        #Move the function to top left
        self.play(func.animate.to_corner(UL))
        self.wait(1)

        # Create x and y axes
        axes1 = Axes(
            x_range=[-10, 10, 0.5],  # [min, max, step]
            y_range=[-5, 5, 0.5],
            axis_config={"include_numbers": Falsfrom manim import *

class MainVideo(Scene):
    def construct(self):
        func = MathTex(r"f(x) = \frac{1}{x}")
        self.play(Write(func), run_time=2)
        self.wait(2)

        #Move the function to top left
        self.play(func.animate.to_corner(UL))
        self.wait(1)

        # Create x and y axes
        axes1 = Axes(
            x_range=[-10, 10, 0.5],  # [min, max, step]
            y_range=[-5, 5, 0.5],
            axis_config={"include_numbers": False}
        )

        # Label axes
        labels = axes1.get_axis_labels(x_label="x", y_label="y")

        # Play smooth creation of axes
        self.play(Create(axes1), run_time=1, rate_func=smooth)
        self.play(Write(labels), run_time=1.5)

        self.wait(1)

        graph1_left = axes1.plot(lambda x: 1/x, x_range=[-5, -0.1], color=YELLOW)
        graph1_right = axes1.plot(lambda x: 1/x, x_range=[0.1, 5], color=YELLOW)

        self.play(Create(graph1_left), Create(graph1_right), run_time=3)



        # Fade out the graph
        self.play(FadeOut(labels), run_time=1)
        self.wait(1)

        # Create the new text
        new_text = Tex(r"Let's find the area under the curve")
        new_text.move_to(ORIGIN)

        # Transform the function text into the new one and move to center
        self.play(Transform(func, new_text))
        self.wait(2)
        }
        )

        # Label axes
        labels = axes1.get_axis_labels(x_label="x", y_label="y")

        # Play smooth creation of axes
        self.play(Create(axes1), run_time=1, rate_func=smooth)
        self.play(Write(labels), run_time=1.5)

        self.wait(1)

        graph1_left = axes1.plot(lambda x: 1/x, x_range=[-5, -0.1], color=YELLOW)
        graph1_right = axes1.plot(lambda x: 1/x, x_range=[0.1, 5], color=YELLOW)

        self.play(Create(graph1_left), Create(graph1_right), run_time=3)



        # Fade out the graph
        self.play(FadeOut(labels), run_time=1)
        self.wait(1)

        # Create the new text
        new_text = Tex(r"Let's find the area under the curve")
        new_text.move_to(ORIGIN)

        # Transform the function text into the new one and move to center
        self.play(Transform(func, new_text))
        self.wait(2)
