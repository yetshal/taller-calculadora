"""
Calculadora Básica
Operaciones: suma, resta, multiplicación, división
"""

def suma(a, b):
    """Retorna la suma de dos números"""
    return a + b

def resta(a, b):
    """Retorna la resta de dos números"""
    return a - b

def multiplicacion(a, b):
    """Retorna la multiplicación de dos números"""
    return a * b

def division(a, b):
    """Retorna la división de dos números con manejo de error"""
    if b == 0:
        raise ValueError("Error: No se puede dividir por cero")
    return a / b

def validar_numero(valor):
    """Valida que el valor sea un número válido"""
    try:
        return float(valor)
    except ValueError:
        raise ValueError(f"'{valor}' no es un número válido")

def main():
    """Función principal de la calculadora"""
    print("=== CALCULADORA BÁSICA ===")
    print("Operaciones disponibles:")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    
    try:
        opcion = input("Seleccione operación (1-4): ").strip()
        
        if opcion not in ["1", "2", "3", "4"]:
            print("Error: Opción debe ser 1, 2, 3 o 4")
            return
            
        num1 = validar_numero(input("Ingrese primer número: "))
        num2 = validar_numero(input("Ingrese segundo número: "))
        
        if opcion == "1":
            resultado = suma(num1, num2)
            print(f"Resultado: {num1} + {num2} = {resultado}")
        elif opcion == "2":
            resultado = resta(num1, num2)
            print(f"Resultado: {num1} - {num2} = {resultado}")
        elif opcion == "3":
            resultado = multiplicacion(num1, num2)
            print(f"Resultado: {num1} × {num2} = {resultado}")
        elif opcion == "4":
            resultado = division(num1, num2)
            print(f"Resultado: {num1} ÷ {num2} = {resultado}")
        else:
            print("Opción no válida")
            
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Error inesperado: {e}")

if __name__ == "__main__":
    main()