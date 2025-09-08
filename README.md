# Máquina de Turing para Operaciones Matemáticas

## Descripción
Implementación simple de una máquina de Turing en Python para realizar operaciones matemáticas básicas.

## Estructura del Proyecto

```
proyecto_primer_corte/
├── README.md              # Este archivo
├── maquina_turing.py      # Clase principal de la máquina de Turing
├── cinta.py              # Clase para manejar la cinta
├── cabezera.py           # Clase para manejar la cabezera de lectura/escritura
├── operaciones.py        # Operaciones matemáticas (archivo existente)
└── main.py               # Programa principal
```

## Clases Principales

### 1. Cinta (cinta.py)
- Maneja la cinta infinita de la máquina de Turing
- Operaciones de lectura y escritura
- Representación visual de la cinta

### 2. Cabezera (cabezera.py)
- Controla la posición de la cabeza de lectura/escritura
- Maneja el movimiento izquierda/derecha
- Lee y escribe símbolos en la cinta

### 3. Máquina de Turing (maquina_turing.py)
- Clase principal que coordina todo
- Maneja los estados de la máquina
- Ejecuta las operaciones matemáticas

## Operaciones Implementadas

1. **Suma**: `3 + 5 = 8`
2. **Resta**: `10 - 4 = 6`
3. **Multiplicación**: `7 * 6 = 42`
4. **División**: `20 / 4 = 5`
5. **Potenciación**: `2^3 = 8`
6. **Raíz cuadrada**: `√16 = 4`

## Uso

```bash
python main.py
```

## Ejemplo de Uso

```python
from maquina_turing import MaquinaTuring

# Crear máquina
tm = MaquinaTuring()

# Realizar operaciones
resultado = tm.sumar(3, 5)  # 8
resultado = tm.restar(10, 4)  # 6
resultado = tm.multiplicar(7, 6)  # 42
```

## Características

- ✅ Implementación simple y clara
- ✅ Separación de responsabilidades en clases
- ✅ Operaciones matemáticas básicas
- ✅ Manejo de errores (división por cero, etc.)
- ✅ Visualización del estado de la cinta