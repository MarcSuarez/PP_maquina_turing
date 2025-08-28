from math import sqrt

def sumar(a, b):
    return bin(a + b)
    
def restar(a, b):
    return bin(a - b)
    
def multiplicar(a, b):
    return bin(a * b)
    
def dividir(a, b):
    if b == 0:
        return "Error division por 0"
    return bin(a // b)
    
def potenciacion(a, b):
    return bin(a **b)
    
def raiz(a):
    return bin(int(sqrt(a)))