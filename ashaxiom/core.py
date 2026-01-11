# from .lib.main import AxiomMain
# from .lib.brain.AxiomIntelligence import BrainCore

# class Axiom:
#     @staticmethod
#     def start(initial_value=0):
#         return AxiomMain(initial_value)
    
#     @staticmethod
#     def think(mode="solve"):
#         return BrainCore(AxiomMain(), mode=mode)
    
#     @staticmethod
#     def static_metod(*args):
#         """Собирает список GraphicConfig для мульти-графика."""
#         return list(args)

#     @staticmethod
#     def static_2D(data_list):
#         """Рисует синхронизированный 2D график. Импорт внутри для стабильности."""
#         from .lib.graph.hGraph import hGraph
#         return hGraph().render_static_2D(data_list)

#     @staticmethod
#     def version():
#         return "2.3.5 (Full Integration Edition)"


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
        """Собирает список объектов для мульти-графика."""
        return list(args)

    @staticmethod
    def static_2D(data_list):
        """Синхронизированная 2D визуализация."""
        from .lib.graph.hGraph import hGraph
        return hGraph().render_static_2D(data_list)

    @staticmethod
    def version():
        return "2.3.8 (Consolidated Global Edition)"