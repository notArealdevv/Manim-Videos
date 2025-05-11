# Gabriel's Horn – Visualized with Manim

This project uses [Manim](https://www.manim.community/) to create a mathematical animation that visualizes **Gabriel’s Horn**, a fascinating solid of revolution formed by rotating the curve y=1/x about the x-axis and bounded by the region [1, infinity].

Despite having an **infinite surface area**, Gabriel’s Horn encloses only a **finite volume** — a classic paradox in calculus and mathematical analysis.

---

## 🎥 What the Video Shows

- The function \( f(x) = \frac{1}{x} \) graphed on the interval \([1, \infty)\)
- A rotating animation showing the formation of the 3D solid
- An explanation of how the volume converges (finite) while the surface area diverges (infinite)
- Labels, formulas, and smooth camera transitions for clarity

---

## 📂 Files Included

- `gabriels_horn.py`: Manim code for generating the animation
- `README.md`: Project documentation (this file)
- `output/`: Folder where rendered videos will be saved (created after rendering)

---

## 🧮 Math Behind Gabriel's Horn
How can we find the volume of the surface generated?

First, let's find the area of the cross section. The cross section will be a circle with the area, A(x)= pi(r^2).
The radius will be equal to the function f(x). Therefore the area A(x)= pi [f(x)]^2).

- **Volume:**
Let's find the volume of the surface generated. We know volume(v)= Area x height.
Volume, v(x)= Area x dx. Where dx is the height of the cross section.
To find the volume of the entire surface, integrate it from 1 to infinity.

  \[
  V(x) = \pi \int_1^\infty \left(\frac{1}{x}\right)^2 dx = \pi
  \]

- **Surface Area:**  
  \[
  A = 2\pi \int_1^\infty \frac{1}{x} \sqrt{1 + \left(-\frac{1}{x^2}\right)^2} dx \rightarrow \infty
  \]

---

## 🚀 How to Run

1. **Install Manim** (if you haven’t already):
   ```bash
   pip install manim
