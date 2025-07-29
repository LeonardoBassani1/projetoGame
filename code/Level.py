#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame
from code.EntityFactory import EntityFactory

class Level:
    def __init__(self, window, name, game_mode):
        self.window = window
        self.name = name
        self.game_mode = game_mode
        self.entity_list = []
        self.entity_list.extend(EntityFactory.get_entity('Level1Bg'))

    def run(self):
        running = True
        clock = pygame.time.Clock()
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    pygame.quit()
                    quit()

            # Desenha todos os backgrounds (e outras entidades depois)
            for ent in self.entity_list:
                self.window.blit(source=ent.surf, dest=ent.rect)
                ent.move()
            pygame.display.flip()
            clock.tick(60)  # limita a 60 FPS
