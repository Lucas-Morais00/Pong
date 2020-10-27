# Lucas Morais Zaroni
#Pong 24/10/2020
#Desenvolvido com o auxilio da playlis https://www.youtube.com/playlist?list=PLlEgNdBJEO-kXk2PyBxhSmo84hsO3HAz2

#Importando os modulos necessarios
import turtle
import winsound
import time
import terminedia as TM

#Definindo a tela do jogo
window = turtle.Screen()
window.title("Pong by @LucasMorais")
window.bgcolor("black")
window.setup(width = 800, height = 600)
window.tracer(0) #Setup p/ atualizar

#Raquete A
raqueteA = turtle.Turtle() #Criar um objeto Turtle
raqueteA.speed(0) #Velocidade de animacao p/ Turtle
raqueteA.shape("square")
raqueteA.color("red")
raqueteA.shapesize(stretch_wid = 5, stretch_len = 1)
raqueteA.penup()
raqueteA.goto(-350, 0) #Posicao inicial

#Raquete B
raqueteB = turtle.Turtle() #Criar um objeto Turtle
raqueteB.speed(0) #Velocidade de animacao p/ Turtle
raqueteB.shape("square")
raqueteB.color("green")
raqueteB.shapesize(stretch_wid = 5, stretch_len = 1)
raqueteB.penup()
raqueteB.goto(350, 0) #Posicao inicial

#Bola
bola = turtle.Turtle() #Criar um objeto Turtle
bola.speed(0) #Velocidade de animacao p/ Turtle
bola.shape("square")
bola.color("white")
bola.penup()
bola.goto(0, 0) #Posicao inicial
bola.dx = 0.2
bola.dy = 0.2

#"Caneta"
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Vermelho: 0   Verde: 0", align = "center", font = ("Courier", 22, "normal"))

#Texto vermelho
penA = turtle.Turtle()
penA.speed(0)
penA.color("red")
penA.penup()
penA.hideturtle()
penA.goto(0, 150)

#Texto verde
penB = turtle.Turtle()
penB.speed(0)
penB.color("green")
penB.penup()
penB.hideturtle()
penB.goto(0, 150)

#Jogar novamente
penC = turtle.Turtle()
penC.speed(0)
penC.color("white")
penC.penup()
penC.hideturtle()
penC.goto(0, 0)

#Pontos
pontoA = 0
pontoB = 0

#Funcao para movimentar as raquetes
def raqueteA_up():
    y = raqueteA.ycor() #Pegar a coordenada Y
    y += 20
    raqueteA.sety(y)

def raqueteA_down():
    y = raqueteA.ycor() #Pegar a coordenada Y
    y -= 20
    raqueteA.sety(y)

def raqueteB_up():
    y = raqueteB.ycor() #Pegar a coordenada Y
    y += 20
    raqueteB.sety(y)

def raqueteB_down():
    y = raqueteB.ycor() #Pegar a coordenada Y
    y -= 20
    raqueteB.sety(y)

#tecla = TM.getch()

#Chamar a funcao pelo teclado
window.listen()
window.onkeypress(raqueteA_up, "w")
window.onkeypress(raqueteA_down, "s")
window.onkeypress(raqueteB_up, "Up")
window.onkeypress(raqueteB_down, "Down")

#Loop principal
while True:
    window.update()

    #Mover a bola
    bola.sety(bola.ycor() + bola.dy)
    bola.setx(bola.xcor() + bola.dx)

    #Bater e quicar no eixo Y
    if bola.ycor() > 290:
        bola.sety(290)
        bola.dy *= -1 #Muda a direcao
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    if bola.ycor() < -290:
        bola.sety(-290)
        bola.dy *= -1 #Muda a direcao
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    #Pontuar no eixo X
    if bola.xcor() > 390:
        bola.goto(0, 0) #Volta p/ o centro
        bola.dx *= -1 #Muda a direcao
        pontoA += 1 #Pontua para o Vermelho
        winsound.PlaySound("coin.wav", winsound.SND_ASYNC)
        pen.clear() #Limpa o texto anterior
        pen.write("Vermelho: {}   Verde: {}".format(pontoA, pontoB), align = "center", font = ("Courier", 22, "normal"))

    if bola.xcor() < -390:
        bola.goto(0, 0) #Volta p/ o centro
        bola.dx *= -1 #Muda a direcao
        pontoB += 1 #Pontua para o verde
        winsound.PlaySound("coin.wav", winsound.SND_ASYNC)
        pen.clear() #Limpa o texto anterior
        pen.write("Vermelho: {}   Verde: {}".format(pontoA, pontoB), align = "center", font = ("Courier", 22, "normal"))

    #Batendo na raquete
    if (bola.xcor() > 340 and bola.xcor() < 350) and (bola.ycor() < raqueteB.ycor() + 40 and bola.ycor() > raqueteB.ycor() - 40):
        bola.setx(340)
        bola.dx *= -1 #Muda a direcao
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    if (bola.xcor() < -340 and bola.xcor() > -350) and (bola.ycor() < raqueteA.ycor() + 40 and bola.ycor() > raqueteA.ycor() - 40):
        bola.setx(-340)
        bola.dx *= -1 #Muda a direcao
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    #Pontuando 
    if pontoA == 3:
        bola.goto(0, 0)
        bola.dx = 0
        bola.dy = 0
        penA.write("Vermelho ganhou!", align = "center", font = ("Courier", 20, "normal"))
        winsound.PlaySound("vic.wav", winsound.SND_FILENAME)
        turtle.exitonclick()

    if pontoB == 3:
        bola.goto(0, 0)
        bola.dx = 0
        bola.dy = 0
        penB.write("Verde ganhou!", align = "center", font = ("Courier", 20, "normal"))
        winsound.PlaySound("vic.wav", winsound.SND_FILENAME)
        turtle.exitonclick()

    #AI
    '''
    if  tecla == 's':
        if raqueteB.ycor() < bola.ycor() and abs(raqueteB.ycor() - bola.ycor()) > 10:
            raqueteB_up()

        elif raqueteB.ycor() > bola.ycor() and abs(raqueteB.ycor() - bola.ycor()) > 10:
            raqueteB_down()
    '''










        

