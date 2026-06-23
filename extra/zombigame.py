import random

player_health = 100
zombies_killed = 0

print("🧟 Welcome to Zombie Fight!")
print("Defeat 5 zombies to win.\n")

while player_health > 0 and zombies_killed < 5:
    zombie_health = random.randint(20, 50)

    print(f"\nA zombie appears with {zombie_health} health!")

    while zombie_health > 0 and player_health > 0:
        print(f"\nYour Health: {player_health}")
        print(f"Zombie Health: {zombie_health}")

        action = input("Choose an action (attack/run): ").lower()

        if action == "attack":
            player_damage = random.randint(10, 25)
            zombie_health -= player_damage
            print(f"You hit the zombie for {player_damage} damage!")

            if zombie_health > 0:
                zombie_damage = random.randint(5, 15)
                player_health -= zombie_damage
                print(f"The zombie attacks you for {zombie_damage} damage!")

        elif action == "run":
            print("You escaped from the zombie!")
            break

        else:
            print("Invalid action! Try again.")

    if zombie_health <= 0:
        zombies_killed += 1
        print("🎉 Zombie defeated!")

print("\n===== GAME OVER =====")

if zombies_killed >= 5:
    print("🏆 Congratulations! You survived the zombie invasion!")
else:
    print("☠️ You were defeated by the zombies.")

print(f"Zombies Killed: {zombies_killed}")
print(f"Remaining Health: {max(0, player_health)}")