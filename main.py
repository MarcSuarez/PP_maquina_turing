"""
Programa principal para la Máquina de Turing de Operaciones Matemáticas

Este programa demuestra el uso de la máquina de Turing para realizar
operaciones matemáticas básicas.
"""

from maquina_turing import MaquinaTuring


def mostrar_menu():
    """Muestra el menú de opciones."""
    print("\n" + "="*50)
    print("🤖 MÁQUINA DE TURING - OPERACIONES MATEMÁTICAS")
    print("="*50)
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Potenciación")
    print("6. Raíz cuadrada")
    print("7. Ver estado de la máquina")
    print("8. Ver historial")
    print("9. Reiniciar máquina")
    print("0. Salir")
    print("="*50)


def obtener_numero(mensaje):
    """
    Obtiene un número entero del usuario.
    
    Args:
        mensaje (str): Mensaje a mostrar
        
    Returns:
        int: Número ingresado por el usuario
    """
    while True:
        try:
            numero = int(input(mensaje))
            return numero
        except ValueError:
            print("❌ Por favor, ingresa un número entero válido.")


def ejecutar_operacion(tm, opcion):
    """
    Ejecuta la operación seleccionada.
    
    Args:
        tm (MaquinaTuring): Instancia de la máquina de Turing
        opcion (int): Opción seleccionada
    """
    if opcion == 1:  # Suma
        a = obtener_numero("Ingresa el primer número: ")
        b = obtener_numero("Ingresa el segundo número: ")
        resultado = tm.sumar(a, b)
        print(f"✅ Resultado: {a} + {b} = {resultado}")
        
    elif opcion == 2:  # Resta
        a = obtener_numero("Ingresa el primer número: ")
        b = obtener_numero("Ingresa el segundo número: ")
        resultado = tm.restar(a, b)
        print(f"✅ Resultado: {a} - {b} = {resultado}")
        
    elif opcion == 3:  # Multiplicación
        a = obtener_numero("Ingresa el primer número: ")
        b = obtener_numero("Ingresa el segundo número: ")
        resultado = tm.multiplicar(a, b)
        print(f"✅ Resultado: {a} * {b} = {resultado}")
        
    elif opcion == 4:  # División
        a = obtener_numero("Ingresa el dividendo: ")
        b = obtener_numero("Ingresa el divisor: ")
        resultado = tm.dividir(a, b)
        if isinstance(resultado, str):
            print(f"❌ {resultado}")
        else:
            print(f"✅ Resultado: {a} / {b} = {resultado}")
            
    elif opcion == 5:  # Potenciación
        base = obtener_numero("Ingresa la base: ")
        exponente = obtener_numero("Ingresa el exponente: ")
        resultado = tm.potenciacion(base, exponente)
        print(f"✅ Resultado: {base}^{exponente} = {resultado}")
        
    elif opcion == 6:  # Raíz cuadrada
        numero = obtener_numero("Ingresa el número: ")
        resultado = tm.raiz_cuadrada(numero)
        print(f"✅ Resultado: √{numero} = {resultado}")


def mostrar_estado(tm):
    """Muestra el estado actual de la máquina."""
    print("\n📊 ESTADO DE LA MÁQUINA DE TURING:")
    print("-" * 40)
    print(tm.mostrar_estado())


def mostrar_historial(tm):
    """Muestra el historial de operaciones."""
    historial = tm.obtener_historial()
    
    if not historial:
        print("\n📝 No hay operaciones en el historial.")
    else:
        print(f"\n📝 HISTORIAL DE OPERACIONES ({len(historial)} operaciones):")
        print("-" * 50)
        for i, operacion in enumerate(historial, 1):
            print(f"{i:2d}. {operacion}")


def main():
    """Función principal del programa."""
    print("🚀 Iniciando Máquina de Turing...")
    
    # Crear instancia de la máquina de Turing
    tm = MaquinaTuring()
    
    print("✅ Máquina de Turing inicializada correctamente.")
    
    while True:
        mostrar_menu()
        
        try:
            opcion = int(input("\nSelecciona una opción: "))
            
            if opcion == 0:
                print("\n👋 ¡Hasta luego!")
                break
                
            elif opcion in range(1, 7):
                ejecutar_operacion(tm, opcion)
                
            elif opcion == 7:
                mostrar_estado(tm)
                
            elif opcion == 8:
                mostrar_historial(tm)
                
            elif opcion == 9:
                tm.reiniciar()
                print("🔄 Máquina reiniciada correctamente.")
                
            else:
                print("❌ Opción no válida. Por favor, selecciona una opción del 0 al 9.")
                
        except ValueError:
            print("❌ Por favor, ingresa un número válido.")
        except KeyboardInterrupt:
            print("\n\n👋 ¡Hasta luego!")
            break
        except Exception as e:
            print(f"❌ Error inesperado: {e}")
        
        # Pausa antes de continuar
        input("\nPresiona Enter para continuar...")


def ejecutar_ejemplos():
    """Ejecuta ejemplos de uso de la máquina de Turing."""
    print("🧪 EJECUTANDO EJEMPLOS DE USO")
    print("=" * 40)
    
    tm = MaquinaTuring()
    
    # Ejemplos de operaciones
    ejemplos = [
        ("Suma", lambda: tm.sumar(3, 5)),
        ("Resta", lambda: tm.restar(10, 4)),
        ("Multiplicación", lambda: tm.multiplicar(7, 6)),
        ("División", lambda: tm.dividir(20, 4)),
        ("Potenciación", lambda: tm.potenciacion(2, 3)),
        ("Raíz cuadrada", lambda: tm.raiz_cuadrada(16))
    ]
    
    for nombre, operacion in ejemplos:
        print(f"\n🔹 {nombre}:")
        resultado = operacion()
        print(f"   Resultado: {resultado}")
        print(f"   Estado: {tm.obtener_estado()}")
        print(f"   Cinta: {tm.cinta.mostrar_cinta(tm.cabezera.obtener_posicion())}")
    
    print(f"\n📝 Historial completo:")
    for operacion in tm.obtener_historial():
        print(f"   • {operacion}")


if __name__ == "__main__":
    # Preguntar al usuario qué modo desea usar
    print("Selecciona el modo de ejecución:")
    print("1. Modo interactivo (menú)")
    print("2. Ejecutar ejemplos")
    
    try:
        modo = int(input("Ingresa tu opción (1 o 2): "))
        
        if modo == 1:
            main()
        elif modo == 2:
            ejecutar_ejemplos()
        else:
            print("❌ Opción no válida. Ejecutando modo interactivo por defecto.")
            main()
            
    except ValueError:
        print("❌ Entrada no válida. Ejecutando modo interactivo por defecto.")
        main()
    except KeyboardInterrupt:
        print("\n👋 ¡Hasta luego!")
