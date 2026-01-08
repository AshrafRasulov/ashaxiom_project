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
    def static_metod(*args):
        """Собирает список конфигураций линий."""
        return list(args)

    @staticmethod
    def static_2D(data_list):
        """Рисует синхронизированный график. Исправлен импорт."""
        from .lib.graph.hGraph import hGraph
        return hGraph().render_static_2D(data_list)

    @staticmethod
    def version():
        return "2.3.0 (Academy Edition)"