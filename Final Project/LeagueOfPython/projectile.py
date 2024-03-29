import pygame


class Projectile(pygame.sprite.Sprite):
    def __init__(self, xcoor, ycoor, velocity, damage, team, image):
        """
        Same as in Player, all varibles needed are initialized here
        :param xcoor: x pos of bullet
        :param ycoor: y pos of bullet
        :param velocity: vel of bullet
        :param damage: damage of bullet
        :param team: bullet's shooter's team
        :param image: image file of bullet
        """
        self.res = pygame.display.get_surface().get_size()
        pygame.sprite.Sprite.__init__(self)
        self.x = xcoor
        self.y = ycoor
        self.vel = velocity
        self.dmg = damage
        self.team = team
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        self.projectile = self.image
        self.rect = self.projectile.get_rect()
        self.rect.center = self.x, self.y

    def bullet_travelling(self, ally_player, enemy_player, bullets_hit):
        """
        Updates bullets
        :param ally_player: ally player
        :param enemy_player: not friendly player
        :param bullets_hit: num of bullets hit
        :return: bullets hit
        """
        if self.team == "BLUE" and self.x < self.res[0]:
            self.x += self.vel
        if self.team == "RED" and self.x > 0:
            self.x -= self.vel
        if self.team == "BLUE" and self.x >= self.res[0]:
            self.kill()
        if self.team == "RED" and self.x <= 0:
            self.kill()
        if self.rect.colliderect(enemy_player.rect):
            enemy_player.hp = enemy_player.hp - self.dmg

            # lifesteal bullet
            if self in ally_player.lsbullets.sprites():
                if ally_player.hp < ally_player.maxhp:
                    ally_player.hp += self.dmg
                if ally_player.hp > ally_player.maxhp:
                    ally_player.hp = ally_player.maxhp

            self.kill()
            bullets_hit += 1
        self.rect = self.image.get_rect()
        self.rect.center = self.x, self.y
        return bullets_hit
