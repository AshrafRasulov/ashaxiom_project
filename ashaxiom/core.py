from .lib.main import AxiomMain

class Axiom:
    """
    Main entry point for the AshAxiom library.
    """
    @staticmethod
    def start(initial_value=0):
        """Initializes a new calculation chain."""
        return AxiomMain(initial_value)

    @staticmethod
    def version():
        """Returns the current library version."""
        return "0.3.0 (English Edition)"