class Fila:
    def __init__(self):
        self.fila = []

    def enfileirar(self, item):
        self.fila.append(item)
        print(f"{item} adicionado à fila")

    def desenfileirar(self):
        if not self.esta_vazia():
            item = self.fila.pop(0)
            print(f"{item} removido da fila")
            return item
        else:
            print("A fila está vazia")
            return None

    def esta_vazia(self):
        return len(self.fila) == 0

    def tamanho(self):
        return len(self.fila)

# Exemplo de uso
fila = Fila()
fila.enfileirar(1)
fila.enfileirar(2)
fila.enfileirar(3)
print(f"Tamanho da fila: {fila.tamanho()}")
fila.desenfileirar()
print(f"Tamanho da fila: {fila.tamanho()}")


#import vlc
 
# # importing time module
# import time
 
 
# # creating vlc media player object
# media_player = vlc.MediaPlayer()
 
# # media object
# media = vlc.Media("./videos/prototipo-ag.mkv")
 
# # setting media to the media player
# media_player.set_media(media)
 
 
# # start playing video
# media_player.play()
 
# # wait so the video can be played for 5 seconds
# # irrespective for length of video
# time.sleep(5)