import pygame
import threading
import time
from config import *

class AI:
	def __init__(self, ball):
		self.ball = ball
		self.sees_ball = False
		self.direction = 0
		self.ball_seen_time = 0
		self.running = True

	def start(self):
		threading.Thread(target=self.observe_game, daemon=True).start()

	def observe_game(self):
		while self.running:
			time.sleep(1)
		
			self.sees_ball = True
			self.ball_seen_time = time.time()

			if self.ball.rect.centery < 300:
				self.direction  = -1
			else:
				self.direction = 1

	def get_ai_input(self):
		return self.direction