print("Welcome to my computer quiz!")

playing = input("Do you want to play? ")

if playing.lower() != "yes":  
    # .lower helps to convert the input into lower case
    quit()

print("Okay! Let's play :) ")
score = 0 

answer = input("What does CPU stand for? ")
if answer.lower() =="central processing unit":
    print("correct!")
    score += 1
else:
    print("incorrect")    
answer = input("What does GPU stand for? ")
if answer.lower() =="graphics processing unit":
    print("correct!")
    score += 1
else:
    print("incorrect")    
answer = input("What does RAM stand for? ")
if answer.lower() =="random access memory":
    print("correct!")
    score += 1
else:
    print("incorrect")    
answer = input("What does PSU stand for? ")
if answer.lower() =="power supply":
    print("correct!")
    score += 1
else:
    print("incorrect")  


print("You got " + str(score) + " questions correct")      
#you can only concatenate the similar 
# datatypes so we have converted score into string datatype


print("You got " + str(((score)/4)*100) + "% questions correct")    
