################### Scope ####################

enemies = 1

def increase_enemies():
    global enemies
    enemies += 2
    print(f"enemies inside function: {enemies}")

increase_enemies()
print(f"enemies outside function: {enemies}")

# Global Constants
PI = 3.14
MANA_COST = [3, "red", "bluef"]
