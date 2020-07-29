import pygame
import cocos
import pyglet
import arcade
from pyglet import image
from pyglet.window import key
from collections import defaultdict
from cocos.layer import *
from cocos.director import director
from cocos.sprite import Sprite
from cocos.actions import * 
import cocos.collision_model as cm 
import cocos.euclid as eu 
from cocos.actions import MoveTo, Repeat

class Actor(cocos.sprite.Sprite) :
    def __init__(self, imagen, x, y) :
        super().__init__(image.load(imagen))
        self.position = (x, y)
        self.velocidad = 100.0
        self.teclas_pulsadas = defaultdict(int) 
        self.schedule(self.update) 
        
        
        

    def on_key_press(self, k, m) :
        self.teclas_pulsadas[k] = 1
    def on_key_release(self, k, m) :
        self.teclas_pulsadas[k] = 0 

 
    def update(self, dt) :
        '''
        self.coll_manager.clear()
        for _, node in self.children:
            self.coll_manager.add(node)
        for other in self.coll_manager.iter_colliding(self.mi_actor):
            self.remove(other)
        '''      
        x = self.teclas_pulsadas[key.RIGHT] - self.teclas_pulsadas[key.LEFT]
        y = self.teclas_pulsadas[key.UP] - self.teclas_pulsadas[key.DOWN]
        z = self.teclas_pulsadas[key.SPACE] + Chamas.Move((50,10), 8)
        
        if x != 0 or y != 0:
            posicion = self.mi_actor.position
            nueva_x = posicion[0] + self.velocidad * x * dt * 2
            nueva_y = posicion[1] + self.velocidad * y * dt * 2
            self.mi_actor.position = (nueva_x, nueva_y)

  


class MiCapa(cocos.layer.Layer) :
    is_event_handler = True 
    def __init__(self) :
        super().__init__()
        
        jogobg = Sprite('Jogo.png', (320,240)) 
        self.add(jogobg)    
        self.mi_actor = Actor('C:\Istec\Projeto_py\player.png', 100, 90)
        self.mi_inimigo = Inimigo_('C:\Istec\Projeto_py\inimigo.png', 500, 100)
        self.mi_chamas = Chamas ('C:\Istec\Projeto_py\chamas.png',320, 100) 
        self.mi_chamas_p2 = Chamas_p2 ('C:\Istec\Projeto_py\chamas2.png',500,100)
        self.mi_chamas = False
        self.mi_chamas_p2 = False
        self.add(self.mi_chamas)
        self.add(self.mi_chamas_p2)
        self.add(self.mi_actor)
        self.add(self.mi_inimigo)

        self.velocidad = 100.0
        self.teclas_pulsadas = defaultdict(int)
        self.schedule(self.update)  
        
  
        
        
    def on_key_press(self, k, m) :
        self.teclas_pulsadas[k] = 1
    def on_key_release(self, k, m) :
        self.teclas_pulsadas[k] = 0 

    def update(self, dt) :
      
        '''
        self.mi_actor.update(self,dt)
        self.mi_inimigo.update(self,dt) 

        '''
        
        x = self.teclas_pulsadas[key.RIGHT] - self.teclas_pulsadas[key.LEFT]
        y = self.teclas_pulsadas[key.UP] - self.teclas_pulsadas[key.DOWN]
        
        
        '''
        if x != 0 or y != 0:
            posicion = self.mi_actor.position
            nueva_x = posicion[0] + self.velocidad * x * dt * 2
            nueva_y = posicion[1] + self.velocidad * y * dt * 2
            self.mi_actor.position = (nueva_x, nueva_y)
        ''' 
        if self.teclas_pulsadas[key.RIGHT]>0 or self.teclas_pulsadas[key.LEFT]>0 or self.teclas_pulsadas[key.UP]>0 or self.teclas_pulsadas[key.DOWN]>0:

            x = self.teclas_pulsadas[key.RIGHT] - self.teclas_pulsadas[key.LEFT]
            y = self.teclas_pulsadas[key.UP] - self.teclas_pulsadas[key.DOWN]
            z = self.teclas_pulsadas[key.SPACE] + Chamas.Move((50,10), 8)
            
            if x != 0 or y != 0:
                posicion = self.mi_actor.position
                nueva_x = posicion[0] + self.velocidad * x * dt * 2
                nueva_y = posicion[1] + self.velocidad * y * dt * 2
                self.mi_actor.position = (nueva_x, nueva_y)
            
             

        if self.teclas_pulsadas[key.D]>0 or self.teclas_pulsadas[key.A]>0 or self.teclas_pulsadas[key.W]>0 or self.teclas_pulsadas[key.S]>0:

            x = self.teclas_pulsadas[key.D] - self.teclas_pulsadas[key.A]
            y = self.teclas_pulsadas[key.W] - self.teclas_pulsadas[key.S]
            z = self.teclas_pulsadas[key.E] + Chamas_p2.Move((50,10), 8)
            if x != 0 or y != 0: 
                posicion = self.mi_inimigo.position
                nueva_x = posicion[0] + self.velocidad * x * dt * 2
                nueva_y = posicion[1] + self.velocidad * y * dt * 2 
                self.mi_inimigo.position = (nueva_x, nueva_y)

            
        
     

        
class Inimigo_(cocos.sprite.Sprite): 
    def __init__(self, imagen, x, y) :
        super().__init__(image.load(imagen))
        self.position = (x, y)
        self.scale = 0.8
        self.position = (x, y)
        self.velocidad = 100.0
        self.teclas_pulsadas = defaultdict(int)
        self.schedule(self.update) 

        
        

    def on_key_press(self, k, m) :
        self.teclas_pulsadas[k] = 1
    def on_key_release(self, k, m) :
        self.teclas_pulsadas[k] = 0 

    def update(self, dt) :

        x = self.teclas_pulsadas[key.D] - self.teclas_pulsadas[key.W]
        y = self.teclas_pulsadas[key.W] - self.teclas_pulsadas[key.S]
        z = self.teclas_pulsadas[key.E] + Chamas_p2.Move((50,10), 8)
        
        if x != 0 or y != 0:
            posicion = self.mi_inimigo.position
            nueva_x = posicion[0] + self.velocidad * x * dt * 2
            nueva_y = posicion[1] + self.velocidad * y * dt * 2
            self.mi_inimigo.position = (nueva_x, nueva_y)
        '''
        self.coll_manager.clear()
        for _, node in self.children:
            self.manejador_colision.add(node)
        for other in self.coll_manager.iter_colliding(self.mi_actor):
            self.remove(other) 
        '''
class Chamas (cocos.sprite.Sprite): 
    def __init__(self, imagen, x, y) :
        super().__init__(image.load(imagen)) 
        self.position = (x, y)
        self.scale = 0.8

  

class Chamas_p2 (cocos.sprite.Sprite): 
    def __init__(self, imagen, x, y) :
        super().__init__(image.load(imagen)) 
        self.position = (x, y)
        self.scale = 0.8

if __name__ == '__main__':
    cocos.director.director.init(caption='The Lost Guy')
    
    mi_escena = cocos.scene.Scene(MiCapa())
    '''
    mi_escena.schedule_interval(mi_escena.update, 1/60)
    '''
    cocos.director.director.run(mi_escena)
    
