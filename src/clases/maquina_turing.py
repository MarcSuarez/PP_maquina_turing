"""
Clase MaquinaTuring - Implementación principal de la máquina de Turing

Esta clase coordina la cinta, la cabezera y las operaciones matemáticas
para crear una máquina de Turing funcional.
"""

from .cinta import Cinta
from .cabezera import Cabezera
from math import sqrt


class MaquinaTuring:
    """
    Máquina de Turing para operaciones matemáticas.
    
    Esta clase integra todos los componentes necesarios para
    realizar operaciones matemáticas usando el concepto de
    máquina de Turing.
    """
    
    def __init__(self):
        """Inicializa la máquina de Turing."""
        self.cinta = Cinta()
        self.cabezera = Cabezera(self.cinta)
        self.estado = "inicial"  # Estado actual de la máquina
        self.historial = []  # Historial de operaciones realizadas
    
    def cambiar_estado(self, nuevo_estado):
        """
        Cambia el estado de la máquina.
        
        Args:
            nuevo_estado (str): Nuevo estado de la máquina
        """
        self.estado = nuevo_estado
    
    def obtener_estado(self):
        """
        Obtiene el estado actual de la máquina.
        
        Returns:
            str: Estado actual
        """
        return self.estado
    
    def preparar_entrada(self, numero1, numero2=None):
        """
        Prepara la cinta con los números de entrada.
        
        Args:
            numero1 (int): Primer número
            numero2 (int): Segundo número (opcional)
        """
        # Limpiar la cinta
        self.cinta.limpiar()
        self.cabezera.mover_a(0)
        
        # Escribir los números en la cinta
        entrada = str(numero1)
        if numero2 is not None:
            entrada += "#" + str(numero2)  # Usar # como separador
        
        for i, simbolo in enumerate(entrada):
            self.cabezera.escribir(simbolo)
            self.cabezera.mover_derecha()
        
        # Volver al inicio
        self.cabezera.mover_a(0)
        self.cambiar_estado("preparado")
    
    def escribir_resultado(self, resultado):
        """
        Escribe el resultado en la cinta.
        
        Args:
            resultado (int): Resultado a escribir
        """
        # Limpiar la cinta y escribir solo el resultado
        self.cinta.limpiar()
        self.cabezera.mover_a(0)
        
        resultado_str = str(resultado)
        for simbolo in resultado_str:
            self.cabezera.escribir(simbolo)
            self.cabezera.mover_derecha()
        
        self.cabezera.mover_a(0)
        self.cambiar_estado("completado")
    
    def sumar(self, a, b):
        """
        Suma dos números usando la máquina de Turing.
        
        Args:
            a (int): Primer número
            b (int): Segundo número
            
        Returns:
            int: Resultado de la suma
        """
        # Preparar entrada
        self.preparar_entrada(a, b)
        
        # Realizar la operación
        resultado = a + b
        
        # Escribir resultado en la cinta
        self.escribir_resultado(resultado)
        
        # Registrar en historial
        self.historial.append(f"Suma: {a} + {b} = {resultado}")
        
        return resultado
    
    def restar(self, a, b):
        """
        Resta dos números usando la máquina de Turing.
        
        Args:
            a (int): Primer número
            b (int): Segundo número
            
        Returns:
            int: Resultado de la resta
        """
        self.preparar_entrada(a, b)
        resultado = a - b
        self.escribir_resultado(resultado)
        self.historial.append(f"Resta: {a} - {b} = {resultado}")
        return resultado
    
    def multiplicar(self, a, b):
        """
        Multiplica dos números usando la máquina de Turing.
        
        Args:
            a (int): Primer número
            b (int): Segundo número
            
        Returns:
            int: Resultado de la multiplicación
        """
        self.preparar_entrada(a, b)
        resultado = a * b
        self.escribir_resultado(resultado)
        self.historial.append(f"Multiplicación: {a} * {b} = {resultado}")
        return resultado
    
    def dividir(self, a, b):
        """
        Divide dos números usando la máquina de Turing.
        
        Args:
            a (int): Dividendo
            b (int): Divisor
            
        Returns:
            int o str: Resultado de la división o mensaje de error
        """
        self.preparar_entrada(a, b)
        if b == 0:
            resultado = "Error: División por cero"
        else:
            resultado = a // b
        
        if isinstance(resultado, str):  # Error
            self.cinta.limpiar()
            self.cabezera.mover_a(0)
            for simbolo in "ERROR":
                self.cabezera.escribir(simbolo)
                self.cabezera.mover_derecha()
            self.cambiar_estado("error")
        else:
            self.escribir_resultado(resultado)
        
        self.historial.append(f"División: {a} / {b} = {resultado}")
        return resultado
    
    def potenciacion(self, base, exponente):
        """
        Calcula la potencia usando la máquina de Turing.
        
        Args:
            base (int): Base
            exponente (int): Exponente
            
        Returns:
            int: Resultado de la potenciación
        """
        self.preparar_entrada(base, exponente)
        resultado = base ** exponente
        self.escribir_resultado(resultado)
        self.historial.append(f"Potenciación: {base}^{exponente} = {resultado}")
        return resultado
    
    def raiz_cuadrada(self, numero):
        """
        Calcula la raíz cuadrada usando la máquina de Turing.
        
        Args:
            numero (int): Número del cual calcular la raíz
            
        Returns:
            int: Resultado de la raíz cuadrada
        """
        self.preparar_entrada(numero)
        if numero < 0:
            resultado = "Error: No se puede calcular la raíz cuadrada de un número negativo"
        else:
            resultado = int(sqrt(numero))
        self.escribir_resultado(resultado)
        self.historial.append(f"Raíz cuadrada: √{numero} = {resultado}")
        return resultado
    
    def mostrar_estado(self):
        """
        Muestra el estado actual de la máquina.
        
        Returns:
            str: Estado detallado de la máquina
        """
        estado_info = f"""
Estado de la Máquina de Turing:
- Estado: {self.estado}
- Posición de la cabezera: {self.cabezera.obtener_posicion()}
- Símbolo actual: '{self.cabezera.leer()}'
- Cinta: {self.cinta.mostrar_cinta(self.cabezera.obtener_posicion())}
- Contenido de la cinta: '{self.cinta.obtener_contenido()}'
        """
        return estado_info.strip()
    
    def obtener_historial(self):
        """
        Obtiene el historial de operaciones.
        
        Returns:
            list: Lista de operaciones realizadas
        """
        return self.historial.copy()
    
    def limpiar_historial(self):
        """Limpia el historial de operaciones."""
        self.historial = []
    
    def reiniciar(self):
        """Reinicia la máquina a su estado inicial."""
        self.cinta.limpiar()
        self.cabezera.mover_a(0)
        self.cambiar_estado("inicial")
        self.limpiar_historial()
    
    def __str__(self):
        """Representación string de la máquina."""
        return f"MaquinaTuring(estado={self.estado}, posición={self.cabezera.obtener_posicion()})"
    
    def __repr__(self):
        """Representación detallada de la máquina."""
        return f"MaquinaTuring(estado={self.estado}, cinta={repr(self.cinta)}, cabezera={repr(self.cabezera)})"
