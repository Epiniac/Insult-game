import random

class Character:
    def __init__(self, name, weaknesses):
        self.name = name
        self.current_insult = ""
        self.score = 0
        self.weaknesses = weaknesses

    def select_phrase(self, phrases):
        return random.choice(phrases)

    def assemble_insult(self, phrase):
        self.current_insult = phrase

    def reset_insult(self):
        self.current_insult = ""

    def effectiveness(self):
        effect = 1.0
        for insult in self.current_insult:
            if insult in self.weaknesses:
                effect*=2
        return effect
    
class Player1(Character):
    def __init__(self, name, weaknesses):
        super().__init__(name, weaknesses)

class Player2(Character):
    def __init__(self, name, weaknesses):
        super().__init__(name, weaknesses)

class Game:
    def __init__(self, max_rounds, player):
        self.current_round = 0
        self.max_rounds = max_rounds
        self.player = player

    def start_game(self):
        #TODO
        pass

    def end_game(self):
        #TODO
        pass

    def start_round(self):
        #TODO
        pass

    def end_round(self):
        #TODO
        pass

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


#fastai 