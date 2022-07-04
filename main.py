name=input("what is your name ")
print("hi",name)
age=input("what is your age ")
print("oh your age is ",age)
print("my age is 13")
print("oh sorry I don't tell my name 😅")
print("my name is asbin ")
print("are you fine ")
fineornot=input( "i hope you are fine answer in yes or  no ")
if 'yes'in fineornot :
  print ("I'm fine also") 
else:
      print ("oh bad")
print("let's play game")
print("Welcome to AskPython Quiz")
answer=input('Are you ready to play the Quiz ? (yes/no) :')
score=0
total_questions=3
 
if answer.lower()=='yes':
    answer=input('Question 1: What is easiest language ')
    if answer.lower()=='python':
        score += 1
        print('correct')
    else:
        print('Wrong Answer :(')
 
 
    answer=input('Question 2: does this made python or not Guido van Rossum ')
    if answer.lower()=='yes':
        score += 1
        print('correct')
    else:
        print('why follow me now :(')
 
    answer=input('Question 3: what is my name ')
    if answer.lower()=='asbin':
        score += 1
        print('correct')
    else:
        print('Wrong Answer :(')
 
print('Thankyou for Playing this small quiz game, you attempted',score,"questions correctly!")
mark=(score/total_questions)*100
print('Marks obtained:',mark)
print('game end ')
print ("do you like the game")
