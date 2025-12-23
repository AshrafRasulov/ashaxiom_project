from .lib.main import AxiomMain
from .lib.brain.AxiomIntelligence import BrainCore

class Axiom:
    @staticmethod
    def start(initial_value=0):
        return AxiomMain(initial_value)
    
    @staticmethod
    def think(mode="solve"):
        """Entry to Intelligent Interface."""
        return BrainCore(AxiomMain(), mode=mode)

    @staticmethod
    def version():
        return "1.3.0 (Trading Analysis)"