import random
import string

'''
words = [
    "python",
    "programa",
    "variable",
    "funcion",
    "bucle",
    "cadena",
    "entero",
    "lista",
]
'''

categorias = {
    "conceptos": ["programa", "variable", "funcion", "bucle"],
    "datos": ["cadena", "entero", "lista"],
    "lenguajes": ["python"]
}

letters = string.ascii_lowercase
# word = random.choice(words)
guessed = []
attempts = 6

print("¡Bienvenido al Ahorcado!")
print()
print('ingrese una de las siguentes categorias')
print(f'{categorias.keys()}')
categoria = input('ingrese el nombre de una categoria si lo desea sino ingrese -1')
if categoria != '-1':
    word = random.choice(categorias[categoria])
else:
    lista_palabras = random.choice(list(categorias.values()))
    word = random.choice(lista_palabras)

while attempts > 0:
    # Mostrar progreso: letras adivinadas y guiones para las que faltan
    progress = ""
    for letter in word:
        if letter in guessed:
            progress += letter + " "
        else:
            progress += "_ "

    print(progress)

    # Verificar si el jugador ya adivinó la palabra completa
    if "_" not in progress:
        print(f"¡Ganaste! Obtuviste un total de {attempts} puntos")
        break

    print(f"Intentos restantes: {attempts}")
    print(f"Letras usadas: {', '.join(guessed)}")

    letter = input("Ingresá una letra: ").lower()

    # Si no es una letra o si posee mas de un caracter se considera invalido
    if ( (not letter in letters) or (len(letter) > 1)):
        print('Entrada no válida')
        continue

    if letter in guessed:
        print("Ya usaste esa letra.")
    elif letter in word:
        guessed.append(letter)
        print("¡Bien! Esa letra está en la palabra.")
    else:
        guessed.append(letter)
        attempts -= 1
        print("Esa letra no está en la palabra.")

    print()

else:
    print(f"¡Perdiste! La palabra era: {word} obtuviste un total de {attempts}")