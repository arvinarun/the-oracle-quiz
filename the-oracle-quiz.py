# The Oracle Adventure - Upgraded Story

running = True

while running:

    print("🖤 Welcome to The Oracle Adventure 🖤")
    name = input("What is your name, traveler? ").strip()
    print(f"\nGreetings {name}, you awaken in a mysterious land...\n")

    score = 0

    # Scene 1: Choose a path
    answer = input("You see two paths: 🌲 left into the dark forest (1) or 🌄 right to the sunny hills (2)? ").strip()
    while answer not in ["1", "2"]:
        print("Invalid choice. Try again.")
        answer = input("You see two paths: 🌲 left into the dark forest (1) or 🌄 right to the sunny hills (2)? ").strip()
    if answer == "1":
        score += 1
        print("You enter the shadowy forest. The trees whisper secrets as you pass...")
    else:
        score += 2
        print("You climb the sunlit hills. Warmth and courage fill your chest...")

    # Scene 2: Encounter a mystical creature
    answer = input("\nA mystical creature appears: 🐉 dragon (1) or 🦅 giant eagle (2)? ").strip()
    while answer not in ["1", "2"]:
        print("Invalid choice. Try again.")
        answer = input("A mystical creature appears: 🐉 dragon (1) or 🦅 giant eagle (2)? ").strip()
    if answer == "1":
        score += 2
        print("The dragon gazes at you. Your bravery impresses it, and it allows you to pass...")
    else:
        score += 1
        print("The eagle circles above and drops a feather as a sign of favor...")

    # Scene 3: Find a potion
    answer = input("\nYou find a glowing potion: 🔴 red (1) or 🔵 blue (2)? ").strip()
    while answer not in ["1", "2"]:
        print("Invalid choice. Try again.")
        answer = input("You find a glowing potion: 🔴 red (1) or 🔵 blue (2)? ").strip()
    if answer == "1":
        score += 2
        print("The red potion fills you with daring energy...")
    else:
        score += 1
        print("The blue potion clears your mind, giving wisdom and calm...")

    # Scene 4: Choose a companion
    answer = input("\nYou meet two companions: 🐺 wolf (1) or 🐱 cat (2)? Who do you follow? ").strip()
    while answer not in ["1", "2"]:
        print("Invalid choice. Try again.")
        answer = input("You meet two companions: 🐺 wolf (1) or 🐱 cat (2)? Who do you follow? ").strip()
    if answer == "1":
        score += 2
        print("The wolf becomes your loyal ally, fierce and protective...")
    else:
        score += 1
        print("The cat guides you silently, clever and elusive...")

    # Scene 5: Face a challenge
    answer = input("\nYou reach a rickety bridge over a dark chasm: 🏃‍♂️ run across (1) or 🐾 step carefully (2)? ").strip()
    while answer not in ["1", "2"]:
        print("Invalid choice. Try again.")
        answer = input("You reach a rickety bridge over a dark chasm: 🏃‍♂️ run across (1) or 🐾 step carefully (2)? ").strip()
    if answer == "1":
        score += 2
        print("You dash across, fearless! Adrenaline fuels you...")
    else:
        score += 1
        print("You step carefully, every movement measured and precise...")

    # Ending based on score
    print("\n🔮 Your journey concludes... 🔮\n")
    if score <= 4:
        print(f"👼 {name}, you emerge as a Guardian of Calm. Wise, serene, and observant.")
    elif 5 <= score <= 7:
        print(f"🕶️ {name}, you become a Shadow Wanderer. Quiet, mysterious, and adaptable.")
    elif 8 <= score <= 10:
        print(f"😈 {name}, you are now a Fierce Adventurer. Bold, daring, and fearless.")
    elif 11 <= score <= 12:
        print(f"🃏 {name}, a Trickster of Fate. Clever, unpredictable, and playful.")
    else:
        print(f"👻 {name}, you are the Phantom of the Realm. Elusive, mystical, and untouchable.")

    # Ask to play again
    play_again = input("\nPlay Again? (yes/no): ").strip().lower()
    while play_again not in ["yes", "no"]:
        print("Invalid input. Type yes or no.")
        play_again = input("Play Again? (yes/no): ").strip().lower()

    if play_again == "no":
        running = False
        print("\nThank you for playing The Oracle Adventure! Farewell, traveler... 🖤")
    else:
        print("\nRestarting the adventure...\n")
