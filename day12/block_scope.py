# Python does not have block scope

game_level = 3

enimies = ["Skeletons", "Zombies", "Alien"]

if game_level < 5:
    new_enemy = enimies[0]

    print(new_enemy)

def create_enemy():
    if game_level < 5:
        new_enemy_func = enimies[0]

print(new_enemy_func)
