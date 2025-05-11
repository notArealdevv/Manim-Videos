from manim import *

class SolidOfRevolution(ThreeDScene):
    def construct(self):
        # Set up axes
        axes = ThreeDAxes(
            x_range=[0, 5],
            y_range=[0, 3],
            z_range=[0, 5],
            x_length=6,
            y_length=3,
            z_length=5
        )
        self.set_camera_orientation(phi=75 * DEGREES, theta=-45 * DEGREES)

        # Define the function
        curve = lambda x: np.sqrt(x)
        graph = axes.plot(curve, x_range=[0, 4], color=BLUE)

        # Region under the curve
        region = axes.get_area(graph, x_range=[0, 4], color=BLUE, opacity=0.5)

        # Labels
        fx_label = MathTex("f(x) = \\sqrt{x}").next_to(graph, UP)
        self.add(axes, graph, region, fx_label)

        self.wait(2)

        # Surface of revolution using parametric surface
        surface = Surface(
            lambda u, v: axes.c2p(
                u,
                np.sqrt(u) * np.cos(v),
                np.sqrt(u) * np.sin(v)
            ),
            u_range=[0, 4],
            v_range=[0, 2 * PI],
            resolution=(30, 30),
            fill_opacity=0.5,
            checkerboard_colors=[BLUE_D, BLUE_E],
        )

        # Add surface
        self.play(Create(surface), run_time=3)
        self.wait(2)

        # Disk slice demonstration
        x_val = 2
        radius = np.sqrt(x_val)
        thickness = 0.1

        disk = Cylinder(
            radius=radius,
            height=thickness,
            direction=RIGHT,
            fill_color=YELLOW,
            fill_opacity=0.8,
        ).move_to(axes.c2p(x_val, 0, 0))

        # Disk label
        disk_label = MathTex("dV = \\pi r^2 dx").scale(0.7)
        disk_label.next_to(disk, UP)

        self.play(FadeIn(disk), Write(disk_label))
        self.wait(2)

        # Show integral
        integral = MathTex(
            "V = \\int_0^4 \\pi (\\sqrt{x})^2 dx = \\int_0^4 \\pi x\\ dx"
        ).to_corner(UL)

        self.play(Write(integral))
        self.wait(3)

        # Animate rotating view
        self.begin_ambient_camera_rotation(rate=0.1)
        self.wait(6)
        self.stop_ambient_camera_rotation()
        self.wait()
