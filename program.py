import threading
import pygame
import time


def tocar_som(caminho_som):
    pygame.mixer.init() 
    pygame.mixer.music.load(caminho_som) 
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        time.sleep(0.1)



def iniciar_thread_som_1():
    thread1 = threading.Thread(target=tocar_som, args=("old-sound-of-zombie-in-minecraft.mp3",))
    thread1.start()
    return thread1

def iniciar_thread_som_2():
    thread2 = threading.Thread(target=tocar_som, args=("vai-corinthians-estouradasso.mp3",))
    thread2.start()
    return thread2

def iniciar_thread_som_3():
    thread3 = threading.Thread(target=tocar_som, args=("pega-o-jack.mp3",))
    thread3.start()
    return thread3

def dungeon():
    print("Você está em uma dungeon. Escolha um caminho:")
    print("1 - Caminho da esquerda")
    print("2 - Caminho do meio")
    print("3 - Caminho da direita")
    
    escolha = input("Digite o número do caminho (1, 2 ou 3): ")

    if escolha == '1':
        print("Você escolheu o Caminho da esquerda. Um som misterioso ecoa!")

        thread1 = iniciar_thread_som_1()
        thread1.join() 

    elif escolha == '2':
        print("Você escolheu o Caminho do meio. Um rugido de monstros vem de longe!")
        
        thread2 = iniciar_thread_som_2()
        thread2.join()

    elif escolha == '3':
        print("Você escolheu o Caminho da direita. Tem um homem gritando!")
  
        thread3 = iniciar_thread_som_3()
        thread3.join()

    else:
        print("Escolha inválida! Tente novamente.")
        dungeon()

    print("Som finalizado. Você pode seguir em frente!")

if __name__ == "__main__":
    
    dungeon()
