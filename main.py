
import random

place_list = ['Austin', 'Waco', 'Fort Worth',]

food_list = ['Pasta', 'Steak', 'Sushi']

travel_list = ['Car', 'Train', 'Hoverboard']

fun_list = ['Going shopping', 'Seeing a movie', 'Driving around and looking mansions']

day_trip_dictionary = {
    "Transport": "",
    "Destination": "", 
    "Food": "",
    "Entertainment": "",
}

# travel = random.choice(travel_list)
# food = random.choice(food_list)
# place = random.choice(place_list)
# fun = random.choice(fun_list)
print("")
print("Lets plan a day trip!")
print("")

def travel_selection():
    travel = random.choice(travel_list)
    user_choice = input(f"How does taking a {travel} sound? (Y?N) ")
    while user_choice != "Y":
        print("Ok, let's try something else.")
        travel = random.choice(travel_list)
        user_choice = input(f"How does taking a {travel} sound? (Y/N) ")
    print("That soulds like fun!")

travel_selection()