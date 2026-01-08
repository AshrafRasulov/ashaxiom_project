import ashaxiom

class AxiomVisionBridge:
    """
    Stand-alone application that executes AshAxiom library 
    based on manual input or direct task strings.
    (LatexOCR removed as per project update)
    """
    def __init__(self):
        print("[Vision App] Axiom System Bridge Active.")
        self.axiom = ashaxiom.Axiom.think()

    def process_and_solve(self, task_type, task_input):
        """
        Directly calls the Axiom Brain to solve a task.
        task_type: e.g., 'integral', 'limit', 'predict_3d'
        task_input: the expression or ticker
        """
        print(f"[Vision App] Processing Task: {task_type}")
        print(f"[Vision App] Input: {task_input}")
        
        # Call the library to solve
        # The Brain will automatically find the best expert(s)
        res = self.axiom.solve(task_type, expr=task_input, ticker=task_input)
        return res

if __name__ == "__main__":
    app = AxiomVisionBridge()
    # Example: solve an integral
    result = app.process_and_solve("integral", "x**2 + sin(x)")
    # If in Jupyter, result will display via its _repr_html_
    print(result)