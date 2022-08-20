import pygame

class SpaceInvader:

    def init(self):

        pygame.init()

        self.pyclock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((850,600))
        pygame.display.set_caption('Space Invaders')


    def main(self):

        self.background = pygame.image.load('stuff/background.jpg').convert_alpha()

        self.player = pygame.image.load('stuff/player.png').convert_alpha()
        self.playerRECTANGLE = self.player.get_rect()

    def main_loop(self):

        self.playerRECTANGLE.y = 500
        self.playerRECTANGLE.x = 400 

        XuniformlyXplayer= 0
        YuniformlyYplayer= 0
        
        while True:

            for ewent in pygame.event.get():

                if ewent.type == pygame.QUIT:
                    exit()
                if ewent.type == pygame.KEYDOWN:
                    
                    if ewent.key == pygame.K_w:
                        pass

                    if ewent.key == pygame.K_s:
                        pass     

                    if ewent.key == pygame.K_a:
                        XuniformlyXplayer = -2 

                    if ewent.key == pygame.K_d: 
                        XuniformlyXplayer = 2

                if ewent.type == pygame.KEYUP:
                    XuniformlyXplayer = 0

            self.screen.blit(self.background,(0,0)) #background
            self.screen.blit(self.player,(self.playerRECTANGLE.x,self.playerRECTANGLE.y)) #player

            self.playerRECTANGLE.x += XuniformlyXplayer #movement x
            self.playerRECTANGLE.y += YuniformlyYplayer #movement y

            pygame.display.update()
            self.pyclock.tick(60) 
    
    def mobs(self):
        pass

    def bullet(self):
        pass

    def config(self):
        pass


def main():

    game = SpaceInvader()
    game.init()
    game.main()
    game.main_loop()

if __name__ == '__main__':
    
    main()