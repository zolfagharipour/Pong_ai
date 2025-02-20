import pygame
import time
from config import *
from ai import AI

class Paddle:
	def __init__(self, x, y, debug):
		self.rect = pygame.Rect(x, y, PADDLE_WIDTH, PADDLE_HEIGHT*(1+2*(debug)))

	def move(self, dy):
		if 0 <= self.rect.y + dy <= SCREEN_HEIGHT - PADDLE_HEIGHT:
			self.rect.y += dy
	def draw(self, window):
		pygame.draw.rect(window, WHITE, self.rect)


class Ball:
	def __init__(self, x, y):
		self.rect = pygame.Rect(x, y, BALL_SIZE, BALL_SIZE)
		self.vel_x = BALL_SPEED
		self.vel_y = BALL_SPEED
		self.color = WHITE
		self.last_seen_time = 0
		self.last_coll_time = 0
	
	def move(self):
		self.rect.x += self.vel_x
		self.rect.y += self.vel_y
		if self.rect.centery <= 0 or self.rect.centery >= SCREEN_HEIGHT:
			self.vel_y *= -1

	def draw(self, window):
		if time.time() - self.last_seen_time < 0.1:
			pygame.draw.ellipse(window, RED, self.rect)
		else:
			pygame.draw.ellipse(window, WHITE, self.rect)


class PongGame:
	def __init__(self):
		self.running = True
		self.window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
		pygame.display.set_caption("PONG AI")

		self.paddle1 = Paddle(0, SCREEN_HEIGHT // 2 - PADDLE_HEIGHT // 2 , True)
		# self.paddle1 = Paddle(0, SCREEN_HEIGHT // 2 - PADDLE_HEIGHT // 2 ,False)
		self.paddle2 = Paddle(SCREEN_WIDTH - PADDLE_WIDTH, SCREEN_HEIGHT // 2 - PADDLE_HEIGHT // 2 ,False)
		self.ball = Ball(SCREEN_HEIGHT // 2, PADDLE_HEIGHT // 2)

		self.ai = AI(self.ball, self.paddle2)
		self.ai.start()

	def run(self):
		clock = pygame.time.Clock()
		while self.running:
			self.handle_events()
			self.update()
			self.draw()
			clock.tick(FPS)

	def handle_events(self):
		keys = pygame.key.get_pressed()
		if keys[pygame.K_UP]:
			self.paddle1.move(-PADDLE_SPEED)
		if keys[pygame.K_DOWN]:
			self.paddle1.move(PADDLE_SPEED)
		if keys[pygame.K_ESCAPE]:
			self.running = False
			self.ai.running = False

		ai_move = self.ai.get_ai_input()
		if ai_move == -1:
			self.paddle2.move(-PADDLE_SPEED)
		elif ai_move == 1:
			self.paddle2.move(PADDLE_SPEED)


		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				self.running = False
				self.ai.running = False

	
	def update(self):
		self.ball.move()
		this_time = pygame.time.get_ticks()

		if self.ai.sees_ball:
			self.ball.last_seen_time = time.time()
			self.ai.sees_ball = False

		if self.ball.rect.colliderect(self.paddle1.rect) and pygame.time.get_ticks() - self.ball.last_coll_time > 3000 / FPS:
			dy = (self.paddle1.rect.centery - self.ball.rect.centery) / (PADDLE_HEIGHT / 2)
			self.ball.vel_x *= -1
			self.ball.vel_y *= 0.5 + abs(dy)
			self.ball.last_coll_time = pygame.time.get_ticks()
		elif self.ball.rect.colliderect(self.paddle2.rect) and pygame.time.get_ticks() - self.ball.last_coll_time > 3000 / FPS:
			dy = (self.paddle2.rect.centery - self.ball.rect.centery) / (PADDLE_HEIGHT / 2)
			self.ball.vel_x *= -1
			self.ball.vel_y *= 0.5 + abs(dy)
			self.ball.last_coll_time = pygame.time.get_ticks()

		if self.ball.rect.left <= 0 or self.ball.rect.right >= SCREEN_WIDTH:
			self.ball.rect.x = SCREEN_WIDTH // 2
			self.ball.rect.y = SCREEN_HEIGHT // 2
			self.ball.vel_x = -BALL_SPEED
			self.ball.vel_y = BALL_SPEED



		

	def draw(self):
		self.window.fill(BLACK)
		self.paddle1.draw(self.window)
		self.paddle2.draw(self.window)
		self.ball.draw(self.window)
		pygame.display.flip()