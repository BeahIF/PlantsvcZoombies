from graphics import *
from time import *
from pokemon import *
import pygame, random, sys, time
from pygame.locals import *
class Planta():       
    def __init__ (self):
        self.contador = 0
        self.limit = 15
     #   self.img = img
      #  self.tipo =  tipo
       # self.vida = vida
        #self.dano = dano
    
  #  def achaPokemon(win):
    
    def dispara(self, p,win, matrizErvilhas,i):     
        x = p.x +10   
        y = p.y -10
        p = Point(x, y)
        ervilha = Image(p, "pea.gif")
        ervilha.draw(win)
        matrizErvilhas[i].append(ervilha)

        
       

    def colocaPlanta(planta, qualPlanta, win,wall,avaible, vetSol, matrizErvilhas):
        print("dentro do coloca planta")
        print(qualPlanta)
        #Esse if verifica qual eh a flor selecionada
        #Ainda falta verificar se a pessoa tem sol suficiente para essa planta
       # if(point.x < 180 and point.x > 100 and point.y > 10 and point.y < 70):
        if(qualPlanta == 1):
            print("vetSol")
            print(vetSol)
            if(vetSol >= 10):
                
                print("vetSol agora")
                print(vetSol)
                p = win.getMouse()
                x = p.x
                print(x)
                y = p.y
                print(y)
                for i, linha in enumerate(wall):
                    for j, retangulo in enumerate(linha):
                        p1 = retangulo.getP1()
                        p2 = retangulo.getP2()
                        if p1.x < x < p2.x and p1.y < y < p2.y:
                            if(avaible[j][i] == 0):
                                avaible[i][j] = 1
                                print(avaible)
                                p = retangulo.getCenter()
                                planta.p=p
                                flor = Image(p, "p1.gif")
                                flor.draw(win)
                                planta.dispara(p,win,matrizErvilhas,i)
                                return i
                            else:
                                return False
        elif(qualPlanta == 2):
        #(point.x < 280 and point.x > 200 and point.y > 10 and point.y < 70):
            if(vetSol >= 10):
                vetSol = vetSol -20
                p = win.getMouse()
                x = p.x
                print(x)
                y = p.y
                print(y)
                for i, linha in enumerate(wall):
                    for j, retangulo in enumerate(linha):
                        p1 = retangulo.getP1()
                        p2 = retangulo.getP2()
                        if p1.x < x < p2.x and p1.y < y < p2.y:
                            if(avaible[j][i] == 0):
                                avaible[i][j] == 1
                                p = retangulo.getCenter()
                                flor = Image(p, "flower.gif")
                                flor.draw(win)

                                return True
                            else:
                                return False
        # else:
        #     if(point.x < 380 and point.x >/ 300 and point.y > 10 and point.y < 70):
        #         if(vetSol >= 30):
        #             vetSol = vetSol -30
        #             p = win.getMouse()
        #             x = p.x
        #             print(x)
        #             y = p.y
        #             print(y)
        #             for i, linha in enumerate(wall):
        #                 for j, retangulo in enumerate(linha):
        #                     p1 = retangulo.getP1()
        #                     p2 = retangulo.getP2()
        #                     if p1.x < x < p2.x and p1.y < y < p2.y:
        #                         if(avaible[j][i] == 0):
        #                             avaible[i][j] = 1
        #                             print(avaible)
        #                             p = retangulo.getCenter()
        #                             flor = Image(p, "p1.gif")
        #                             flor.draw(win)
        #                             return True
        #                         else:
        #                             return False
    


    def achaPokemon(win):
        i = 0
        j = 0
        while(i < 5):
            while(j < 6):
                if(matrizPokemons[i] == 1):
                    if(avaible[i][j] == 1):
                        dispara(win,wall[i][j]) 
                j = j+1
            i = i+1