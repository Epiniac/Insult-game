import json

class Character:
    
    f = open('word.json', encoding="utf8")

    insult_block = json.loads(f.read())

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
        for block1 in self.insult_block["Nouns"]:
            if block1[1] in self.current_insult:
                combo += 1
        for block2 in self.insult_block["Verbs"]:
            if block2[1] in self.current_insult:
                combo += 1.1
        for block3 in self.insult_block["Endings"]:
            if block3[1] in self.current_insult:
                combo += 1.8
        combo += len(self.current_insult)*0.2
        return int(combo)

    def calculate_damage(self, opponent):

        opponent_weaknesses_present = any(weakness in self.current_insult for weakness in opponent.weaknesses)

        if opponent_weaknesses_present:
            print("\n !!! EMOTIONNAL DAMAGE !!! \n")
            damage = 15
        else:
            damage = 0

        combo = self.combo_meter()
        damage += combo

        opponent_score_before = opponent.score
        opponent.score -= damage

        return damage, opponent_score_before, opponent.score

skeleton_weak = ["a bag of bones"]
skeleton = Character("Skeleton", skeleton_weak)

creeper_weak = ["an armless pig"]
creeper = Character("Creeper", creeper_weak)

zombie_weak = ["a brainless monster"]
zombie = Character("Zombie", zombie_weak)

enderman_weak = ["a tall creepy guy"]
enderman = Character("Enderman", enderman_weak)

piglin_weak = ["a gold digger"]
piglin = Character("Piglin", piglin_weak)

golem_weak = ["a big iron nose"]
golem = Character("Golem",golem_weak)

c_list = [skeleton, creeper, zombie, enderman, piglin, golem]

name_list = [skeleton.name,creeper.name,zombie.name,enderman.name,piglin.name,golem.name]

def main():
    for character in c_list:
        print(character.name," / ", character.weaknesses)

    player1_input = str(input("\nSelect a character for player one: "))

    while player1_input not in name_list:
        player1_input = str(input("\nPlease select a valid character! : "))

    lengh = len(c_list)
    for i in range(lengh):
        if name_list[i] == player1_input:
            player1 = c_list[i]

    player2_input = str(input("\nSelect a character for player two: "))

    while player2_input not in name_list :
        player2_input = str(input("\nPlease select a valid character! : "))

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

        player2.assemble_insult(player2.input_insult())
        print(f"{player2.name}'s insult: {player2.current_insult}")

        damage, _, _ = player1.calculate_damage(player2)
        print(f"\nDamage dealt to {player2.name}: {damage}\n")

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