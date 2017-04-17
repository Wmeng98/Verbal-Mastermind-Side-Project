## Verbal Mastermind!
import check
import math

## constant definitions...
verification_message = "Exact: {0}, Other: {1}"
incorrect_message = "Your guess contains an incorrect number of characters."
keyword_message = "The keyword has {0} characters."
congratulations_message = "Congratulations! "
correct_keyword_message = "The correct keyword was {0}."
guess_message = "Please enter a guess: "

## ex_ot(x,y) consumes two strings x and y of equal length and produces a
##  list of 2 numbers the firt telling how many elements within each string
##  are the same for both strings in the same position and the second tells
##  of number of characters in y exlcuding those already correct that are in 
##  x but just not in correct position.
## ex_ot: Str Str -> (list Nat Nat)

def ex_ot(x,y):
    exact = 0
    other = 0
    listx = list(x)
    listy = list(y)
    new_listx = []
    new_listy = []
      
    for i in range(len(listx)):
        if listx[i] == listy[i]:
            exact = exact + 1
        else:
            new_listx.append(listx[i])
            new_listy.append(listy[i])
    for j in new_listy.copy():
        if j in new_listx.copy():
            other = other + 1
            new_listx.remove(j)
            new_listy.remove(j)
    ans = [exact,other]
    return ans

## verbal_mastermind(keyword): consumes keyword and runs a version of thepopular
##  game mastermind. program prompts user to input string and prints result of
##  how close user was to keyword until user terminates program or guesses right
## Effects: prints details on game through loop
##          reads in user guess on loop until program terminates
## verbal_mastermind: Str -> None
## requires: keyword length between 2-100 and keyword in all lowercase
## Examples:
## If verbal_mastermind("Harambe") is called, descriptions are printed to screen
##  prompting user to input a guess, if user inputs 'DDonald' program prints 
##  to screen saying guess is too long or short, if user then inputs 'Harambe',
##  program prints congratualtions and program terminates
## If verbal_mastermind('hacksfordayz') is called and user inputs '!quit', then
##  program prints termination description and program terminates

def verbal_mastermind(keyword):
    print(keyword_message.format(len(keyword)))
    guess = ''
    while guess != keyword:
        guess = input(guess_message)
        if guess == '!quit':
            print(correct_keyword_message.format(keyword))
            return None
        if (len(guess) > len(keyword)) or (len(guess) < len(keyword)):
            print(incorrect_message)
            print(keyword_message.format(len(keyword)))
        if len(guess) == len(keyword):
            if guess == keyword:
                print(congratulations_message+correct_keyword_message.format(keyword))
            elif guess != keyword:
                print(verification_message.format(ex_ot(keyword,guess)[0],ex_ot(keyword,guess)[1]))

## Tests:
##No possible test for which body executes 0 times
## Q3T1 Test for which body executes 1 time
check.set_input(['Shrek4life'])
check.set_screen('inital descriptions printed when function called with keyword and when input entered program congratulates user with congratulations message printed on seperate line')
check.expect('Q3T1',verbal_mastermind('Shrek4life'),None)
## Q3T2 Test for which body executes a maximum number of times (shortened for time purposes)
check.set_input(['DDonald','Harambe'])
check.set_screen('inital descriptions printed when function called with keyword and when input entered program prints Exact and other statement line and proceeds to prompt user enter another guess, when user enters Harambe, program congratulates user with print on seperate sentence and program terminates...')
check.expect('Q3T2',verbal_mastermind('Harambe'),None)
## Q3T3 Test for which body executes a typical number of times (user inputs !quit)
check.set_input(['!quit'])
check.set_screen('inital descriptions printed when function called with keyword and when input entered program prints the quit statements and terminates')
check.expect('Q3T3',verbal_mastermind('hacksfordayz'),None)
## Q3T4 Test for keyword restriction of 2 (minimum)
check.set_input(['laksd','asd','bb','ab','aa'])
check.set_screen('inital descriptions printed when function called with keyword and when input entered program prints too long, then as user input gets smaller program prints Exact other statement until user finally inputs correctly to terminate program')
check.expect('Q3T4',verbal_mastermind('aa'),None)
## Q3T5 Test for keyword restriction of 4
check.set_input(['dfgh','BOSS'])
check.set_screen('inital descriptions printed when function called with keyword and when input entered program prints exact/other statement and then when user inputs again correctly program prints congratulation statment to termiante')
check.expect('Q3T5',verbal_mastermind('BOSS'),None)



            
                
                
                




    

