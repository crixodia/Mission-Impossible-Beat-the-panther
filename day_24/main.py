import curses
import json
import random

WORDS = json.load(open("words.json"))


def dibujar_menu():
    pantalla.clear()
    pantalla.addstr(0, 0, "Ahorcado")
    pantalla.addstr(2, 2, "1. Jugar")
    pantalla.addstr(3, 2, "2. Salir")
    pantalla.addstr(4, 2, "> ")
    pantalla.refresh()


def dibujar_dificultad():
    pantalla.clear()
    pantalla.addstr(0, 0, "Ahorcado")
    pantalla.addstr(2, 2, "1. Fácil")
    pantalla.addstr(3, 2, "2. Medio")
    pantalla.addstr(4, 2, "3. Difícil")
    pantalla.addstr(5, 2, "> ")
    pantalla.refresh()


def dibujar_ganar():
    pantalla.addstr(10, 0, "¡Ganaste!")
    pantalla.addstr(11, 2, "1. Jugar de nuevo")
    pantalla.addstr(12, 2, "2. Salir")
    pantalla.addstr(13, 2, "> ")


def dibujar_perder():
    pantalla.addstr(10, 0, "¡Perdiste!")
    pantalla.addstr(11, 2, "1. Jugar de nuevo")
    pantalla.addstr(12, 2, "2. Salir")
    pantalla.addstr(13, 2, "> ")


def dibujar_ahorcado(intentos, word_mask):
    pantalla.clear()

    # Dibujar la horca
    pantalla.addstr(0, 0, "Ahorcado")
    pantalla.addstr(2, 2, " +---+")
    pantalla.addstr(3, 2, " |   |")
    pantalla.addstr(4, 2, "     |")
    pantalla.addstr(5, 2, "     |")
    pantalla.addstr(6, 2, "     |")
    pantalla.addstr(7, 2, "     |")
    pantalla.addstr(8, 2, "     |")
    pantalla.addstr(9, 2, "=========")

    if intentos == 6:
        pantalla.addstr(4, 3, "O")
    elif intentos == 5:
        pantalla.addstr(4, 3, "O")
        pantalla.addstr(5, 3, "|")
    elif intentos == 4:
        pantalla.addstr(4, 3, "O")
        pantalla.addstr(5, 3, "|")
        pantalla.addstr(5, 2, "/")
    elif intentos == 3:
        pantalla.addstr(4, 3, "O")
        pantalla.addstr(5, 3, "|")
        pantalla.addstr(5, 2, "/")
        pantalla.addstr(5, 4, "\\")
    elif intentos == 2:
        pantalla.addstr(4, 3, "O")
        pantalla.addstr(5, 3, "|")
        pantalla.addstr(5, 2, "/")
        pantalla.addstr(5, 4, "\\")
        pantalla.addstr(6, 3, "|")
    elif intentos == 1:
        pantalla.addstr(4, 3, "O")
        pantalla.addstr(5, 3, "|")
        pantalla.addstr(5, 2, "/")
        pantalla.addstr(5, 4, "\\")
        pantalla.addstr(6, 3, "|")
        pantalla.addstr(7, 2, "/")
    elif intentos == 0:
        pantalla.addstr(4, 3, "O")
        pantalla.addstr(5, 3, "|")
        pantalla.addstr(5, 2, "/")
        pantalla.addstr(5, 4, "\\")
        pantalla.addstr(6, 3, "|")
        pantalla.addstr(7, 2, "/")
        pantalla.addstr(7, 4, "\\")
    # Dibujar la palabra
    pantalla.addstr(2, 20, "Palabra: ")
    pantalla.addstr(2, 29, " ".join(word_mask))

    # Dibujar los intentos
    pantalla.addstr(4, 20, "Intentos: ")
    pantalla.addstr(4, 30, str(intentos))

    pantalla.addstr(6, 20, "> ")

    pantalla.refresh()


def main():
    # Inicializar la pantalla
    global pantalla
    pantalla = curses.initscr()
    curses.curs_set(1)
    pantalla.keypad(True)
    pantalla.nodelay(True)

    # Dibujar el menú
    dibujar_menu()

    # Esperar a que el usuario presione una tecla
    while True:
        key = int(pantalla.getstr().decode())
        if key == 1:
            dibujar_dificultad()
            dificultad = int(pantalla.getstr().decode())

            dificultades = {
                1: "easy",
                2: "medium",
                3: "hard"
            }

            word_to_guess = random.choice(WORDS[dificultades[dificultad]])
            word_mask = ["_" for _ in word_to_guess]
            # Pista
            letra_pista = random.choice(word_to_guess)
            for i, c in enumerate(word_to_guess):
                if c == letra_pista:
                    word_mask[i] = c

            intentos = 7

            finished = False

            while intentos > 0 and not finished:
                dibujar_ahorcado(intentos, word_mask)
                letra = pantalla.getstr().decode()
                if letra in word_to_guess:
                    for i, c in enumerate(word_to_guess):
                        if c == letra:
                            word_mask[i] = c
                else:
                    intentos -= 1

                dibujar_ahorcado(intentos, word_mask)
                if intentos == 0:
                    dibujar_perder()
                    finished = True

                if "_" not in word_mask:
                    dibujar_ganar()
                    finished = True

        elif key == 2:
            curses.endwin()
            break


if __name__ == "__main__":
    main()
