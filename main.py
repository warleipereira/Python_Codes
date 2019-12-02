import pygame 
  
# activate the pygame library . 
# initiate pygame and give permission 
# to use pygame's functionality. 

#update:01/12/2019 - 22:10h
X = 500
Y = 600
screen = pygame.display.set_mode((X, Y))


class Background(pygame.sprite.Sprite): #Creates space background
    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self)  #call Sprite initializer
        self.bgimage = pygame.image.load(image_file)
        self.bgimage = pygame.transform.scale(self.bgimage, (1333, 600))
        self.rectBGimg = self.bgimage.get_rect()

        self.bgY1 = 0
        self.bgX1 = 0

        self.bgY2 = 0
        self.bgX2 = self.rectBGimg.width

        self.movingUpSpeed = 5

    def move_bg_right(self):
        self.bgX1 -= self.movingUpSpeed
        self.bgX2 -= self.movingUpSpeed
        if self.bgX1 <= -self.rectBGimg.width:
            self.bgX1 = self.rectBGimg.width
        if self.bgX2 <= -self.rectBGimg.width:
            self.bgX2 = self.rectBGimg.width

    def move_bg_left(self):
        self.bgX1 += self.movingUpSpeed
        self.bgX2 += self.movingUpSpeed
        if self.bgX1 <= -self.rectBGimg.width:
            self.bgX1 = self.rectBGimg.width
        if self.bgX2 <= -self.rectBGimg.width:
            self.bgX2 = self.rectBGimg.width           

    def render(self):
        screen.blit(self.bgimage, (self.bgX1, self.bgY1))
        screen.blit(self.bgimage, (self.bgX2, self.bgY2))


class KeyPress():
    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and not prior_key_states[pygame.K_LEFT]:
            print("seta esquerda pressionada")

        if keys[pygame.K_RIGHT] and not prior_key_states[pygame.K_RIGHT]:
            print("seta direita pressionada")



def main():
    pygame.init() 
    
    # define the RGB value 
    # for white colour 
    white = (255, 255, 255) 
    
    # assigning values to X and Y variable 

    
    # create the display surface object 
    # of specific dimension..e(X, Y). 
    display_surface = pygame.display.set_mode((X, Y )) 
    
    # set the pygame window name 
    pygame.display.set_caption('Primeiro Jogo em Python') 
    
    # create a surface object, image is drawn on it. 
    image = pygame.image.load(r'./images/supermario_launch.gif').convert_alpha()
  
    relogio = pygame.time.Clock()



    # set up the window
    

    BackGround = Background(r'./images/img_bg.png', [0,0])

    # infinite loop 
    while True : 
    
        # set color 

    
        # instrução para identificar a saida do game
        for event in pygame.event.get() : 
            if event.type == pygame.QUIT : 
                pygame.quit() 
                print("usuário saiu do game")
                quit() 
    
            relogio.tick(60)
            # update da tela
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT]:
                print("seta esquerda pressionada")                
                BackGround.move_bg_left()

            if keys[pygame.K_RIGHT]:
                print("seta direita pressionada")
                BackGround.move_bg_right()
            
            BackGround.render()
            pygame.display.flip()
            pygame.display.update()




main()           