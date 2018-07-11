# coding=utf-8

import sys
import pygame
from datetime import timezone
import struct
from pygame.locals import *
# print(sys.version)
# print(timezone.max)
pygame.init()

# file = open('binary.dat', 'wb+')
# for n in range(23):
#     data = struct.pack('i', n)
#     file.write(data)
#
# file.close()
#
# file = open('binary.dat', 'rb')
# size = struct.calcsize('i')
#
# bytes_read = file.read(size)
# while bytes_read:
#     value = struct.unpack('i', bytes_read)
#     value = value[0]
#     print(value, end=' ')
#     bytes_read = file.read(size)
# file.close()


class Trivia(object):
    def __init__(self, file_name):
        self.data = []
        self.current = 0
        self.total = 0
        self.correct = 0
        self.score = 0
        self.scored = False
        self.failed = False
        self.wronganswer = 0
        self.colors = [white,white,white,white]

        f = open(file_name, 'r')
        trivia_data = f.readlines()
        f.close()

        for text_line in trivia_data:
            self.data.append(text_line.strip())
            self.total += 1



    def show_question(self):
        print_text(font1, 210, 5, 'TRIVIA GAME')
        print_text(font2, 190, 500-20, 'Press key (1-4) To Answer', purple)
        print_text(font2, 500, 25, 'Score', purple)
        print_text(font2, 500, 25, str(self.score), purple)

        self.correct = int(self.data[self.current+5])

        question = self.current // 6 + 1
        print_text(font1, 5, 80, 'QUESTION' + str(question))
        print_text(font2, 20, 120, self.data[self.current], yellow)

        if self.scored:
            self.colors = [white,white,white,white]
            self.colors[self.current-1] = green
            print_text(font1, 230, 380, "CORreCT", green)
            print_text(font2, 170, 420, "Press Enter To Next Question", green)
        elif self.failed:
            self.colors = [white,white,white,white]
            self.colors[self.wronganswer-1] = red
            self.colors[self.correct-1] = green
            print_text(font1, 220, 380, 'INCORRECT', red)
            print_text(font1, 170, 420, 'ress Enter To Next Question', red)


        print_text(font1, 5, 170, 'ANSWER')
        print_text(font2, 20, 210, '1-' + self.data[self.current+1],self.colors[0])
        print_text(font2, 20, 240, '2-' + self.data[self.current+2],self.colors[1])
        print_text(font2, 20, 270, '3-' + self.data[self.current+3],self.colors[2])
        print_text(font2, 20, 300, '4-' + self.data[self.current+4],self.colors[3])


    def handler_input(self,number):
        if not self.scored and not self.failed:
            if number == self.correct:
                self.scored = True
                self.score += 1
            else:
                self.failed = True
                self.wronganswer = number

    def next_question(self):
        if self.scored or self.failed:
            self.scored = False
            self.scored = False
            self.corrent = 0
            self.colors = [white,white,white,white]
            self.current += 6
            if self.current >= self.total:
                self.current = 0



def print_text(font,x,y,text,color=(255,255,255),shadow=True):
    if shadow:
        imgText = font.render(text, True, (0,0,0))
        screen.blit(imgText, (x-2,y-2))
    imgText = font.render(text, True, color)
    screen.blit(imgText, (x, y))


screen = pygame.display.set_mode((800,600))
pygame.display.set_caption('The Trivia Game')
font1 = pygame.font.Font(None, 40)
font2 = pygame.font.Font(None, 24)
white = 255, 255, 255
cyan = 0, 255, 255
yellow = 255, 255, 0
purple = 255, 0, 255
green = 0, 255, 0
red = 255, 0, 0


trivia = Trivia('question')
pygame.key.set_repeat()



while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()
        # myfont = pygame.font.Font(None, 30)
        # screen = pygame.display.set_mode((800,600))
        # test = 'safukumei'
        # image = myfont.render(test, True, (255,255,255))
        # screen.blit(image,(100,100))
        # pygame.display.update()
        elif event.type == KEYUP:
            if event.key == pygame.K_ESCAPE:
                sys.exit()
            elif event.key == pygame.K_1:
                trivia.handler_input(1)
            elif event.key == pygame.K_2:
                trivia.handler_input(2)
            elif event.key == pygame.K_3:
                trivia.handler_input(3)
            elif event.key == pygame.K_4:
                trivia.handler_input(4)
            elif event.key == pygame.K_RETURN:
                trivia.next_question()

        screen.fill((0,0,200))
        trivia.show_question()
        pygame.display.update()
