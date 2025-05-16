from manim import*

class XYZAxes3D(ThreeDScene):
    def construct(self):
        title = Text("Gabriel's Horn", font_size=15)
        
        self.play(Write(title))  # Animate the writing
        self.wait(1)

        # Move to upper-left corner (using coordinates)
        self.play(
            title.animate.to_corner(UL),
            run_time=1
        )

        self.wait(1)
        
        # Create 3D axes
        axes = ThreeDAxes(
            x_range=[-5, 5],
            y_range=[-5, 5],
            x_length=10,
            y_length=10,
        )

        # Add labels
        labels = axes.get_axis_labels(x_label="x", y_label="y")

        # Add everything to the scene
        self.add(axes, labels)
        self.wait(2)