import random

# Preguntas para el juego
questions = [
"¿Qué función se usa para obtener la longitud de una cadena en Python?",
"¿Cuál de las siguientes opciones es un número entero en Python?",
"¿Cómo se solicita entrada del usuario en Python?",
"¿Cuál de las siguientes expresiones es un comentario válido en Python?",
"¿Cuál es el operador de comparación para verificar si dos valores son iguales?",
]
# Respuestas posibles para cada pregunta, en el mismo orden que las preguntas
answers = [
("size()", "len()", "length()", "count()"),
("3.14", "'42'", "10", "True"),
("input()", "scan()", "read()", "ask()"),
(
"// Esto es un comentario",
"/* Esto es un comentario */",
"-- Esto es un comentario",
"# Esto es un comentario",
),
("=", "==", "!=", "==="),
]
# Índice de la respuesta correcta para cada pregunta, el el mismo orden que las preguntas
correct_answers_index = [1, 2, 0, 3, 1]

TotalPreguntas = 0
valido = True
puntuacion = 0

#se crea una lista de tuplas con 'preguntas, respuestas y respuesta correcta' con repeticion
questions_to_ask = random.choices(list(zip(questions,
answers, correct_answers_index)), k=3)

# El usuario deberá contestar 3 preguntas
for pregunta, respuestas, respuesta_correcta in questions_to_ask : 
     if (not valido) :
         break
     # Se muestra la pregunta
     print(pregunta)
     # Se muestra las respuestas posibles
     for i, answer in enumerate(respuestas):
         print(f"{i + 1}. {answer}")
     # El usuario tiene 2 intentos para responder correctamente
     for intento in range(2):
         user_answer = int(input("Respuesta: ")) - 1
         if (user_answer < 0 or user_answer > 4 ) :
             print("respuesta no valida")
             valido = False
             #puntuacion -= 0.5
             break
         # Se verifica si la respuesta es correcta
         if user_answer == respuesta_correcta:
             print("¡Correcto!")
             puntuacion += 1
             break
         else:
             # Si el usuario no responde correctamente después de 2 intentos,
             # se muestra la respuesta correcta
             print("Incorrecto. La respuesta correcta es:")
             print(f'{respuesta_correcta}')
             puntuacion -= 0.5
     # Se imprime un blanco al final de la pregunta
     print()
print(f'Puntacion total : {puntuacion}')