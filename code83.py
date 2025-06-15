# def water_state(temperature):
#     if temperature > 25:
#         return "Hot"
#     elif 15 < temperature <= 25:
#         return "Warm"
#     elif temperature < 15:
#         return "Cold"

# print(water_state(26))
# print(water_state(24))
# print(water_state(14))

from functions import count
 
nr_of_periods = count("Trees are good. Grass is green.")
print(nr_of_periods)