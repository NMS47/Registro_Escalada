import datetime as dt


class UserInput:
    def __init__(self):
        self.climb_type = self.type_climb()
        self.date = {'date': dt.datetime.now().strftime('%d/%m/%Y')}
        self.place = {'place': (input('Where did you climb?:\n')).title()}

    def routes_selection(self):
        if self.climb_type == 'boulderIndoors':
            grades = ['green', 'blue', 'yellow', 'orange', 'red', 'black']
        elif self.climb_type == 'boulderOutdoors':
            grades = ['V' + str(i) for i in range(18)]
        elif self.climb_type == 'sportClimbing':
            grades = ['5', '5+', '6a', '6a+', '6b', '6b+', '6c', '6c+', '7a', '7a+', '7b+', '7c', '7c+', '8a', '8a+',
                      '8b', '8b+', '8c', '8c+', '9a', '9a+', '9b', '9b+', '9c']

        climbs = {key: (input(f'How many {key}:\n')) for key in grades}
        user_inputs = {**self.date, **self.place, **climbs}
        print(user_inputs)
        return user_inputs

    def type_climb(self):
        user_choice = (input('Hello climber, what did you do today?(Indoors/Outdoors/Sport):\n')).title()
        if user_choice == 'Indoors' or user_choice == 'Outdoors':
            climb_style = 'boulder' + user_choice
        elif user_choice == 'Sport':
            climb_style = 'sportClimbing'
        else:
            raise NameError('Write the climbing style as indicated in the first question.')
        return climb_style
