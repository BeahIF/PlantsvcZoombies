from graphics import *
from time import *
from ervilhas import *
class Pokemon():
    def __init__(self,id,img, tipo, vida, dano,y) :
        self.id = id
        self.img = img
        self.tipo =  tipo
        self.vida = vida
        self.dano = dano
        self.position = Point(620,y)
        self.image = None
        
    def anda(self,win):
        print("DESENHA OS FRAME")
      
        #a = 5 #valor que anda no x
        #image = Image(Point(255, 255), str(1)+".gif")
   #     p = Point(620+a,y)        
  #      image =  Image(p, "charizard.gif")
 #       image.draw(win)
#        acha=False
      #  while(acha==False):

        i = 1
      #  while(i < 39):#arrumar esse valor para ele andar ate achar uma flor
        self.image.undraw()
            #i = i + 1
        #a = a -10
        x = 620 -10
       # p = Point(x,y)
        self.position.move(-0.2,0)        
        self.image =  Image(self.position, str(i)+".gif")
         #   image = Image(Point(255+a, 255), str(i)+".gif")
        self.image.draw(win)
     #   morri()
        #sleep(0.15)
        #    acha = achaPokemon()
#                if(620+a == )

  #  def morri():