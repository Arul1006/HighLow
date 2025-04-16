import random
from Art import logo,vs
print(logo)

from GameData import data
a=b=1
while(a==b):
    a = random.randint(0,36)
    b = random.randint(0,36)
print(f" Compare A: {data[a]['name']}, {data[a]['description']}, {data[a]['country']}")
score = 0
def RecursionFromB(a,score):
    print(vs)
    b=a
    while(b==a):
        b = random.randint(0,36)
    print(f" Against B: {data[b]['name']}, {data[b]['description']}, {data[b]['country']}")

    guess = input("Who has more followers? Type 'A' or 'B' :").lower()
    if (data[a]['follower_count'] > data[b]['follower_count'] and guess == 'a') or (data[a]['follower_count'] < data[b]['follower_count'] and guess == 'b'):
        score += 1
        a = b
        print(logo)
        print(f"You're Right!! Current Score: {score}")
        print(f" Compare A: {data[a]['name']}, {data[a]['description']}, {data[a]['country']}")
        RecursionFromB(a,score)
    else:
        print(logo)
        print(f"Sorry, that's the wrong answer. Final Score: {score}")

RecursionFromB(a,score)






