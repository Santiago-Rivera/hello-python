# Expresiones regulares

import re

texto = "Llama al 555-123-4567 o al soporte 800-999-0000 hoy mismo."

telefonos_encontrados = []
palabras = texto.split()

for palabra in palabras:
    # Limpiamos puntos o comas al final
    palabra_limpia = palabra.replace(".", "").replace(",", "")
    
    # Validamos manualmente si tiene el formato
    partes = palabra_limpia.split("-")
    if len(partes) == 3 and partes[0].isdigit() and partes[1].isdigit() and partes[2].isdigit():
        telefonos_encontrados.append(palabra_limpia)

print(telefonos_encontrados) 
# Resultado: ['555-123-4567', '800-999-0000']

texto = "Llama al 555-123-4567 o al soporte 800-999-0000 hoy mismo."

# El patrón: \d{3} (3 dígitos) seguido de un guión, etc.
patron = r'\d{3}-\d{3}-\d{4}'

telefonos_encontrados = re.findall(patron, texto)

print(telefonos_encontrados) 
# Resultado: ['555-123-4567', '800-999-0000']

registro_log = "El usuario pagó con la tarjeta 4532-1111-2222-9876 a las 10 AM."

# Buscamos bloques de 4 dígitos repetidos 3 veces seguidos de un guión
patron_tarjeta = r'\d{4}-\d{4}-\d{4}-'

# Reemplazamos todo ese bloque inicial por asteriscos
texto_seguro = re.sub(patron_tarjeta, '****-****-****-', registro_log)

print(texto_seguro)
# Resultado: El usuario pagó con la tarjeta ****-****-****-9876 a las 10 AM.