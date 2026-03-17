import random

categorias = {
  "programacion": ["python", "variable", "funcion", "bucle"],
  "objetos": ["mesa", "silla", "puerta", "ventana"],
  "animales": ["perro", "gato", "elefante", "tigre"]
}

print("categorias disponibles: ")
for c in categorias: 
    print("-",c)

categoria = input("elija una categoría: ")

while categoria not in categorias:
  print("Categoría no válida")
  categoria = input("elija una categoría: ")

word = random.choice(categorias[categoria])
guessed = []
attempts = 6
score = 0

print("¡Bienvenido al Ahorcado!")
print()

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
    score += 6
    print("¡Ganaste!. Con puntaje: ",score)
    break
    
  print(f"Intentos restantes: {attempts}")
  print(f"Letras usadas: {', '.join(guessed)}")
  
  letter = input("Ingresá una letra: ")
  if len(letter) != 1 or not letter.isalpha(): #checkea que sea una sola letra
      print("Entrada no valida")
      print()
      continue
  
  if letter in guessed:
    print("Ya usaste esa letra.")
  elif letter in word:
    guessed.append(letter)
    print("¡Bien! Esa letra está en la palabra.")
  else:
    guessed.append(letter)
    attempts -= 1
    score -= 1
    print("Esa letra no está en la palabra.")
    
  print()
  
else:
  score = 0
  print(f"¡Perdiste! La palabra era: {word}. Tu puntaje es: {score}")
  
