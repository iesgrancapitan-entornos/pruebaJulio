"""
Clase Perro.

Autor: Monica Blanco
"""
class Perro:
    """
    Genera la clase Perro
    """

    def ladrar(self):
        """

        :return: devuelveme  ladrar
        """
        print(self.method_guau());

    def method_guau(self):
        """

        :return: devuelveme ladrar
        """
        return 'Guau'


p = Perro();
p.ladrar();
