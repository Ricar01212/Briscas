import random
class Cards:
    def __init__(self, type, number, value = 0):
        self.type = type
        self.number = number
        self.value = value


    def __str__(self):
        return f"{self.number} of {self.type}"

#Clubs
club1 = Cards("Club", 1, 11)
club3 = Cards("Club", 3, 10)
club12 = Cards("Club", 12, 4)
club11 = Cards("Club", 11, 3)
club10 = Cards("Club", 10, 2)
club7 = Cards("Club", 7)
club6 = Cards("Club", 6)
club5 = Cards("Club", 5)
club4 = Cards("Club", 4)
club2 = Cards("Club", 2)
#Crowns
crown1 = Cards("Crown", 1, 11)
crown3 = Cards("Crown", 3, 10)
crown12 = Cards("Crown", 12, 4)
crown11 = Cards("Crown", 11, 3)
crown10 = Cards("Crown", 10, 2)
crown7 = Cards("Crown", 7)
crown6 = Cards("Crown", 6)
crown5 = Cards("Crown", 5)
crown4 = Cards("Crown", 4)
crown2 = Cards("Crown", 2)
#Gold
gold1 = Cards("Gold", 1, 11)
gold3 = Cards("Gold", 3, 10)
gold12 = Cards("Gold", 12, 4)
gold11 = Cards("Gold", 11, 3)
gold10 = Cards("Gold", 10, 2)
gold7 = Cards("Gold", 7)
gold6 = Cards("Gold", 6)
gold5 = Cards("Gold", 5)
gold4 = Cards("Gold", 4)
gold2 = Cards("Gold", 2)
# Sword
sword1 = Cards("Sword", 1, 11)
sword3 = Cards("Sword", 3, 10)
sword12 = Cards("Sword", 12, 4)
sword11 = Cards("Sword", 11, 3)
sword10 = Cards("Sword", 10, 2)
sword7 = Cards("Sword", 7)
sword6 = Cards("Sword", 6)
sword5 = Cards("Sword", 5)
sword4 = Cards("Sword", 4)
sword2 = Cards("Sword", 2)



AllCards = [club1, club3, club12, club11, club10, club7, club6, club5, club4, club2,
            crown1, crown3, crown12, crown11, crown10, crown7, crown6, crown5, crown4, crown2,
            gold1, gold3, gold12, gold11, gold10, gold7, gold6, gold5, gold4, gold2,
            sword1, sword3, sword12, sword11, sword10, sword7, sword6, sword5, sword4, sword2]



Mycards = []
Rivalcards = []

def shuffle(AllCards):
    Mycards.clear()
    Rivalcards.clear()
    kill = AllCards[len(AllCards) - 1].type
    for num in range(6):
        if (num % 2 == 0):
            Mycards.append(AllCards[num])
        else:
            Rivalcards.append(AllCards[num])

    AllCards = AllCards[6:]
    return AllCards

def game(AllCards):
    random.shuffle(AllCards)
    turn = 0
    AllCards = shuffle(AllCards)
    Player_Points = 0
    Enemy_Points = 0

    while True:


        if (len(Mycards) == 0 and len(Rivalcards) == 0):
            print(f"\n Your points: {Player_Points} \n Enemy points: {Enemy_Points}")
            break

        else:
            if (turn > 0 and len(AllCards) != 0):
                Mycards.append(AllCards[0])
                Rivalcards.append(AllCards[1])
                AllCards = AllCards[2:]

            print("YOUR CARDS") #TEST
            for num in range(len(Mycards)):
                print(f"{num + 1}. {Mycards[num]}")

            print("RIVAL CARDS") #TEST
            for num in range(len(Rivalcards)):
                print(f"{num + 1}. {Rivalcards[num]}")


            user = int(input("Choose your card: "))
            while user < 1 or user > len(Mycards):
                user = int(input("Invalid number, try again: "))

            rival = random.randint(0, len(Rivalcards) - 1)

            if (Mycards[user - 1].value >= Rivalcards[rival - 1].value):
                print("YOU WIN!")
                Player_Points += Mycards[user - 1].value + Rivalcards[rival - 1].value
            else:
                print("YOU LOSE!")
                Enemy_Points += Mycards[user - 1].value + Rivalcards[rival - 1].value

        #print(f"\n Your points: {Player_Points} \n Enemy points: {Enemy_Points}")
        Mycards.pop(user - 1)
        Rivalcards.pop(rival - 1)
        turn += 1

game(AllCards)