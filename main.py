
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


def run_day_trip():

    print("")
    print("Let's plan a day trip!")
    print("")

    def travel_selection():
        travel = random.choice(travel_list)
        user_choice = input(f"How does taking a {travel} sound? (Y?N) ")
        while user_choice != "Y":
            print("Ok, let's try something else.")
            travel = random.choice(travel_list)
            user_choice = input(f"How does taking a {travel} sound? (Y/N) ")
        print("That soulds like fun!")
        day_trip_dictionary["Transport"] = travel

    def place_selection():
        place = random.choice(place_list)
        user_choice = input(f"Lets' pick a fun place to go! How does {place} sound? (Y/N) ")
        while user_choice != "Y":
            print("Ok, let's find somewhere else.")
            place = random.choice(place_list)
            user_choice = input(f"How about {place}? (Y/N) ")
        print("That sounds like a cool place!")
        day_trip_dictionary["Destination"] = place

    def food_selection():
        food = random.choice(food_list)
        user_choice = input(f"Time for something tasty! How about {food}? (Y/N) ")
        while user_choice != "Y":
            print("We'll find something else.")
            food = random.choice(food_list)
            user_choice = input(f"What about {food} instead? (Y/N) ")
        print("Sounds tasty!")
        day_trip_dictionary["Food"] = food

    def activity_selection():
        fun = random.choice(fun_list)
        user_choice = input(f"How about {fun} while you're out? (Y/N) ")
        while user_choice != "Y":
            print("We can find something else to do.")
            fun = random.choice(fun_list)
            user_choice = input(f"How does {fun} sound? (Y/N) ")
        print("Thats a fun thing to do!") 
        day_trip_dictionary["Activity"] = fun

    travel_selection()
    place_selection()
    food_selection()
    activity_selection()



# final_selection = input(f"For your trip you'll be taking a {day_trip_dictionary['Transport']} to {day_trip_dictionary['Destination']}. While you're there you'll grab some {day_trip_dictionary['Food']} before {day_trip_dictionary['Activity']}. How does that sound? (Y/N) ")
# while final_selection != "Y":

run_day_trip()