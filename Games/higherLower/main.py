import random
from game_data import data
from art import *

print(logo)
def compare_followers(a,b):
    if a['follower_count']>b['follower_count']:
        return 1
    else:
        return 0
should_continue = True
score = 0
while should_continue:
    print(f"Your current score is {score}")
    a = random.choice(data)
    print("Compare A :"+a['name'] +" " +a['description']+" from "+a['country'])
    print(vs)
    b = random.choice(data)
    print("Against B: "+b['name'] +" " +b['description']+" from "+b['country'])
    guess = input("Who has more followers? Type 'A' or 'B' ").upper()
    if guess not in ['A', 'B']:
        print("Sorry, that's not a valid input.")
    else:
        compare_followers(a,b)
    if compare_followers(a,b) == 1 and guess == 'A':
        print(logo)
        print("Yes, that is correct!")
        score += 1
    elif compare_followers(a,b) == 0 and guess == 'B':
        print(logo)
        print("Yes. that is correct!")
        score += 1
    else:
        should_continue = False
        print(logo)
        print("Sorry, that's incorrect.")
