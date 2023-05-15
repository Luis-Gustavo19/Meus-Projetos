'''Exercício Python 21: Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3'''
import pygame
pygame.init()
pygame.mixer.music.load('ex0021.mp3')
pygame.mixer.music.play()
input()
pygame.event.wait()

#não deu certo de primeira pq o comando mudou com o tempo,maas vi nos comentárosma expçicacção e agr prestou.