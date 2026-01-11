from .core import Axiom
from .lib.threadManager import Threader
from .lib.pipUtil.console import Console
from .lib.pipUtil.convertData import DataConverter

thread = Threader()

def Convert(data):
    return DataConverter(data)

# Теперь пользователь может писать ashaxiom.Console(data)
__all__ = ["Axiom", "thread", "Console", "Convert"]