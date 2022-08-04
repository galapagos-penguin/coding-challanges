def zombie_shootout(zombies, distance, ammo):
    remaining_zombies = zombies
    remaining_distance = distance
    remaining_ammo = ammo
    while True:
        if remaining_zombies == 0:
            s = f'You shot all {zombies} zombies.'
            print(s)
            return s
        if remaining_distance == 0:
            s = f'You shot {zombies-remaining_zombies} zombies before being eaten: overwhelmed.'
            print(s)
            return s
        if remaining_ammo == 0:
            s = f'You shot {zombies-remaining_zombies} zombies before being eaten: ran out of ammo.'
            print(s)
            return s
        remaining_distance -= 0.5
        remaining_ammo -= 1
        remaining_zombies -= 1