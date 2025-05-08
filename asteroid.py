import pygame
from circleshape import CircleShape
from constants import *
import random

class Asteroid(CircleShape):
	def __init__(self, x, y, radius):
		super().__init__(x, y, radius)

	def draw(self, screen):
		center = (int(self.position.x), int(self.position.y))
		pygame.draw.circle(screen, "white", center, self.radius, width=2)

	def update(self, dt):
		self.position += (self.velocity * dt)

	def split(self):
		self.kill()
		if self.radius <= ASTEROID_MIN_RADIUS:
			return
		random_angle = random.uniform(20, 50)
		velocity_1 = self.velocity.rotate(random_angle) * 1.2
		velocity_2 = self.velocity.rotate(-random_angle) * 1.2
		new_radius = self.radius - ASTEROID_MIN_RADIUS
		small_asteroid_1 = Asteroid(self.position.x, self.position.y, new_radius)
		small_asteroid_1.velocity = velocity_1
		small_asteroid_2 = Asteroid(self.position.x, self.position.y, new_radius)
		small_asteroid_2.velocity = velocity_2