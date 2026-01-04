while True:
    if can_harvest():
        harvest()
    else:
        do_a_flip()