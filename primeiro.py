from graphics import *
from time import *
from datetime import datetime
from ervilhas import *
from pokemon import *
from random import *

vetSol = 0
matrizPokemons = []
global matrizPokemons 
matrizErvilhas = []
global matrizErvilhas 
matrizPokemons = [[],[],[],[],[]]
matrizPlantas = [[],[],[],[],[]]
global matrizPlantas

def qualPonto(point):

    x = point.x
    y = point.y
   
    if(x > 30 and x < 150 and y >=80 and y <200):
        return 4
    elif(x > 125 and x < 240 and y >0 and y < 60 ):
        return 1
    else:
        if(x > 230 and x < 340 and y > 140 and y <240):
            return 2
        else:
            return 3
def grid(win):
    t = Text(Point(610, 70), vetSol)
    t.setTextColor("white")
    t.draw(win)
    chao = Image(Point(100,140),"novoChao.gif")
    chao.draw(win)
    chao = Image(Point(200,140), "novoChao.gif")
    chao.draw(win)
    chao = Image(Point(300,140), "novoChao.gif")
    chao.draw(win)
    chao = Image(Point(400,140), "novoChao.gif")
    chao.draw(win)
    chao = Image(Point(500,140), "novoChao.gif")
    chao.draw(win)
    chao = Image(Point(600,140), "novoChao.gif")
    chao.draw(win)
    chao = Image(Point(100,240),"novoChao.gif")
    chao.draw(win)
    chao = Image(Point(200,240), "novoChao.gif")
    chao.draw(win)
    chao = Image(Point(300,240), "novoChao.gif")
    chao.draw(win)
    chao = Image(Point(400,240), "novoChao.gif")
    chao.draw(win)
    chao = Image(Point(500,240), "novoChao.gif")
    chao.draw(win)
    chao = Image(Point(600,240), "novoChao.gif")
    chao.draw(win)
    chao = Image(Point(100,340),"novoChao.gif")
    chao.draw(win)
    chao = Image(Point(200,340), "novoChao.gif")
    chao.draw(win)
    chao = Image(Point(300,340), "novoChao.gif")
    chao.draw(win)
    chao = Image(Point(400,340), "novoChao.gif")
    chao.draw(win)
    chao = Image(Point(500,340), "novoChao.gif")
    chao.draw(win)
    chao = Image(Point(600,340), "novoChao.gif")
    chao.draw(win)
    chao = Image(Point(100,440),"novoChao.gif")
    chao.draw(win)
    chao = Image(Point(200,440), "novoChao.gif")
    chao.draw(win)
    chao = Image(Point(300,440), "novoChao.gif")
    chao.draw(win)
    chao = Image(Point(400,440), "novoChao.gif")
    chao.draw(win)
    chao = Image(Point(500,440), "novoChao.gif")
    chao.draw(win)
    chao = Image(Point(600,440), "novoChao.gif")
    chao.draw(win)
    chao = Image(Point(100,540),"novoChao.gif")
    chao.draw(win)
    chao = Image(Point(200,540), "novoChao.gif")
    chao.draw(win)
    chao = Image(Point(300,540), "novoChao.gif")
    chao.draw(win)
    chao = Image(Point(400,540), "novoChao.gif")
    chao.draw(win)
    chao = Image(Point(500,540), "novoChao.gif")
    chao.draw(win)
    chao = Image(Point(600,540), "novoChao.gif")
    chao.draw(win)
    global wall
    wall = []
    x = 50
    y = 90
    for i in range(5):
        line = []
        matrizErvilhas.append([])
        for j in range(6)  :
            pt1 = Point(0,0)
            pt2 = Point(100,100)
            rec1 = Rectangle(pt1,pt2) 
            rec1.setOutline(color_rgb(0,255,255))
            dx=(j*100) +(50)
            dy=(i*100) + 90
            rec1.move(dx,dy)
            rec1.draw(win)
            line.append(rec1)

        wall.append(line)
    global avaible
    avaible = [[1,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0]]
    return t

def colocaSol(janela, point):
    sol = Image(point, "sun.gif")
    sol.draw(janela)
    print(sol)
    return sol

def gridSuperior(win):
    #Plantas
    ervilha = Image(Point(140, 40), "pcard.gif")
    ervilha.draw(win)
    #Fazer mais plantas


