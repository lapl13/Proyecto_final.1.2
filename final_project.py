import turtle
import random


# definir funciones para poder dibujar la cuadricula

def cuadrado_1(color):  # dibuja los cuadrados
    turtle.color(color)
    turtle.fillcolor(color)
    turtle.begin_fill()
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(100)
    turtle.left(90)
    turtle.end_fill()


def preparacion():  # se regresa a la posicion inicial en el renglon siguiente
    turtle.right(180)
    turtle.forward(300)
    turtle.left(90)
    turtle.forward(100)
    turtle.left(90)


# listas de colores para los diferentes niveles
colors_1 = ["red", "green", "blue", "orange", "purple", "pink", "yellow", "cyan", "brown"]
colors_2 = ["red", "green", "blue", "orange", "purple", "pink", "yellow", "cyan", "brown", "black", "olive", "gold"]
colors_3 = ["red", "green", "blue", "orange", "purple", "pink", "yellow", "cyan", "brown", "black", "olive", "gold",
            "teal", "grey", "aqua", "honeydew", "tomato", "tan", "lime", "lavender"]

# comentarios
comentario_inicial = """
    A continuacion se te presentaran colores en una cuadricula
    fijate en que posicion queda cada color
    al final se te preguntara la posicion del color
    cada acierto sumara 10 puntos
    los colores estaran en las posiciones 
    1  2  3
    4  5  6
    7  8  9
    ya que hayas terminado de leer las instrucciones da <enter>

    """
comentario_2 = """
                Observa las posiciones
                cuando estes seguro de haber memorizado los colores y donde se encuentran
                da <enter>
                """
# Programa principal
num = 0

print(comentario_inicial)

listo = str(input())

if listo == "":  # se comienza a dibujar la cuadricula cuando den enter y pongan el nivel

    print("Que nivel de memoria tienes?")  # mayor nivel son mas colores

    num = int(input())

    if num == 1:

        print(colors_1)

        for first in range(3):
            color = random.choice(colors_1)
            cuadrado_1(color)
            turtle.forward(100)

        preparacion()

        for second in range(3):
            color = random.choice(colors_1)
            cuadrado_1(color)
            turtle.forward(100)

        preparacion()

        for third in range(3):
            color = random.choice(colors_1)
            cuadrado_1(color)
            turtle.forward(100)

        print(comentario_2)

        listo = str(input())
        if listo == "":
            color = "black"
            turtle.color(color)
            turtle.fillcolor(color)
            turtle.begin_fill()
            turtle.left(90)
            turtle.forward(300)
            turtle.left(90)
            turtle.forward(300)
            turtle.left(90)
            turtle.forward(300)
            turtle.left(90)
            turtle.forward(300)
            turtle.end_fill()

        print("""Recuerda, el orden de las posiciones es:
                    1  2  3
                    4  5  6
                    7  8  9""")

        for i in range(9):

            print("Color del cuadro?")
            cuadro = str(input())

            if cuadro == cuadro_1[colors_1]:
                print("Acertaste")
            else:
                print("Error")

    elif num == 2:

        print(colors_2)

        for first in range(3):
            color = random.choice(colors_2)
            cuadrado_1(color)
            turtle.forward(100)

        preparacion()

        for second in range(3):
            color = random.choice(colors_2)
            cuadrado_1(color)
            turtle.forward(100)

        preparacion()

        for third in range(3):
            color = random.choice(colors_2)
            cuadrado_1(color)
            turtle.forward(100)

        print(comentario_2)

        listo = str(input())
        if listo == "":
            color = "black"
            turtle.color(color)
            turtle.fillcolor(color)
            turtle.begin_fill()
            turtle.left(90)
            turtle.forward(300)
            turtle.left(90)
            turtle.forward(300)
            turtle.left(90)
            turtle.forward(300)
            turtle.left(90)
            turtle.forward(300)
            turtle.end_fill()

        print("""Recuerda, el orden de las posiciones es:
                1  2  3
                4  5  6
                7  8  9""")

        for i in range(9):

            print("Color del cuadro?")
            cuadro = str(input())

            if cuadro == cuadro_1[colors_2]:
                print("Acertaste")
            else:
                print("Error")


    elif num == 3:

        print(colors_3)

        for first in range(3):
            color = random.choice(colors_3)
            cuadrado_1(color)
            turtle.forward(100)

        preparacion()

        for second in range(3):
            color = random.choice(colors_3)
            cuadrado_1(color)
            turtle.forward(100)

        preparacion()

        for third in range(3):
            color = random.choice(colors_3)
            cuadrado_1(color)
            turtle.forward(100)

        print(comentario_2)

        listo = str(input())
        if listo == "":
            color = "black"
            turtle.color(color)
            turtle.fillcolor(color)
            turtle.begin_fill()
            turtle.left(90)
            turtle.forward(300)
            turtle.left(90)
            turtle.forward(300)
            turtle.left(90)
            turtle.forward(300)
            turtle.left(90)
            turtle.forward(300)
            turtle.end_fill()

        print("""Recuerda, el orden de las posiciones es:
                1  2  3
                4  5  6
                7  8  9""")

        for i in range(9):

            print("Color del cuadro?")
            cuadro = str(input())

            if cuadro == cuadro_1[colors_3]:
                print("Acertaste")
            else:
                print("Error")


