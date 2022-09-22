import random

place_list = ['Austin', 'Waco', 'Fort Worth',]
food_list = ['Pasta', 'Steak', 'Sushi']
travel_list = ['Car', 'Train', 'Hoverboard']
fun_list = ['Going shopping', 'Seeing a movie', 'Driving around and looking at mansions']

day_trip_dictionary = {
    "Transport": "Car",
    "Destination": "Austin", 
    "Food": "Pasta",
    "Activity": "Going Shopping",
}

print("")
print("Let's plan a day trip!")
print("")

def run_day_trip():

    def travel_selection():
        travel = random.choice(travel_list)
        user_choice = input(f"How does taking a {travel} sound? (Y?N) ")
        print("")
        while user_choice != "Y":
            print("Ok, let's try something else.")
            print("")
            travel = random.choice(travel_list)
            user_choice = input(f"How does taking a {travel} sound? (Y/N) ")
            print("")
        print("That soulds like fun!")
        print("")
        day_trip_dictionary["Transport"] = travel

    def place_selection():
        place = random.choice(place_list)
        user_choice = input(f"Lets' pick a fun place to go! How does {place} sound? (Y/N) ")
        print("")
        while user_choice != "Y":
            print("Ok, let's find somewhere else.")
            print("")
            place = random.choice(place_list)
            user_choice = input(f"How about {place}? (Y/N) ")
            print("")
        print("That sounds like a cool place!")
        print("")
        day_trip_dictionary["Destination"] = place

    def food_selection():
        food = random.choice(food_list)
        user_choice = input(f"Time for something tasty! How about {food}? (Y/N) ")
        print("")
        while user_choice != "Y":
            print("We'll find something else.")
            print("")
            food = random.choice(food_list)
            user_choice = input(f"What about {food} instead? (Y/N) ")
            print("")
        print("Sounds tasty!")
        print("")
        day_trip_dictionary["Food"] = food

    def activity_selection():
        fun = random.choice(fun_list)
        user_choice = input(f"How about {fun} while you're out? (Y/N) ")
        print("")
        while user_choice != "Y":
            print("We can find something else to do.")
            print("")
            fun = random.choice(fun_list)
            user_choice = input(f"How does {fun} sound? (Y/N) ")
            print("")
        print("Thats a fun thing to do!") 
        print("")
        day_trip_dictionary["Activity"] = fun

    travel_selection()
    place_selection()
    food_selection()
    activity_selection()
    
    print(f"Looks like you're taking a {day_trip_dictionary['Transport']} to {day_trip_dictionary['Destination']}.")
    user_choice = input(f"Then you'll grab some {day_trip_dictionary['Food']} while you enjoy {day_trip_dictionary['Activity']}. Sound good? (Y/N) ")
    print("")
    while user_choice != "Y":
        print("hmm...ok...lets start over then.")
        print("")
        run_day_trip()
    print("Have a great day trip!")
    print("")
    
run_day_trip()