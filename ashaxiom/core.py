from .lib.main import AxiomMain
from .lib.brain.AxiomIntelligence import BrainCore

class Axiom:
    @staticmethod
    def start(initial_value=0):
        return AxiomMain(initial_value)
    
    @staticmethod
    def think(mode="solve"):
        return BrainCore(AxiomMain(), mode=mode)

    @staticmethod
    def version():
        return "2.2.0 (Academy Edition)"