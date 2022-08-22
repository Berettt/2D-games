import pygame, random

class SpaceInvader:

    def init(self):

        pygame.init()

        self.enem = 6

        self.pyclock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((850,800))
        pygame.display.set_caption('Space Invaders')


    def main(self):

        self.background = pygame.image.load('stuff/background.jpg').convert_alpha()

        self.player = pygame.image.load('stuff/player.png').convert_alpha()
        self.playerRECTANGLE = self.player.get_rect()

    def mobs(self):
        self.mob = []
        self.mobRECTANGLE = []
        self.randomx = []

        for m in range(self.enem):

            self.mob.append(pygame.image.load('stuff/ufo.png').convert_alpha())
            self.mobRECTANGLE.append(self.mob[m].get_rect())
            self.randomx.append(random.randint(10,840))
            self.mobRECTANGLE[m].x = self.randomx[m]

    def main_loop(self):
        self.fire = False
        MOBMOVEMENT = 2.5

        self.playerRECTANGLE.y = 700
        self.playerRECTANGLE.x = 400 

        self.shotRECTANGLE.y = 700

        XuniformlyXplayer= 0
        YuniformlyYplayer= 0

        while True:

            for ewent in pygame.event.get():

                if ewent.type == pygame.QUIT:
                    exit()
                if ewent.type == pygame.KEYDOWN:

                    if ewent.key == pygame.K_w and ewent.key == pygame.K_a:
                        print('test')
                    
                    if ewent.key == pygame.K_w:
                        YuniformlyYplayer = -3 

                    if ewent.key == pygame.K_s:
                        YuniformlyYplayer = 3     

                    if ewent.key == pygame.K_a:
                        XuniformlyXplayer = -3

                    if ewent.key == pygame.K_d: 
                        XuniformlyXplayer = 3

                if ewent.type == pygame.KEYUP:
                    XuniformlyXplayer = 0
                    YuniformlyYplayer = 0

            self.slayed()

            self.fire_bullet()

            self.screen.blit(self.background,(0,0)) #background
            self.screen.blit(self.player,self.playerRECTANGLE) #player
            for m in range(self.enem):
                self.screen.blit(self.mob[m],self.mobRECTANGLE[m])
                self.mobRECTANGLE[m].y += MOBMOVEMENT
            #self.screen.blit(self.mob,(self.randomxx,self.mobRECTANGLE.y))
            #self.screen.blit(self.mob,(self.randomxxx,self.mobRECTANGLE.y))
            self.screen.blit(self.shot,self.shotRECTANGLE)

            self.playerRECTANGLE.x += XuniformlyXplayer #movement x
            self.playerRECTANGLE.y += YuniformlyYplayer #movement y
            self.multiple_bullets()
            self.shotRECTANGLE.y -= self.bulletchange


            pygame.display.update()
            self.pyclock.tick(60) 

   
    def bullet(self):
        
        self.shot = pygame.image.load('stuff/bullet.png')
        self.shotRECTANGLE = self.shot.get_rect()
        self.bulletchange = 0
        self.shotRECTANGLE.x = self.playerRECTANGLE.x
        if self.shotRECTANGLE.x == 0: #bugaa
            self.shotRECTANGLE.x = 400
        
    
    def fire_bullet(self):
        self.bulletchange = 15

    def multiple_bullets(self):
         if self.shotRECTANGLE.y <=0:
            self.shotRECTANGLE.y = 700
            self.fire = True

         if self.fire == True:
            self.shotRECTANGLE.y = self.playerRECTANGLE.y
            self.shotRECTANGLE.x = self.playerRECTANGLE.x
            self.screen.blit(self.shot,(self.shotRECTANGLE.x,self.shotRECTANGLE.y))
            self.shotRECTANGLE.y -= self.bulletchange
            self.fire = False

    def slayed(self):

        for m in range(self.enem):

            if self.shotRECTANGLE.colliderect(self.mobRECTANGLE[m]):
                self.mob[m] = pygame.image.load('stuff/boom.png').convert_alpha()
                self.mobRECTANGLE[m].x = -9999
                self.mobRECTANGLE[m].y = -9999

            if self.mobRECTANGLE[m].colliderect(self.playerRECTANGLE):

                self.player = pygame.image.load('stuff/explosion.png').convert_alpha()


    def config(self):
        pass


def main():

    game = SpaceInvader()
    game.init()
    game.main()
    game.mobs()
    game.bullet()
    game.main_loop()

if __name__ == '__main__':
    
    main()
    