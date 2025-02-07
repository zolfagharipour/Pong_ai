import pygame
from game import PongGame

def main():
	pygame.init()
	game = PongGame()
	game.run()
	pygame.quit()

if __name__ == "__main__":
	main()