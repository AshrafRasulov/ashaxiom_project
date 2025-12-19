# AshAxiom Library 🚀
**The Intelligent Analytical Framework for Higher Mathematics and Scientific Research.**

AshAxiom is a high-level Python ecosystem specifically optimized for Jupyter Notebook. It combines a dynamic modular architecture with an AI-driven "Brain" for intent recognition, making complex mathematical workflows intuitive and automated.

---

## 🌟 Key Features

- **Dynamic Discovery Engine**: Automatically scans and indexes mathematical modules (hmBooks) from subdirectories. Add a file, and the library learns instantly.
- **Axiom Intelligence (The Brain)**: Fuzzy-search logic that maps user intent to mathematical solvers. It intelligently handles argument synonyms (e.g., automatically maps `expr` to `expr_str` or `equation`).
- **Fluent Chaining (Piping)**: Build complex calculation pipelines using intuitive "LINQ-style" syntax where every method returns the instance.
- **Scientific Visualization**: Native 2D and 3D plotting with automatic data flattening for robust rendering of complex matrices.
- **Hardware Optimized**: Built-in CPU detection and batch task parallelization via a dedicated Thread Manager.
- **Output Explorer**: Interactive, scrollable HTML output container with precision control (`.precision(n)`) for large numerical datasets.

---

## 📚 Scientific Knowledge Base
AshAxiom is systematically trained on the fundamental 7-volume series **"All Higher Mathematics" by M.L. Krasnov et al.**:

*   **Vol 1**: Analytical Geometry, Vectors, Matrices, and Function Analysis. ✅
*   **Vol 2**: Field Theory, Vector Analysis, and ODEs. ✅
*   **Vol 3**: Numerical Series, Fourier Series, and Multiple Integrals. ✅
*   **Vol 4**: Complex Variables (TFCP), Laplace Transforms, and Special Functions. ✅
*   **Vol 5**: Probability Theory, Mathematical Statistics, and Game Theory. ✅
*   **Vol 6**: Calculus of Variations, Numerical Methods, and Spline Theory. ✅
*   **Vol 7**: Number Theory, Graph Theory, and Combinatorics. ✅

---

## 📦 Dependencies
To ensure all modules work correctly, install the following:
```bash
pip install numpy sympy matplotlib pandas openpyxl scipy
🚀 Quick Start
1. Using the Intelligent Brain (Automated Solving)
The Brain recognizes the task and maps your "lazy" arguments to the correct internal parameters:
code
Python
import ashaxiom
res = ashaxiom.Axiom.think().solve('fourier', expr='x**2', n=5)
display(res)
2. Using Method Chaining (The Pipe)
code
Python
import ashaxiom
# Calculate plane equation and format output in one go
plane = (ashaxiom.Axiom.start()
         .plane_from_3_points((1,0,0), (0,1,0), (0,0,1))
         .precision(3))
display(plane)
3. Visualizing 3D Models
code
Python
import ashaxiom
# The library automatically flattens meshgrids for 3D rendering
ashaxiom.Axiom.start(Z_data).plot3D(X_grid, Y_grid, color='auto')
🏗 Project Structure
code
Text
ashaxiom/
├── lib/
│   ├── brain/         # Axiom Intelligence (AxiomIntelligence.py)
│   │   └── libBrain/  # AI Mapping & Reflection Utilities
│   ├── hMath/         # Core Mathematics Logic
│   │   └── hmBooks/   # Digital Library (MLKrasnov Vols 1-7)
│   ├── graph/         # Visualization Engine (2D/3D)
│   ├── data/          # Export Tools (Excel, JSON)
│   ├── pipUtil/       # Scanners, Hardware API & Core Logic
│   └── application.py # UI/UX Layer: Explorer & Precision
├── core.py            # Main Library Entry Point
└── setup.py           # Local Installation Configuration
🛠 Installation
To install AshAxiom in development mode:
code
Bash
git clone https://github.com/AshrafRasulov/ashaxiom_project.git
cd ashaxiom_project
pip install -e .
Author: Ashraf Rasulov
Version: 1.0.0 (Grand Finale Edition)