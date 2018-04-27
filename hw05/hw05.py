##
# Tharin Dresher-Hurst
# hw05.py functions
# 25 - 04 - 18
# started functions - tdh
##

import random

def quiz():
    correctAnswer = 0
    questionsAsked = 0
    print('Match the state with the capital')
    stateCap = {'Alabama': 'Montgomery','Alaska': 'Juneau','Arizona':'Phoenix','Arkansas':'Little Rock','California': 'Sacramento','Colorado':'Denver','Connecticut':'Hartford','Delaware':'Dover','Florida': 'Tallahassee','Georgia': 'Atlanta','Hawaii': 'Honolulu','Idaho': 'Boise','Illinios': 'Springfield','Indiana': 'Indianapolis','Iowa': 'Des Monies','Kansas': 'Topeka','Kentucky': 'Frankfort','Louisiana': 'Baton Rouge','Maine': 'Augusta','Maryland': 'Annapolis','Massachusetts': 'Boston','Michigan': 'Lansing','Minnesota': 'St. Paul','Mississippi': 'Jackson','Missouri': 'Jefferson City','Montana': 'Helena','Nebraska': 'Lincoln','Neveda': 'Carson City','New Hampshire': 'Concord','New Jersey': 'Trenton','New Mexico': 'Santa Fe','New York': 'Albany','North Carolina': 'Raleigh','North Dakota': 'Bismarck','Ohio': 'Columbus','Oklahoma': 'Oklahoma City','Oregon': 'Salem','Pennsylvania': 'Harrisburg','Rhoda Island': 'Providence','South Carolina': 'Columbia','South Dakoda': 'Pierre','Tennessee': 'Nashville','Texas': 'Austin','Utah': 'Salt Lake City','Vermont': 'Montpelier','Virginia': 'Richmond','Washington': 'Olympia','West Virginia': 'Charleston','Wisconsin': 'Madison','Wyoming': 'Cheyenne'}
    while len(stateCap.keys()) != 0:
        question = random.choice(list(stateCap.keys()))
        answer = stateCap.pop(question)
        userInput = str(input("What is %s's capital city?\n" %(question)))
        if userInput == answer:
            correctAnswer += 1
            questionsAsked += 1
        else:
            questionsAsked += 1
    return correctAnswer, questionsAsked

def userScore(score, total):
    grade = (score/total)*100
    return grade
