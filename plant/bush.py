change_hat(Hats.Purple_Hat)

while True:
	plant(Entities.Bush)
	move(North) # or other direction, depending on the drone's position.
	if can_harvest():
		harvest()