# you must unlock Operators and Senses first in order for this to work without any warnings.

change_hat(Hats.Purple_Hat)

while True:
	move(North)
	if can_harvest():
		harvest()
		plant(Entities.Carrot)
	elif get_ground_type() == Grounds.Grassland:
		till()
		plant(Entities.Carrot)
	else:
		do_a_flip()