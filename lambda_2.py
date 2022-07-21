print('Lambdas Exercise')

class Player:
   def __init__(self, name, score):
       self.name = name
       self.score =  score

Eric = Player('Eric', 116700)
John = Player('John', 24327)
Terry = Player('Terry', 150000)
player_list = [Eric, John, Terry]



#Exercise: Sort this by score using lambda!
#write code here 
player_list.sort(key = lambda person: int(person.score))
# for person in player_list:
    # print(person.name, end=' ')
print([player.name for player in player_list])
player_list.reverse()
print([player.name for player in player_list])

