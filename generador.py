import random

# Función para generar un correo electrónico aleatorio
def generar_correo():
    numeros = "0123456789"
    longitud = 6
    
    # Generar una secuencia de 6 dígitos aleatorios
    numero_aleatorio = "".join(random.sample(numeros, longitud))
    
    # Elegir un prefijo que sea "23" o "22"
    prefijo = random.choice(["23", "22"])
    
    # Concatenar el prefijo y el número aleatorio con el dominio fijo
    correo = f"{prefijo}{numero_aleatorio}@uttt.edu.com"
    
    return correo

# Generar y mostrar un correo electrónico aleatorio
correo_aleatorio = generar_correo()
print(correo_aleatorio)

