"""
Clase Cabezera - Maneja la cabeza de lectura/escritura de la máquina de Turing

Esta clase controla la posición de la cabeza y las operaciones
de lectura y escritura en la cinta.
"""


class Cabezera:
    """
    Representa la cabeza de lectura/escritura de la máquina de Turing.
    
    La cabezera puede moverse por la cinta, leer y escribir símbolos.
    """
    
    def __init__(self, cinta):
        """
        Inicializa la cabezera con una cinta.
        
        Args:
            cinta (Cinta): La cinta sobre la cual operar
        """
        self.cinta = cinta
        self.posicion = 0  # Posición actual de la cabezera
    
    def leer(self):
        """
        Lee el símbolo en la posición actual.
        
        Returns:
            str: Símbolo en la posición actual
        """
        return self.cinta.leer(self.posicion)
    
    def escribir(self, simbolo):
        """
        Escribe un símbolo en la posición actual.
        
        Args:
            simbolo (str): Símbolo a escribir
        """
        self.cinta.escribir(self.posicion, simbolo)
    
    def mover_izquierda(self):
        """Mueve la cabezera una posición hacia la izquierda."""
        self.posicion -= 1
    
    def mover_derecha(self):
        """Mueve la cabezera una posición hacia la derecha."""
        self.posicion += 1
    
    def mover_a(self, posicion):
        """
        Mueve la cabezera a una posición específica.
        
        Args:
            posicion (int): Nueva posición de la cabezera
        """
        self.posicion = posicion
    
    def obtener_posicion(self):
        """
        Obtiene la posición actual de la cabezera.
        
        Returns:
            int: Posición actual
        """
        return self.posicion
    
    def mostrar_estado(self):
        """
        Muestra el estado actual de la cabezera y la cinta.
        
        Returns:
            str: Representación visual del estado
        """
        return f"Posición: {self.posicion}, Símbolo: '{self.leer()}', Cinta: {self.cinta.mostrar_cinta(self.posicion)}"
    
    def __str__(self):
        """Representación string de la cabezera."""
        return f"Cabezera(posición={self.posicion}, símbolo='{self.leer()}')"
    
    def __repr__(self):
        """Representación detallada de la cabezera."""
        return f"Cabezera(posición={self.posicion}, cinta={repr(self.cinta)})"
