# Definir el valor de pi con 6 decimales
pi = 3.141593

# Función para calcular la circunferencia
def calcular_circunferencia(radio):
    return 2 * pi * radio

# Solicitar al usuario que ingrese el valor del radio
radio_usuario = float(input("Ingresa el valor del radio: "))

# Calcular la circunferencia con el radio proporcionado por el usuario
circunferencia = calcular_circunferencia(radio_usuario)

# Imprimir el resultado
print(f"La circunferencia con radio {radio_usuario} es: {circunferencia:.6f}")
