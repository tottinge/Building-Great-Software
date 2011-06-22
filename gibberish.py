import random

class Gibberish(object):
    names = ["Tim", "Jeff","Bob","Charlene"]
    adjectives = ["huge", "tiny","hairy","wrinkly"]
    parts = ["arms","ears","feet","earrings","knuckles"]

    def pickName(self):
        return random.choice(self.names)

    def speak(self):
        print self.pickName() + \
              " has "+\
              random.choice(self.adjectives)+ \
              " "+\
              random.choice(self.parts)+ \
              "."

if __name__ == "__main__":
    talker = Gibberish()
    talker.speak()
