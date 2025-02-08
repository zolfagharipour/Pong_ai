import pygame
import threading
import time
import math
import numpy
from config import *

class AI:
	def __init__(self, ball, paddle):
		self.ball = ball
		self.paddle = paddle
		self.sees_ball = False
		self.direction = 0
		self.ball_seen_time = 0
		self.running = True
		# print( -1 * True, -1 * False)

	def start(self):
		threading.Thread(target=self.observe_game, daemon=True).start()

	def traj_calc(self):
			x_dist = SCREEN_WIDTH - self.ball.rect.right - PADDLE_WIDTH
			estimated_coll_time = x_dist / int(self.ball.vel_x)
			lazy_coll_y = self.ball.rect.centery + int(self.ball.vel_y) * estimated_coll_time 
			n_coll , residue =  lazy_coll_y // SCREEN_HEIGHT, lazy_coll_y % SCREEN_HEIGHT

			if n_coll % 2 != 0:
				residue = SCREEN_HEIGHT - residue
			if residue < self.paddle.rect.centery:
				self.direction  = -1
			elif residue > self.paddle.rect.centery:
				self.direction = +1
			needed_time = abs(residue - self.paddle.rect.centery) / (PADDLE_SPEED * FPS)
			self.sleep_time = min(AI_WAIT , needed_time)
			


	def observe_game(self):
		while self.running:
			self.direction , self.sleep_time = 0 , AI_WAIT
			if self.ball.vel_x > 0:
				self.traj_calc()
			self.ball.last_seen_time = time.time()	
			time.sleep(self.sleep_time)
			self.direction = 0 
			time.sleep(AI_WAIT - self.sleep_time)


	def get_ai_input(self):
		return self.direction