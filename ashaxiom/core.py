from .lib.main import AxiomMain
from .lib.brain.AxiomIntelligence import BrainCore

class Axiom:
    """
    Main Gateway for AshAxiom Framework.
    Provides entry points for direct math computation, intelligent analysis, 
    and synchronized visualization.
    """
    @staticmethod
    def start(initial_value=0):
        """Initializes the Axiom core with a starting numeric value or collection."""
        return AxiomMain(initial_value)
    
    @staticmethod
    def think(mode="solve"):
        """Initializes the Parallel Intelligence engine for expert consensus."""
        return BrainCore(AxiomMain(), mode=mode)
    
    @staticmethod
    def static_metod(*args):
        """Helper to aggregate multiple Axiom objects into a list for batch rendering."""
        return list(args)

    @staticmethod
    def static_2D(data_list):
        """Triggers synchronized 2D rendering for multi-asset comparison."""
        from .lib.graph.hGraph import hGraph
        return hGraph().render_static_2D(data_list)

    @staticmethod
    def version():
        """Returns the current framework version (Global Intelligence Edition)."""
        return "2.4.3 (Consolidated Global Edition)"