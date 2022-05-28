#main code
from user_input import UserInput
from add_data import AddData

user_inputs = UserInput()
AddData(user_inputs.climb_type).new_rows(user_inputs.routes_selection())
print('Data uploaded succesfully.')