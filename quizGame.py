import random
#Interactive quiz game in python

#prompt to the user
print("---Welcome to the U.S Capital Quiz Game!---\n")

#prompt the user if they would like to play
def isUserPlaying ():
    isPlaying = input("Would you like to play? (y/n) > ")
    print(isPlaying)
    return isPlaying
playing = 1
#class of states
class State:
    def __init__(self, state, capital):
        self.state = state
        self.capital = capital
#list of all our states
stateList = []

#define the state objects
Alabama = State("Alabama", "Montgomery")
stateList.append(Alabama)

Alaska = State("Alaska","Juneau")
stateList.append(Alaska)

Arizona = State("arizona", "Phoenix")
stateList.append(Arizona)

Arkansas = State("Arkansas", "Little Rock")
stateList.append(Arkansas)

California = State("California", "Sacramento")
stateList.append(California)

Colorado = State("Colorado", "Denver")
stateList.append(Colorado)

Connecticut = State("Connecticut", "Hartford")
stateList.append(Connecticut)

Delaware = State("Delaware", "Dover")
stateList.append(Delaware)

Florida = State("Florida", "Tallahassee")
stateList.append(Florida)

Georgia = State("Georgia", "Atlanta")
stateList.append(Georgia)

Hawaii = State("Hawaii", "Honolulu")
stateList.append(Hawaii)

Idaho = State("Idaho", "Boise")
stateList.append(Idaho)

Illinois = State("Illinois", "Springfield")
stateList.append(Illinois)

Indiana = State("Indiana", "Indianapolis")
stateList.append(Indiana)

Iowa = State("Iowa", "Des Moines")
stateList.append(Iowa)

Kansas = State("Kansas", "Topeka")
stateList.append(Kansas)

Kentucky = State("Kentucky", "Frankfort")
stateList.append(Kentucky)

Louisiana = State("Louisiana", "Baton Rouge")
stateList.append(Louisiana)

Maine = State("Maine", "Augusta")
stateList.append(Maine)

Maryland = State("Maryland", "Annapolis")
stateList.append(Maryland)

Massachusetts = State("Massachusetts", "Boston")
stateList.append(Massachusetts)

Michigan = State("Michigan", "Lansing")
stateList.append(Michigan)

Minnesota = State("Minnesota", "Saint Paul")
stateList.append(Minnesota)

Mississippi = State("Mississippi", "Jackson")
stateList.append(Mississippi)

Missouri = State("Missouri", "Jefferson City")
stateList.append(Missouri)

Montana = State("Montana", "Helena")
stateList.append(Montana)

Nebraska = State("Nebraska", "Lincoln")
stateList.append(Nebraska)

Nevada = State("Nevada", "Carson City")
stateList.append(Nevada)

NewHampshire = State("New Hampshire", "Concord")
stateList.append(NewHampshire)

NewJersey = State("New Jersey", "Trenton")
stateList.append(NewJersey)

NewMexico = State("New Mexico", "Santa Fe")
stateList.append(NewMexico)

NewYork = State("New York", "Albany")
stateList.append(NewYork)

NorthCarolina = State("North Carolina", "Raleigh")
stateList.append(NorthCarolina)

NorthDakota = State("North Dakota", "Bismarck")
stateList.append(NorthDakota)

Ohio = State("Ohio", "Columbus")
stateList.append(Ohio)

Oklahoma = State("Oklahoma", "Oklahoma City")
stateList.append(Oklahoma)

Oregon = State("Oregon", "Salem")
stateList.append(Oregon)

Pennsylvania = State("Pennsylvania", "Harrisburg")
stateList.append(Pennsylvania)

RhodeIsland = State("Rhode Island", "Providence")
stateList.append(RhodeIsland)

SouthCarolina = State("South Carolina", "Pierre")
stateList.append(SouthCarolina)

Tennessee = State("Tennessee", "Nashville")
stateList.append(Tennessee)

Texas = State("Texas", "Austin")
stateList.append(Texas)

Utah = State("Utah", "Salt Lake City")
stateList.append(Utah)

Vermont = State("Vermont", "Montpelier")
stateList.append(Vermont)

Virginia = State("Virginia", "Richmond")
stateList.append(Virginia)

Washington = State("Washington", "Olympia")
stateList.append(Washington)

WestVirginia = State("West Virginia", "Charleston")
stateList.append(WestVirginia)

Wisconsin = State("Wisconsin", "Madison")
stateList.append(Wisconsin)

Wyoming = State("Wyoming", "Cheyenne")
stateList.append(Wyoming)
#keep track of the user's score
userScore = 0
def giveState():
        global userScore
        #pick a random state for the user to guess its capital
        randomState = random.choice(stateList)
        answer = input(f"What is the capital of {randomState.state}? (type 'q' to quit or 'h' for a hint) >> ")
        #make the input all lowercase so that case sensitivity is not an issue
        lowerAnswer = answer.lower()
        #if the user guessed the state correct, increment the user's score
        if(lowerAnswer == randomState.capital.lower()):
            userScore = userScore + 1
            print(f"Correct! Your score is {userScore}\n")
        #if the user inputs 'quit', quit the program
        elif(lowerAnswer == 'q'):
            quit()
        #give the user an opportunity for a hint
        elif(lowerAnswer == 'h'):
            #give the user the first three letters of the capital
            print(randomState.capital[0:3])
            answer = input(f"(type 'q' to quit or 'h' for a hint) >> ")
            lowerAnswer = answer.lower()
            if(lowerAnswer == randomState.capital.lower()):
                userScore = userScore + 1
                print(f"Correct! Your score is {userScore}\n")
            else:
                print(f"wrong answer :( The capital is {randomState.capital}")
                userScore = 0
            
        #if the user gets the state wrong, set the score back to zero
        else:
            print(f"wrong answer :( The capital is {randomState.capital}")
            userScore = 0
           
#check if user is playing
userPlaying = isUserPlaying()
#if the user is playing, then run the giveState function
if(userPlaying == 'y'):
    while True:
        giveState()
else:
    print("goodbye!\n")
    quit()

        