def colocaPokemon(win):
    i =   randint(0,4)
    if(i == 0):
        pokemon = Pokemon(1,"c/1.gif",1,100,100,140+(i*100))
        matrizPokemons[0].append(pokemon)
    elif(i==1):
        pokemon = Pokemon(1,"c/1.gif",1,100,100,140+(i*100))
        matrizPokemons[1].append(pokemon)
    else:
        if(i==2):
            pokemon = Pokemon(1,"c/1.gif",1,100,100,140+(i*100))
            matrizPokemons[2].append(pokemon)
        elif(i==3):
            pokemon = Pokemon(1,"c/1.gif",1,100,100,140+(i*100))
            matrizPokemons[3].append(pokemon)
        else: 
            pokemon = Pokemon(1,"c/1.gif",1,100,100,140+(i*100))
            matrizPokemons[4].append(pokemon)
    p = Point(620,140+(i*100))        
    image =  Image(p, "c/1.gif")
    image.draw(win)
    pokemon.image = image

def inicio(win):
    global vetSol
    win.setBackground(color_rgb(0,0,0))
    t = grid(win)
    gridSuperior(win)
    flower =  Image(Point(100,120),"s15.gif")
    flower.draw(win)
    point= Point(50,100)
    #sol = colocaSol(win, point) 
    now = datetime.now()
    c = 0
    d= 0
    framerate = 1/30
    while(True):
        init = time()    
        c = c + framerate
        d = d  + framerate 
        if c > 10:
            point= Point(50,100)
            colocaPokemon(win)
            c = 0
        if d > 15:
            point = Point(50,100)
            sol = colocaSol(win, point)
        point = win.checkMouse() # pause for click in window
        if point != None:
            posicaoSol = [25,75, 75, 115]
            if qualPonto(point) == 1 :   
                qualPlanta = qualPonto(point) 
                planta = Planta()
                i = planta.colocaPlanta(qualPlanta, win,wall,avaible, vetSol, matrizErvilhas)
                if i:
                    matrizPlantas[i].append(planta)
                #print("here")
                vetSol = vetSol - 100
                #print(vetSol)
                t.undraw()
                t = Text(Point(610, 70), vetSol)
                t.setTextColor("white")
                t.draw(win)
            
            if qualPonto(point) == 2 :    
                qualPlanta = qualPonto(point) 
                #print("aqui")
                planta = Planta()
                planta.colocaPlanta(qualPlanta, win,wall,avaible, vetSol, matrizErvilhas)
                #print("matriz ervilha")
                #print(matrizErvilhas)
            if qualPonto(point) == 4 :   
                sol.undraw()
                #print(sol)
                #print("aqui")
                vetSol = vetSol +100
                t.undraw()
                t = Text(Point(610, 70), vetSol)
                t.setTextColor("white")
                t.draw(win)
                print(vetSol)
                
            
        for i,linha in enumerate(matrizPokemons) :
            for pokemon in linha:
                pokemon.image.move(-20*framerate,0)
                if pokemon.image.getAnchor().x < 10:
                    final = Image(Point(340,340), "final2.gif")
                    final.draw(win)
        for i,linha in enumerate(matrizErvilhas) :
            for ervilha in linha:
                ervilha.move(20*framerate,0)
                if len(matrizPokemons[i]) > 0:                   
                    if ervilha.getAnchor().x > matrizPokemons[i][0].image.getAnchor().x-20:
                        ervilha.undraw()
                        matrizPokemons[i][0].image.undraw()
                        matrizPokemons[i].pop(0)
                        matrizErvilhas[i].remove(ervilha)
        for   i,linha in enumerate(matrizPlantas):
            for planta in linha:
                planta.contador += framerate
                if planta.contador > planta.limit:
                    planta.dispara(planta.p, win, matrizErvilhas, i)
                    planta.contador = 0
        framerate = time() - init
    win.close()
def main():
    win = GraphWin("Plantas vs. Pokemons", 700, 590)
    win.setBackground(color_rgb(0,0,0))
    p = Point(350,325)
    c = Point(350,500)
    image = Image(p,"inicio4.gif") 
    image.draw(win)
    play = Image(c,"Play.gif")
    play.draw(win)
    while True: 
        p = win.getMouse()
        x=p.x
        y=p.y
        if (x>350 and x<450 and y>350 and y<650 ):
            image.undraw()
            play.undraw()
            inicio(win)
main()



  
  