#This will put the data to the Google Sheet

import requests
import os


class AddData:

    def __init__(self, climb_type):
        self.climb_type = climb_type
        self.endpoint = f'https://api.sheety.co/0a0d36d9222ff50d9006b8de7f458c79/climbingRecord/{self.climb_type}'
        self.username = os.environ['SHEETY_USER']
        self.password = os.environ['SHEETY_PASS']
        self.header = {'Content-Type': 'application/json'}

    def new_rows(self, user_inputs: list):
        if self.climb_type == 'boulderIndoors':
            new_row = {
                'boulderIndoors': user_inputs
    }
        elif self.climb_type == 'boulderOutdoors':
            new_row = {
                'boulderOutdoors': user_inputs
    }
        elif self.climb_type == 'sportClimbing':
            new_row = {
                'sportClimbing': user_inputs
    }
        else:
            print('Something is wrong!')

        sheety_response = requests.post(url=self.endpoint, json=new_row, headers=self.header,
                                    auth=(self.username, self.password))
        print(sheety_response.text)