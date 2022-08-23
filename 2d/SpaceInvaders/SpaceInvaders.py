import pygame, random

class SpaceInvader:

    def init(self):

        pygame.init()
        self.pyclock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((850,800))
        pygame.display.set_caption('Space Invaders')

    def main(self):

        self.enem = 80
        self.score = 0

        self.background = pygame.image.load('SpaceInvaders/stuff/background.jpg').convert_alpha()
        self.tescore = pygame.font.Font(None, 50)
        self.tetext = pygame.font.Font(None, 50)
        self.text = self.tetext.render(str(self.score), False, 'White').convert_alpha()
        self.textscore = self.tescore.render('Score: ', False, 'White').convert_alpha()
        self.player = pygame.image.load('SpaceInvaders/stuff/player.png').convert_alpha()
        self.playerRECTANGLE = self.player.get_rect()

    def mobs(self):
        
        self.mob = []
        self.mobRECTANGLE = []
        self.randomx = []
        self.mobspeed = []

        for m in range(self.enem):

            self.mob.append(pygame.image.load('SpaceInvaders/stuff/ufo.png').convert_alpha())
            self.mobRECTANGLE.append(self.mob[m].get_rect())
            self.randomx.append(random.randint(10,785))
            self.mobRECTANGLE[m].x = self.randomx[m]
            self.mobspeed.append(random.randint(2,4))
            self.mobRECTANGLE[m].y = random.randint(-200,-50)

            if m > 10 <20:
                self.mobRECTANGLE[m].y = -500
            if m > 20 <30:
                self.mobRECTANGLE[m].y = -1000
            if m > 30 <40:
                self.mobRECTANGLE[m].y = -1500
            if m > 40 <50:
                self.mobRECTANGLE[m].y = -2000
            if m > 50 <60:
                self.mobRECTANGLE[m].y = -2500
            if m > 60 <70:
                self.mobRECTANGLE[m].y = -3000
            if m > 70 <80:
                self.mobRECTANGLE[m].y = -3500
            if m > 80 <90:
                self.mobRECTANGLE[m].y = -4000
            if m > 90 <100:
                self.mobRECTANGLE[m].y = -4500
            if m > 100 <110:
                self.mobRECTANGLE[m].y = -5000

    def main_loop(self):

        self.fire = False

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
                        YuniformlyYplayer = -4.5

                    if ewent.key == pygame.K_s:
                        YuniformlyYplayer = 4.5     

                    if ewent.key == pygame.K_a:
                        XuniformlyXplayer = -4.5

                    if ewent.key == pygame.K_d: 
                        XuniformlyXplayer = 4.5

                if ewent.type == pygame.KEYUP:
                    XuniformlyXplayer = 0
                    YuniformlyYplayer = 0

            self.player_wall_colision()

            self.slayed()

            self.fire_bullet()

            self.screen.blit(self.background,(0,0)) #background
            self.screen.blit(self.textscore,(0,0))
            self.screen.blit(self.text,(110,0))
            self.screen.blit(self.player,self.playerRECTANGLE) #player
        
            self.waves(self.enem)

            self.screen.blit(self.shot,self.shotRECTANGLE)
            self.playerRECTANGLE.x += XuniformlyXplayer #movement x
            self.playerRECTANGLE.y += YuniformlyYplayer #movement y
            self.multiple_bullets()
            self.shotRECTANGLE.y -= self.bulletchange


            pygame.display.update()
            self.pyclock.tick(60) 

   
    def bullet(self):
        
        self.shot = pygame.image.load('SpaceInvaders/stuff/bullet.png').convert_alpha()
        self.shotRECTANGLE = self.shot.get_rect()
        self.bulletchange = 0
        self.shotRECTANGLE.x = self.playerRECTANGLE.x

        if self.shotRECTANGLE.x == 0: #bug
            self.shotRECTANGLE.x = 400     
    
    def fire_bullet(self):
        self.bulletchange = 20

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

    def player_wall_colision(self):

        if self.playerRECTANGLE.x <= 10:
            self.playerRECTANGLE.x = 11
        if self.playerRECTANGLE.x >= 780:
            self.playerRECTANGLE.x = 779
        if self.playerRECTANGLE.y >= 725:
            self.playerRECTANGLE.y = 724
        if self.playerRECTANGLE.y <= 150:
            self.playerRECTANGLE.y = 151

    def slayed(self):

        for m in range(self.enem):

            if self.shotRECTANGLE.colliderect(self.mobRECTANGLE[m]):
                self.mob[m] = pygame.image.load('SpaceInvaders/stuff/skull.png').convert_alpha()
                self.mobRECTANGLE[m].x = -9999
                self.mobRECTANGLE[m].y = -9999
                if self.mobRECTANGLE[m].y > -10:
                    self.mobRECTANGLE[m].y += random.randint(10,50)
                self.score += 10
                self.text = self.tetext.render(str(self.score), False, 'White')
                
            if self.mobRECTANGLE[m].colliderect(self.playerRECTANGLE):

                self.player = pygame.image.load('SpaceInvaders/stuff/explosion.png').convert_alpha()
                exit()


    def waves(self, wave:int):


        for m in range(wave):
                if m < 10:
                    self.screen.blit(self.mob[m],self.mobRECTANGLE[m])
                    self.mobRECTANGLE[m].y += self.mobspeed[m]
                    if self.mobRECTANGLE[m].y > 850:
                        self.mobRECTANGLE[m].y = -300
                        self.mobRECTANGLE[m].x = random.randint(10,785)

                if m > 10 <20:
                    self.screen.blit(self.mob[m],self.mobRECTANGLE[m])
                    self.mobRECTANGLE[m].y += self.mobspeed[m]
                    if self.mobRECTANGLE[m].y > 850:
                        self.mobRECTANGLE[m].y = -300
                        self.mobRECTANGLE[m].x = random.randint(10,785)
                
                if m > 20 <30:
                    self.screen.blit(self.mob[m],self.mobRECTANGLE[m])
                    self.mobRECTANGLE[m].y += 0.001
                    if self.mobRECTANGLE[m].y > 850:
                        self.mobRECTANGLE[m].y = -300
                        self.mobRECTANGLE[m].x = random.randint(10,785)
                
                if m > 30 <40:
                    self.screen.blit(self.mob[m],self.mobRECTANGLE[m])
                    self.mobRECTANGLE[m].y += 0.001
                    if self.mobRECTANGLE[m].y > 850:
                        self.mobRECTANGLE[m].y = -300
                        self.mobRECTANGLE[m].x = random.randint(10,785)
                
                if m > 40 <50:
                    self.screen.blit(self.mob[m],self.mobRECTANGLE[m])
                    self.mobRECTANGLE[m].y += 0.001
                    if self.mobRECTANGLE[m].y > 850:
                        self.mobRECTANGLE[m].y = -300
                        self.mobRECTANGLE[m].x = random.randint(10,785)
                
                if m > 50 <60:
                    self.screen.blit(self.mob[m],self.mobRECTANGLE[m])
                    self.mobRECTANGLE[m].y += 0.00001
                    if self.mobRECTANGLE[m].y > 850:
                        self.mobRECTANGLE[m].y = -300
                        self.mobRECTANGLE[m].x = random.randint(10,785)
                
                if m > 60 <70:
                    self.screen.blit(self.mob[m],self.mobRECTANGLE[m])
                    self.mobRECTANGLE[m].y += 0.0001
                    if self.mobRECTANGLE[m].y > 850:
                        self.mobRECTANGLE[m].y = -300
                        self.mobRECTANGLE[m].x = random.randint(10,785)
                
                if m > 70 <80:
                    self.screen.blit(self.mob[m],self.mobRECTANGLE[m])
                    self.mobRECTANGLE[m].y += 0.001
                    if self.mobRECTANGLE[m].y > 850:
                        self.mobRECTANGLE[m].y = -300
                        self.mobRECTANGLE[m].x = random.randint(10,785)
                
                if m > 80 <90:
                    self.screen.blit(self.mob[m],self.mobRECTANGLE[m])
                    self.mobRECTANGLE[m].y += 0.000001
                    if self.mobRECTANGLE[m].y > 850:
                        self.mobRECTANGLE[m].y = -300
                        self.mobRECTANGLE[m].x = random.randint(10,785)
                
                if m > 90 <100:
                    self.screen.blit(self.mob[m],self.mobRECTANGLE[m])
                    self.mobRECTANGLE[m].y += 0.00002
                    if self.mobRECTANGLE[m].y > 850:
                        self.mobRECTANGLE[m].y = -300
                        self.mobRECTANGLE[m].x = random.randint(10,785)
                
                if m > 100 <110:
                    self.screen.blit(self.mob[m],self.mobRECTANGLE[m])
                    self.mobRECTANGLE[m].y += 0.00003
                    if self.mobRECTANGLE[m].y > 850:
                        self.mobRECTANGLE[m].y = -300
                        self.mobRECTANGLE[m].x = random.randint(10,785)

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
    