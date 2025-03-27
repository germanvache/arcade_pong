"""Juego de Arcade Pong
Reproduce el clásico juego de arcade Pong. Para ello puedes usar el módulo "turtle" para
crear los componentes del juego y detectar las colisiones de la pelota con las paletas de los
jugadores.También puedes definir una serie de asignaciones de teclas para establecer los
controles del usuario para las paletas de los jugadores izquierda y derecha. (cg)
"""
# --- Primero importamos el modulo turtle ---
import turtle 

# 1 --- Configuracion de la ventana de juego ---
wn = turtle.Screen()
wn.title("Pong")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)  # Desactiva el refresco automático de la pantalla

# 2 --- Creamos dos paletas, una para el jugador izquierdo y otra para el jugador derecho ---
# Paleta izquierda
paddle_left = turtle.Turtle()
paddle_left.speed(0)
paddle_left.shape("square")
paddle_left.color("white")
paddle_left.shapesize(stretch_wid=6, stretch_len=1)  # Tamaño de la paleta
paddle_left.penup()
paddle_left.goto(-350, 0)

# Paleta derecha
paddle_right = turtle.Turtle()
paddle_right.speed(0)
paddle_right.shape("square")
paddle_right.color("white")
paddle_right.shapesize(stretch_wid=6, stretch_len=1)  # Tamaño de la paleta
paddle_right.penup()
paddle_right.goto(350, 0)

# 3 --- Creamos la pelota que se moverá en el juego ---
# Pelota
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.15  # Velocidad en el eje x
ball.dy = -0.15  # Velocidad en el eje y

# 4 --- Definimos funciones para mover las paletas y asignamos teclas para los controles ---
def paddle_left_up():
    y = paddle_left.ycor()
    if y < 250:
        y += 20
        paddle_left.sety(y)

def paddle_left_down():
    y = paddle_left.ycor()
    if y > -240:
        y -= 20
        paddle_left.sety(y)

def paddle_right_up():
    y = paddle_right.ycor()
    if y < 250:
        y += 20
        paddle_right.sety(y)

def paddle_right_down():
    y = paddle_right.ycor()
    if y > -240:
        y -= 20
        paddle_right.sety(y)

# Asignar teclas
wn.listen()
wn.onkeypress(paddle_left_up, "w")        # tecla w
wn.onkeypress(paddle_left_down, "s")      # tecla s
wn.onkeypress(paddle_right_up, "Up")      # tecla up
wn.onkeypress(paddle_right_down, "Down")  # tecla down


# 5 --- Implementamos la lógica para mover la pelota y detectar colisiones con las paletas y los bordes de la ventana ---
while True:
    wn.update()

    # Mover la pelota
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Bordes de la ventana
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1

    # Colisiones con las paletas
    if (ball.dx > 0) and (350 > ball.xcor() > 340) and (paddle_right.ycor() + 50 > ball.ycor() > paddle_right.ycor() - 50):
        ball.setx(340)
        ball.dx *= -1

    if (ball.dx < 0) and (-350 < ball.xcor() < -340) and (paddle_left.ycor() + 50 > ball.ycor() > paddle_left.ycor() - 50):
        ball.setx(-340)
        ball.dx *= -1

"""
El código desarrollado establece una ventana de juego usando turtle, 
dibuja las paletas y la pelota, maneja los controles del teclado y contiene la 
lógica básica para mover la pelota y detectar colisiones. 
Se puede ejecutar este código en tu entorno Python para probar el Juego de Arcade Pong
"""





