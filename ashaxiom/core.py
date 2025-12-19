class Axiom:
    def __init__(self, name="AshAxiom User"):
        self.name = name
    
    def say_hello(self):
        return f"Привет, {self.name}! Your lib is run successfully!"

    @staticmethod
    def version():
        return "0.1.0"