from manim import*


class XYZAxes3D(ThreeDScene):
    def construct(self):
        # Set the 3D camera orientation
        self.set_camera_orientation(phi=75 * DEGREES, theta=30 * DEGREES)

        text = Text("Gabriel's Horn", font_size=30)
        text.set_color(WHITE)
        text.to_corner(UL)
        
        self.play(Write(text)) 
        self.wait(1) 
        self.play(FadeOut(text))
        
        # Create 3D axes
        axes = ThreeDAxes(
            x_range=[-5, 5, 1],
            y_range=[-5, 5, 1],
            z_range=[-5, 5, 1],
            x_length=6,
            y_length=6,
            z_length=6,
        )

        # Add labels
        labels = axes.get_axis_labels(x_label="x", y_label="y", z_label="z")

        # Add everything to the scene
        self.add(axes, labels)
        self.wait(2)