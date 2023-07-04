

from typing import Any


class ClosureOperator(object):
    """
    Clase para representar un operador de clausura
    """

    def __init__(self, func, universe, arity=None, name=""):
        assert callable(func)
        assert arity == None or (isinstance(arity, int) and arity > 0)
        self.func = func
        self.universe = universe
        self.arity = arity
        self.name = name
        self.class_name = type(self).__name__
    
    def __call__(self, *args: Any) -> Any:
        pass

    def join(self, first_closed, second_closed):
        """
        Devuelve el cerrado generado por 2 cerrados
        """

        return True

    def closed_sets(self):
        """
        Devuelve una lista con los conjuntos cerrados del operador
        """
        return True



if __name__ == "__main__":
    import doctest
    doctest.testmod()