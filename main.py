"""
File:    main.py
Author:  Snowlin Alex
Section: 22
E-mail:  salex2@umbc.edu
Description:
  DESCRIPTION OF WHAT THE PROGRAM DOES
"""

def load_map(map_file_name):

    #This function must take a string which is the file name, and return the "map" or some representation of it for the rest of the game to use.

    f = open(map_file_name, "r")

    line_list = f.readlines()

    game_map = {}

    for line in line_list:

        # creating 2D dictionary to repersent "map"

        line = line.strip()

        line = line.split(",")

        # all lists with one variable are keys

        if len(line) == 1:

            key = line[0]

            game_map[key] = {}

        # rest of lines will become values for the current key

        else:

            game_map[key][line[0]] = int(line[1])

    return(game_map)

def load_events(event_file_name):

    #This function must take a string which is the file name, and return the events for the rest of the game to use.  You can add arguments to the function, but you must pass the file name.  This function must not set any global variables.

    f = open(event_file_name, "r")

    line_list = f.readlines()

    events = [ ]

    # converting a 2D list with all the event text and critical numbers

    for line in line_list:

        new_line = line.strip()

        new_line = new_line.split(",")

        # converting critical number "strings" to integers

        new_line[4] = int(new_line[4])

        new_line[5] = int(new_line[5])

        new_line[6] = int(new_line[6])

        events.append(new_line)

    return(events)

def play_game(start_time, game_map, events, charisma):

    #This function should handle most of the game functionality.  Whatever is returned to you in load_map and load_events should go into this function, as well as the amount of time you have to play.

    start_locations = []

    options_locations = []

    test_locations = []

    for i in range(len(events)):

        # Use test_locations to check if there is an event at the location

        test_locations.append(events[i][0])

    # options_locations will contain all the possible locations from current location

    for i in game_map:

        start_locations.append(i)

        temp = []

        for j in game_map[i]:

            temp.append(j)

        options_locations.append(temp)

    # Game begins with the time given at the first place on the map

    current_location = start_locations[0]

    time = 1 * start_time

    # Game will continue untill time runs out or ITE is reached: at that point there will be no more location options

    while ( current_location != "ITE" ) and ( time > 0 ):

        print("You are currently in", current_location, "and have", time, "seconds left to get to ITE.")

        for i in game_map[current_location]:

            print(i, game_map[current_location][i])

        new_location = input("Where do you want to go next? ")

        # Test to make sure inputted location is valid

        while new_location not in game_map[current_location]:

            new_location = input("That is a invalid location. Where do you want to go next? ")

        time = time - game_map[current_location][new_location]

        if new_location in test_locations:

            # not_crucial has no purpose: I had to fill if statement

            not_crucial = 0

            for i in range(len(test_locations)):

                if new_location != events[i][0]:

                    not_crucial += 1

                # for loop will find the i to index the proper event text from 2D list

                else:

                   print(events[i][1])

                   # Tests to see is there is enough charisma and stealth to pass and print win text

                   if (events[i][4] <= charisma) and (events[i][5] <= (10 - charisma)):

                       print(events[i][2])

                   else:

                       # print losing text and subtract time lost

                       print(events[i][3])

                       print("You lose", events[i][6], "seconds")

                       time = time - events[i][6]

        current_location = new_location

    if time >= 0 and ( current_location == "ITE"):

        print("You made it to ITE and now can learn the secrets of computer science.  You win!")

    else:

        print("You have run out of time, and so you lose.")

def create_character():

    #This function should create your character by getting the name, charisma and stealthiness.

    name = input("What is your name? Enter a first (middle) last separated by spaces, middle being optional. ")

    while " " not in name:

        name = input("Enter a first and last name: ")

    print("You have 10 skill points to distribute, otherwise you aren't going anywhere.")

    charisma = input("How charismatic are you, you have 10 skill points left? ")

    charisma = int(charisma)

    rem_skills = 10 - charisma

    stealth = input("How sneaky are you, you have " + str(rem_skills) + " skill points left? ")

    stealth = int(stealth)

    while ( charisma + stealth != 10) or ( charisma < 0 ) or ( stealth < 0 ):

        print("You have 10 skill points to distribute, they must all be positive. ")

        charisma = input("How charismatic are you, you have 10 skill points left? ")

        charisma = int(charisma)

        rem_skills = 10 - charisma

        stealth = input("How sneaky are you, you have " + str(rem_skills) + " skill points left? ")

        stealth = int(stealth)

    return(charisma)

if __name__ == "__main__":

    map_file_name = input("What is the map file? ")

    game_map = load_map(map_file_name)

    event_file_name = input("What is the events file? ")

    events = load_events(event_file_name)

    start_time = int(input("How much time do you want to start with? "))

    while start_time < 1 :

        start_time = int(input("Start time must be positive, Enter start time: "))

    charisma = create_character()

    play_game(start_time, game_map, events, charisma)
