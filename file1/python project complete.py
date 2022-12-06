import random
print("WELCOME TO GUESS NUMBER GAME")
name=input("WHAT IS YOUR NAME:")
print(name,"ALL THE BEST!")
lower = int(input("Enter lower range: "))
upper = int(input("Enter upper range: "))

x = random.randint(lower, upper)

chances = 0
score = 0

while chances <3:
    guess = int(input("Enter your guess: "))

    if guess == x:
        print("CONGRAT'S")
        score += 1
        
        break
    elif guess < x:
        print("HAVE ONE MORE TRY")
        chances+=1
        score+=0
    else :
        print("HAVE ONE MORE TRY")
        chances+=1
        score+=0
if chances>=3:
 print("BETTER LUCK NEXT TIME")

print("YOUR SCORE IS:",score)    
    
    
