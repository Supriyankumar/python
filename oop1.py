class PlayerCharacter:
    def __init__(self, name, age):
       self.name = name
       self.age = age

    def run(self):
          print('run')

player1 = PlayerCharacter('Tom',55)
player2 = PlayerCharacter('John',60)

print(player1.name)
print(player2.age)
       
