import pygame

class Main:

    def settings(self):

        pygame.init()
        self.pyclock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((800,600))
        pygame.display.set_caption('2D Fight')

    def entities(self):

        self.background = pygame.image.load('stuff/background.png').convert_alpha()
        self.player = pygame.image.load('stuff/playerstay.png').convert_alpha()
        self.playerRECTANGLE = self.player.get_rect()


    def cordinates(self):

        self.playerRECTANGLE.x = 350
        self.playerRECTANGLE.y = 350

        self.playerchangeX = 0
        self.playerchangeY = 0

    def main(self): 

          while True:

            for i in pygame.event.get():

                if i.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                if i.type == pygame.KEYDOWN:
                   
                    if i.key == pygame.K_a:
                        self.playerchangeX = -2
                        self.player = pygame.image.load('stuff/walk1.png').convert_alpha()
                        self.player = pygame.image.load('stuff/walk2.png').convert_alpha()

                    if i.key == pygame.K_d: 
                        self.playerchangeX = 2
                        self.player = pygame.image.load('stuff/walk2.png').convert_alpha()

                if i.type == pygame.KEYUP:
                    self.playerchangeX = 0
                    self.playerchangeY = 0
                    self.player = pygame.image.load('stuff/playerstay.png').convert_alpha()


            self.movement()


            self.blit(self.background,(0,0))
            self.blit(self.player,self.playerRECTANGLE)

            
            pygame.display.update()
            self.pyclock.tick(60) 

    def blit(self,x,y):
        self.screen.blit(x,y)

    def movement(self):

        self.playerRECTANGLE.x += self.playerchangeX
        self.playerRECTANGLE.y += self.playerchangeY


if __name__ == '__main__':
    
    game = Main()
    game.settings()
    game.entities()
    game.cordinates()
    game.main()