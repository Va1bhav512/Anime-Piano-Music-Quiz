from random import shuffle
from playsound import playsound
from inputimeout import inputimeout, TimeoutOccurred
from time import sleep
import json

with open('QNA.json','r') as qna_file:
    data = json.load(qna_file)

# Shuffle the data which is a dictionary by converting into a list
shuffledData:list = list(data.keys())
shuffle(shuffledData)

# Initialize counts
correctCount:int = 0
incorrectCount:int = 0


for i in shuffledData:
    print(f"Question: {data[i]["question"]}\n")
    sleep(1.5)

    # Try to get input using inputimeout
    try:
        
        # Start the song
        playsound(data[i]["song"])
        print("Your options are:\n")
        print(*(j for j in data[i]["options"][:4]),"\n",sep='\n')

        ans = inputimeout(prompt='>>',timeout=10)

    # If user did not input anything then change ans to empty string
    except TimeoutOccurred:
        ans = ''
    if(not ans):
        print("You did not answer!")
        incorrectCount += 1
    else:
        # Check if input answer is same as solution
        if(ans.lower().strip() == data[i]["answer"].lower()):
            correctCount += 1
            print("Your answer was correct!")
        else:
            incorrectCount += 1
            print(f"Your answer was incorrect! Correct answer was {data[i]["answer"]}!")

    print(f"Your score is {correctCount}")
    sleep(3)
    print("Moving on...")
    sleep(3)

print(f"You answered {correctCount} questions correctly and {incorrectCount} questions incorrectly out of {len(data)} questions!")