# Vamos a presentarnos y pedirle aun cliente que nos diga un texto
texto = input("Por favor escriba un texto:")
letras = input("Por favor digame 3 letras: ")

letra_a = texto.count("a")
letra_e = texto.count("e")
letra_i = texto.count("i")

print(f"El texto tiene {letra_a} letras 'a', {letra_e} letras 'e', {letra_i} letras 'i'")

num_palabras = len(texto.split())
print("El numero de palabras en tu texto es:",num_palabras )

primera_letra = texto[0]
ultima_letra = texto [39]

print("La primera letra de tu texto es:", {primera_letra},"la ultima letra de tu texto es:",{ultima_letra})

texto_invertido = texto[::-1]
print(texto_invertido)

palabra = "pyhton"
if palabra in texto:
    print("La palabra '{}' esta en el texto" .format(palabra))
else:
     print("La palabras '{}' no esta en el texto".format(palabra))


