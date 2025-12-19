from .lib.main import AxiomMain
from .lib.brain.AxiomIntelligence import BrainCore

class Axiom:
    """
    Main entry point for the AshAxiom library.
    """
    @staticmethod
    def start(initial_value=0):
        """Initializes a new calculation chain."""
        return AxiomMain(initial_value)
    
    @staticmethod
    def think():
        """Returns the Brain instance for high-level automated solving."""
        return BrainCore(AxiomMain())

    @staticmethod
    def version():
        """Returns the current library version."""
        return "0.4.0 (Axiom Intelligence Edition)"