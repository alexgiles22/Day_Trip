
import random

place_list = ['Austin', 'Waco', 'Fort Worth',]

food_list = ['Pasta', 'Steak', 'Sushi']

travel_list = ['Car', 'Train', 'Hoverboard']

fun_list = ['Going shopping', 'Seeing a movie', 'Driving around and looking at mansions']

day_trip_dictionary = {
    "Transport": "",
    "Destination": "", 
    "Food": "",
    "Activity": "",
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

def place_selection():
    place = random.choice(place_list)
    user_choice = input(f"Lets' pick a fun place to go! How does {place} sound? (Y/N) ")
    while user_choice != "Y":
        print("Ok, let's find somewhere else.")
        place = random.choice(place_list)
        user_choice = input(f"How about {place}? (Y/N) ")
    print("That sounds like a cool place!")

def food_selection():
    food = random.choice(food_list)
    user_choice = input(f"Time for something tasty! How about {food}? (Y/N) ")
    while user_choice != "Y":
        print("We'll find something else.")
        food = random.choice(food_list)
        user_choice = input(f"What about {food} instead? (Y/N) ")
    print("Sounds tasty!")

def activity_selection():
    fun = random.choice(fun_list)
    user_choice = input(f"How about {fun} while you're out? (Y/N) ")
    while user_choice != "Y":
        print("We can find something else to do.")
        fun = random.choice(fun_list)
        user_choice = input(f"How does {fun} sound? (Y/N) ")
    print("Thats a fun thing to do!")

travel_selection()
place_selection()
food_selection()
activity_selection()