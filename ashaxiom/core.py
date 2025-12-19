from .lib.main import AxiomMain

class Axiom:
    @staticmethod
    def start(initial_value=0):
        """Точка входа для создания цепочки вычислений"""
        return AxiomMain(initial_value)

    @staticmethod
    def version():
        return "0.2.0 (Piper Edition)"