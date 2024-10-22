# operacion.py
from aritmetica import sumar, restar

def main():
    a = 10
    b = 5

    suma = sumar(a, b)
    resta = restar(a, b)

    print(f"La suma de {a} y {b} es: {suma}")
    print(f"La resta de {a} y {b} es: {resta}")

if __name__ == "__main__":
    main()