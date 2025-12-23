import ashaxiom
from pix2tex.cli import LatexOCR
from PIL import Image
import sympy as sp

class AxiomVisionBridge:
    """
    Stand-alone application that uses specialized AI 
    to read complex math and execute AshAxiom library.
    """
    def __init__(self):
        print("[Vision App] Loading Mathematical Neural Network...")
        self.model = LatexOCR() # Specialized AI for Math
        self.axiom = ashaxiom.Axiom.think()

    def process_and_solve(self, image_path):
        print(f"[Vision App] Analyzing image: {image_path}")
        
        # 1. AI reads the formula as LaTeX
        img = Image.open(image_path)
        latex_code = self.model(img)
        print(f"[Vision App] Recognized LaTeX: {latex_code}")
        
        # 2. Convert LaTeX to SymPy (so AshAxiom can understand it)
        # We try to find keywords like 'exp', 'sin', 'log' to guess the task
        task_query = ""
        if "exp" in latex_code or "sigma" in latex_code:
            task_query = "probability" # If it looks like distribution
        elif "int" in latex_code:
            task_query = "integrate"
            
        print(f"[Vision App] Intent detected: {task_query}")
        
        # 3. Call the library to solve
        # (For now, let's just simplify the recognized expression as a test)
        res = self.axiom.solve('simplify', expr=latex_code)
        return res

if __name__ == "__main__":
    app = AxiomVisionBridge()
    # Replace with your actual file 'task.jpg'
    result = app.process_and_solve("task.jpg")
    display(result)