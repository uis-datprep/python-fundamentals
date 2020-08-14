next_playerID = 0


class Player:
    def __init__(self, name): ## tested
        global next_playerID
        self.__id = next_playerID
        self.__name = name
        self.__points = 0
        next_playerID += 1

    def get_name(self): ## tested
        return self.__name

    def get_points(self):
        return self.__points

    def get_ID(self):
        return self.__id

    def set_name(self, name): ## tested
        if name == '':
            print('Error: name cannot be empty!') ## tested
        else:
            self.__name = name

    def set_points(self, points):## tested
        if points < 0:
            print('Error : points cannot be negative!')
        else:
            self.__points = points

    def add_points(self, points):## tested
        self.__points += points

    def __str__(self):
        return 'Player ' + format(self.__id) + ': ' + self.__name + \
               ' has points: ' + format(self.__points)