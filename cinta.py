"""
Clase Cinta - Representa la cinta de la máquina de Turing

Esta clase maneja la cinta infinita donde se almacenan los símbolos
que la máquina de Turing puede leer y escribir.
"""


class Cinta:
    """
    Representa la cinta infinita de la máquina de Turing.
    
    La cinta se implementa como una lista que puede crecer hacia
    ambos lados según sea necesario.
    """
    
    def __init__(self):
        """Inicializa una cinta vacía."""
        self.simbolos = []  # Lista de símbolos en la cinta
        self.posicion_inicial = 0  # Posición de referencia para el índice 0
    
    def escribir(self, posicion, simbolo):
        """
        Escribe un símbolo en la posición especificada.
        
        Args:
            posicion (int): Posición donde escribir
            simbolo (str): Símbolo a escribir
        """
        # Convertir posición relativa a índice de lista
        indice = posicion + self.posicion_inicial
        
        # Expandir la lista si es necesario
        while indice >= len(self.simbolos):
            self.simbolos.append(' ')  # Espacio en blanco por defecto
        
        while indice < 0:
            self.simbolos.insert(0, ' ')
            self.posicion_inicial += 1
            indice = posicion + self.posicion_inicial
        
        # Escribir el símbolo
        self.simbolos[indice] = simbolo
    
    def leer(self, posicion):
        """
        Lee el símbolo en la posición especificada.
        
        Args:
            posicion (int): Posición a leer
            
        Returns:
            str: Símbolo en esa posición (espacio si está vacía)
        """
        indice = posicion + self.posicion_inicial
        
        if 0 <= indice < len(self.simbolos):
            return self.simbolos[indice]
        else:
            return ' '  # Espacio en blanco para posiciones no escritas
    
    def limpiar(self):
        """Limpia toda la cinta."""
        self.simbolos = []
        self.posicion_inicial = 0
    
    def obtener_contenido(self, inicio=None, fin=None):
        """
        Obtiene el contenido de la cinta en un rango.
        
        Args:
            inicio (int): Posición inicial (opcional)
            fin (int): Posición final (opcional)
            
        Returns:
            str: Contenido de la cinta en el rango especificado
        """
        if not self.simbolos:
            return ""
        
        if inicio is None:
            inicio = -self.posicion_inicial
        if fin is None:
            fin = len(self.simbolos) - self.posicion_inicial
        
        contenido = []
        for i in range(inicio, fin):
            contenido.append(self.leer(i))
        
        return ''.join(contenido)
    
    def mostrar_cinta(self, posicion_cabezera=None, rango=10):
        """
        Muestra una representación visual de la cinta.
        
        Args:
            posicion_cabezera (int): Posición de la cabezera (opcional)
            rango (int): Número de posiciones a mostrar a cada lado
            
        Returns:
            str: Representación visual de la cinta
        """
        if not self.simbolos:
            return "[]"
        
        # Determinar el rango a mostrar
        if posicion_cabezera is not None:
            inicio = posicion_cabezera - rango
            fin = posicion_cabezera + rango + 1
        else:
            inicio = -self.posicion_inicial
            fin = len(self.simbolos) - self.posicion_inicial
        
        # Crear representación
        representacion = []
        for i in range(inicio, fin):
            simbolo = self.leer(i)
            if i == posicion_cabezera:
                representacion.append(f"[{simbolo}]")
            else:
                representacion.append(simbolo)
        
        return ''.join(representacion)
    
    def __str__(self):
        """Representación string de la cinta."""
        return self.obtener_contenido()
    
    def __repr__(self):
        """Representación detallada de la cinta."""
        return f"Cinta(simbolos={len(self.simbolos)}, posicion_inicial={self.posicion_inicial})"
