class Character:
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

    def calculate_damage(self, opponent):
        effectiveness = self.calculate_effectiveness(opponent)
        damage = effectiveness + 4
        opponent_score_before = opponent.score
        opponent.score -= damage
        return damage, opponent_score_before, opponent.score
    
    def effectiveness(self):
        effect = 2
        for weakness in self.weaknesses:
            if weakness in self.current_insult:
                effect*=2
        return effect

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

insult_block = ["fleshless", "dog food", "can't aim", "scared of cats", "basicly a gliched pig",
                "creepy", "brainless", "bag of rotten flesh", "emergency food", 
                "can't swim", "skinny tower", "ugly", "gold digger", "gets bitten by its mount",
                "stupid", "unreliable", "empty pumpkin head", "tall and scary",
                "Your mom", "dumdass", "little shit", "coward", "airhead", "asshole", "ass-kisser","bimbo", "bastard", "rat"]
