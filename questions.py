import random
import string

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


letters = string.ascii_lowercase
# devuelve una lista completa de palabras en orden aleatorio.
words = random.sample(words, len(words))

print("¡Bienvenido al Ahorcado!")
print()

for word in words:
    attempts = 6
    guessed = []

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

print("¡Se acabaron todas las palabras! Gracias por jugar.")