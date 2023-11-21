class Character:
    insult_block = [
        "fleshless", "dog food", "can't aim", "scared of cats", "basically a glitched pig",
        "creepy", "brainless", "bag of rotten flesh", "emergency food", 
        "can't swim", "skinny tower", "ugly", "gold digger", "gets bitten by its mount",
        "stupid", "unreliable", "empty pumpkin head", "tall and scary",
        "Your mom", "dumdass", "little shit", "coward", "airhead", "asshole", "ass-kisser",
        "bimbo", "bastard", "rat"
    ]

    def __init__(self, name, weaknesses):
        self.name = name
        self.current_insult = ""
        self.score = 100
        self.weaknesses = weaknesses

    def input_insult(self):
        return input(f"{self.name}, enter your insult: ")

    def assemble_insult(self, phrase):
        self.current_insult = phrase

    def reset_insult(self):
        self.current_insult = ""

    def combo_meter(self):
        combo = 0
        for block in self.insult_block:
            if block in self.current_insult:
                combo += 1
        combo+= len(self.current_insult)*0.2
        return combo
    
    def effectiveness(self):
        effect = 2
        for weakness in self.weaknesses:
            if weakness in self.current_insult:
                print("\nEmotional Damage !!")
                effect *= 2
        return effect

    def calculate_damage(self, opponent):
        effect = self.effectiveness()
        combo = self.combo_meter()
        damage = effect + combo
        opponent_score_before = opponent.score
        opponent.score -= damage
        return damage, opponent_score_before, opponent.score


skeleton_weak = ["fleshless", "dog food", "can't aim"]
skeleton = Character("Skeleton", skeleton_weak)

creeper_weak = ["scared of cats", "basicly a gliched pig", "creepy"]
creeper = Character("Creeper", creeper_weak)

zombie_weak = ["brainless", "bag of rotten flesh", "emergency food"]
zombie = Character("Zombie", zombie_weak)

enderman_weak = ["can't swim", "skinny tower", "ugly"]
enderman = Character("Enderman", enderman_weak)

piglin_weak = ["gold digger", "gets bitten by its mount", "stupid"]
piglin = Character("Piglin", piglin_weak)

golem_weak = ["unreliable", "empty pumpkin head", "tall and scary"]
golem = Character("Golem",golem_weak)

c_list = [skeleton, creeper, zombie, enderman, piglin, golem]

name_list = [skeleton.name,creeper.name,zombie.name,enderman.name,piglin.name,golem.name]

def main():

    for character in c_list:
        print(character.name," / ", character.weaknesses)

    player1_input = str(input("\nSelect a character for player one:"))

    while player1_input not in name_list:
        player1_input = str(input("\nPlease select a valid character! :"))

    lengh = len(c_list)
    for i in range(lengh):
        if name_list[i] == player1_input:
            player1 = c_list[i]

    player2_input = str(input("\nSelect a character for player two:"))

    while player2_input not in name_list :
        player2_input = str(input("\nPlease select a valid character! :"))

    for i in range(lengh):
        if name_list[i] == player2_input:
            player2 = c_list[i]

    while player1.score > 0 and player2.score > 0:
        print("\n" + "=" * 30)
        print(f"{player1.name}'s Score: {player1.score}")
        print(f"{player2.name}'s Score: {player2.score}")
        print("=" * 30 + "\n")

        player1.assemble_insult(player1.input_insult())
        print(f"{player1.name}'s insult: {player1.current_insult}")

        damage, _, _ = player1.calculate_damage(player2)
        print(f"\nDamage dealt to {player2.name}: {damage}\n")

        player2.assemble_insult(player2.input_insult())
        print(f"{player2.name}'s insult: {player2.current_insult}")

        damage, _, _ = player2.calculate_damage(player1)
        print(f"\nDamage dealt to {player1.name}: {damage}\n")

    print("\nGame Over!")
    if player1.score > player2.score:
        print(f"{player1.name} wins!")
    elif player2.score > player1.score:
        print(f"{player2.name} wins!")
    else:
        print("It's a draw!")

    print("! FATALITIES !")

if __name__ == "__main__":
    main()