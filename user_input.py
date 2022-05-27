import datetime as dt


class UserInput:
    def __init__(self):
        self.climb_type = (input('Hello climber, what did you do today?(Indoor/Outdoor/Sport):\n')).title()
        self.date = dt.datetime.now().strftime('%d/%m/%Y')
        self.place = (input('Where did you climb?:\n')).title()

    def routes_selection(self):
        if self.climb_type == 'Indoor':
            grades = ['green', 'blue', 'yellow', 'orange', 'red', 'black']
        elif self.climb_type == 'Outdoor':
            grades = ['V' + str(i) for i in range(18)]
        elif self.climb_type == 'Sport':
            grades = ['5', '5+', '6a', '6a+', '6b', '6b+', '6c', '6c+', '7a', '7a+', '7b+', '7c', '7c+', '8a', '8a+',
                      '8b', '8b+', '8c', '8c+', '9a', '9a+', '9b', '9b+', '9c']
        else:
            raise NameError('Write the climbing style as indicated in the first question.')

        climbs = {key: (input(f'How many {key}:\n')) for key in grades}
        print(climbs)