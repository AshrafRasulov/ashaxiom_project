# AshAxiom Library 🚀
**The Intelligent Analytical Ecosystem for Higher Mathematics in Jupyter.**

AshAxiom is a high-level Python framework designed for scientific research, symbolic mathematics, and data visualization. It features a dynamic AI engine that transforms classical textbooks into an interactive calculation environment.

---

## 🌟 Key Features
- **Axiom Brain (AI)**: An intelligent dispatcher that navigates through sections/authors and maps user intent to the correct mathematical model.
- **Dynamic Scopes**: Filter knowledge by Author or Section to accelerate discovery and minimize conflicts.
- **Fluent Chaining (Piping)**: Build complex analytical pipelines using intuitive dot-notation.
- **Task Parallelization**: Multithreaded execution for heavy computational groups.
- **Output Explorer**: Interactive, scrollable HTML output with precision control (up to 15 decimal places).
- **2D/3D Visualization**: High-level wrappers for complex surfaces and mathematical plotting.

---

## 📚 Integrated Knowledge Base
AshAxiom is systematically trained on world-class mathematical literature:
- **M.L. Krasnov et al.** (Volumes 1-7): Full implementation of vector algebra, ODEs, TFCP, probability, and optimization.
- **G.M. Fikhtengolts** (Volumes 1-3): Deep integration of differential and integral calculus.

---

## 📦 Dependencies
Ensure the following are installed in your environment:
`numpy`, `sympy`, `matplotlib`, `pandas`, `openpyxl`, `scipy`.

---

## 🚀 Usage Examples

### 1. Intelligent Solving (Brain Mode)
```python
import ashaxiom
# Solve a 2D geometry problem by author
res = (ashaxiom.Axiom.think()
       .author("Krasnov")
       .solve("plane", p1=(1,0,0), p2=(0,1,0), p3=(0,0,1)))
display(res)


# Browse what the brain knows
brain = ashaxiom.Axiom.think("library")
print(brain.sections().show())
print(brain.section("hMath").show()) # Lists authors