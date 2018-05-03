# SPGL Minimal Code by /u/wynand1004 AKA @TokyoEdTech
# Requires SPGL Version 0.8 or Above
# SPGL Documentation on Github: https://wynand1004.github.io/SPGL
# Use this as the starting point for your own games

# Import SPGL
import spgl
import random 
import math
import turtle

# Create Classes
class Player(spgl.Sprite):
	def __init__(self, shape, color, x, y):
		spgl.Sprite.__init__(self, shape, color, x, y)
		self.lives = 5
		self.score = 0
		
	def rotate_up(self):
		self.left(10)
		
	def rotate_down(self):
		self.right(10)
		
class Ball(spgl.Sprite):
	def __init__(self, shape, color, x, y):
		spgl.Sprite.__init__(self, shape, color, x, y)
		self.speed = 0
		self.state = "ready"
		
	def tick(self):
		if self.state == "firing":
			self.fd(self.speed)
		
			#Border checking
			if self.ycor() > 300:
				self.state = "ready"
				self.goto(player.xcor(), player.ycor())
			if self.ycor() < -300:
				self.state = "ready"
				self.goto(player.xcor(), player.ycor())
			if self.xcor() > 400:
				self.state = "ready"
				self.goto(player.xcor(), player.ycor())
			
					
	def shoot(self):
		if self.state == "ready":
			self.state = "firing"
			self.setheading(player.heading())
			self.speed = 10
			
	def rotate_up(self):
		if self.state == "ready":
			self.left(10)
		
	def rotate_down(self):
		if self.state == "ready":
			self.right(10)


		
	
number = random.randint(1,9)

class Obstacle(spgl.Sprite):
	def __init__(self, shape, color, x, y):
		spgl.Sprite.__init__(self, shape, color, x, y)
		self.setheading(90)
		self.speed = 0
	
	def tick(self):
		self.fd(5)
		
		if self.xcor() > 530:
			self.setx(530)
			self.left(180)
		if self.xcor() < -530:
			self.setx(-530)
			self.left(180)
		if self.ycor() > 290:
			self.sety(290)
			self.left(180)
		if self.ycor() < -290:
			self.sety(-290)
			self.left(180)	



		
# Create Functions
# Initial Game setup
game = spgl.Game(1100, 600, "black", "Uhhh Uhhh...Get It Across", 0)



 
# Create Sprites
player = Player("triangle", "white", -500, 0)
player.shapesize(1, 3, 0)
ball = Ball("circle", "yellow", -470, 0)
obstacle_1 = Obstacle("square", "red", 0, 100)
obstacle_2 = Obstacle("square", "red", 500, 300)
obstacle_3 = Obstacle("square", "red", 250, -200)
			
# sprite_name.set_image("image_name.gif", width, height)
obstacle_1.set_image("brick.gif", 70, 100)
obstacle_2.set_image("brick.gif", 70, 100)
obstacle_3.set_image("brick.gif", 70, 100)
player.set_image("MainGuySpriteSheet.gif", 65, 65)

# player.set_image("

obstacles = [obstacle_1, obstacle_2, obstacle_3]

# Create Labels
label_score = spgl.Label("Score: 0", "white", -525, 270)
#label_score.size_font_size(20) 

label_lives = spgl.Label("Lives left: 5", "white", -525, 250)  


# Create Buttons

# Set Keyboard Bindings

game.set_keyboard_binding(ball.shoot, "Right")
game.set_keyboard_binding(player.rotate_up, "Up")
game.set_keyboard_binding(player.rotate_down, "Down")
game.set_keyboard_binding(ball.rotate_up, "Up")
game.set_keyboard_binding(ball.rotate_down, "Down")
while True:
    # Call the game tick method
	game.tick()
	
	if ball.xcor() > 530:
		player.score += 10
		ball.goto(-470, 0)
		ball.speed = 0
		ball.state = "ready"
		label_score.update("Score: {}".format(player.score))

	for obstacle in obstacles:
		if game.is_collision(ball, obstacle):
			player.lives -= 1 
			print("You lost a life")
			ball.goto(-470, 0)
			ball.speed = 0
			ball.state = "ready"
			label_lives.update("Lives: {}".format(player.lives))
		
		

		
	
	
	
	# goal.move()

