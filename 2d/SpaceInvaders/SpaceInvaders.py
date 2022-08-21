import pygame, random, time

class SpaceInvader:

    def init(self):

        pygame.init()

        self.pyclock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((850,800))
        pygame.display.set_caption('Space Invaders')


    def main(self):

        self.background = pygame.image.load('stuff/background.jpg').convert_alpha()

        self.player = pygame.image.load('stuff/player.png').convert_alpha()
        self.playerRECTANGLE = self.player.get_rect()

    def mobs(self):
        self.mob = pygame.image.load('stuff/ufo.png').convert_alpha()
        self.mobRECTANGLE = self.mob.get_rect()
        self.randomx = random.randint(10,840)
        self.randomxx = random.randint(10,840)
        self.randomxxx = random.randint(10,840)
        self.mobRECTANGLE.x = self.randomx

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
                        YuniformlyYplayer = -2 

                    if ewent.key == pygame.K_s:
                        YuniformlyYplayer = 2      

                    if ewent.key == pygame.K_a:
                        XuniformlyXplayer = -2 

                    if ewent.key == pygame.K_d: 
                        XuniformlyXplayer = 2

                if ewent.type == pygame.KEYUP:
                    XuniformlyXplayer = 0
                    YuniformlyYplayer = 0

            self.slayed()

            self.fire_bullet()

            self.screen.blit(self.background,(0,0)) #background
            self.screen.blit(self.player,self.playerRECTANGLE) #player
            self.screen.blit(self.mob,self.mobRECTANGLE) #mob
            #self.screen.blit(self.mob,(self.randomxx,self.mobRECTANGLE.y))
            #self.screen.blit(self.mob,(self.randomxxx,self.mobRECTANGLE.y))
            self.screen.blit(self.shot,self.shotRECTANGLE)

            self.playerRECTANGLE.x += XuniformlyXplayer #movement x
            self.playerRECTANGLE.y += YuniformlyYplayer #movement y
            self.mobRECTANGLE.y += MOBMOVEMENT
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

        def fun(self):
            self.mobRECTANGLE.x = -9999
            self.mobRECTANGLE.y = -9999

        if self.shotRECTANGLE.colliderect(self.mobRECTANGLE):
            self.mob = pygame.image.load('stuff/boom.png').convert_alpha()
            self.mobRECTANGLE.x = -9999
            self.mobRECTANGLE.y = -9999

        if self.mobRECTANGLE.colliderect(self.playerRECTANGLE):

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