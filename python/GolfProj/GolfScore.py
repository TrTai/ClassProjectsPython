#Golf Score Table and winner
#Program by Treye Chaney
#made 11/11/2016
#read scores input from keyboard by user or from 'golf.txt' file should one be provided and named as such, store
#and recall to display in table format as well as show the winner of the tournament

#define functions
#defining main function to call 'Inputinfo" and "displayReport' functions that will do the work
def main():
    inputInfo()
    displayReport()
#define the 'inputinfo' function that will read from the keyboard information and write it to 'golf.txt.'
def inputInfo():
    #ask user if they have new golfer information or want to read from the previously used data or another file named golf.txt in the same folder
    inputAgain = input('Any new golfer cards to input (y/n)(use n to use previously inputted data or read from preexisting \"golf.txt\"):')
    #ensure the input is 'y' or 'n' or their respective capital forms
    while inputAgain != 'y'and inputAgain != 'n' and inputAgain != 'Y' and inputAgain != 'N':
        inputAgain = input('''Please use 'y' or 'n'. \n Any new golfer info to input (y/n)''')
    #return to the main function to call displayReport if the user chooses to not input new information
    if inputAgain == 'n' or inputAgain == 'N':
        return
    #open or create 'golf.txt' for writing, will erase previous contents
    golfRecord = open('golf.txt', 'w')
    #begin input loop for golfer's information
    while inputAgain == 'y' or inputAgain == 'Y':
        #ask for the name of the golfer
        name = input('Name of Golfer?: ')
        #make sure no blank names are entered
        while name == '':
            name = input('''Please enter a Golfer's name: ''')
        #write the name to the file and write the following command on a new line
        golfRecord.write(name + '\n')
        #enter an infinite loop to ensure the value entered is a 3 digit integer number
        while True:
            try:
                #ask user for the Golfer's score
                score = int(input('''Golfer's score?: '''))
                #ensure input is in the 3 digit, non-negative range
                if 0 < score <= 999:
                    #write score to file and begin a new line
                    golfRecord.write(str(score)+ '\n')
                    #exit loop
                    break
                #if an input is an integer but is not 3 digit non-negative the user is warned then loops back to ask again
                else:
                    print('Please input score in 3-digit whole number format')
            #exception in the event an input is a non-number that will warn the user to input a proper number that will work with the program, then loop back to the input
            except ValueError:
                print('Please input score in a proper 3 digit whole number format')
        #ask user if they have any more golfers information to enter
        inputAgain = input('Do you have more golfer cards to enter? (y/n): ')
        #ensure the input is in 'y' or 'n' format or their respective capital forms
        while inputAgain != 'y' and inputAgain != 'n' and inputAgain != 'Y' and inputAgain != 'N':
            inputAgain = input('''Please input a 'y' or 'n': ''')
    #close the file
    golfRecord.close()
    #return to the main function to open the displayReport function
    return
#begin defining displayReport function
def displayReport():
    #open the golf.txt file for reading and assing to 'golfRecord'
    golfRecord = open('golf.txt','r')
    #open an empty list 'scorelist' to store scores
    scorelist = []
    #open empty list 'namelist' to store names
    namelist = []
    #ask user for the year of the tournament for the table
    YEAR = input('Year of event: ')
    #ask user for the month
    MONTH = input('Month of event: ')
    #enter loop to ensure date is a number
    while True:
        try:
            #ask user for the start date for the event
            dStart = int(input('Start day: '))
            #ensure the date entered falls into calendar days
            while dStart < 1 or dStart > 31:
                dStart = int(input('Please put in the first day of the Tournament in number format: '))
            #exit loop when apropriate value is reached
            if dStart > 0 and dStart < 32:
                break
        #handles exceptions if a non integer string is put into the date
        except ValueError:
            print('Please input using numeric date')
    #enter another loop to ensure end date is a number
    while True:
        try:
            #ask user for the end date of the tournament
            dEnd = int(input('End Day: '))
            #ensure the end date is within calendar days and a date past the start date
            while dEnd < dStart or dEnd < 1 or dEnd > 31:
                dEnd = int(input('Please input the last day of the Tournament in number format: '))
            #exit loop when apropriate date value is reached
            if dEnd > 0 and dEnd < 32:
                break
        #handle exceptions with a warning to input date as a number in the event a non-numeric string is entered.
        except ValueError:
            print('Please input using numeric date')        
    #print header of table with data inputted by user for the dates
    print('\tSPRINGFORK AMATEUR GOLD CLUB')
    print('TOURNAMENT: WEEKEND OF ', dStart , '-', dEnd , MONTH, YEAR)
    print('GOLFER NAME\t\t\t\t SCORE')
    print('------------------------------\t\t-------')
    #read first name from the golfRecord
    name = golfRecord.readline()
    #repeat loop as long as the end of the file (blank string) is not detected
    while name != '':
        #assigns the following line to the score
        score = golfRecord.readline()
        #removes newline character from 'name' 
        name = name.rstrip('\n')
        #removes newline character from 'score'
        score = score.rstrip('\n')
        #converts score to an integer value
        score = int(score)
        #adds the current 'name' to list 'namelist' to pull from later, adds all golfers from files
        namelist.append(name)
        #adds the current 'score' to list 'scorelist' to pull from later, remains in same place in the list(index number) as the name corresponding to it
        scorelist.append(score)
        #calculate number of spaces to keep all numbers and names aligned in table
        formatlen = 44 - len(name)
        #prints each player's name and score in table format, name on the left and score on the right side under their respective headers
        print(name ,' ' * formatlen, format(score, '3d') , sep = '', end = '\n')
        #read next name from the file golfRecord
        name = golfRecord.readline()
    #find the lowest score amongst the competitors from 'scorelist'
    minscore = min(scorelist)
    #find the index number of that score
    index = scorelist.index(minscore)
    #print the line Winner is x with score y, x being the name of the golfer and y being the score pulled from the list of all golfers shown on the table
    print('Winner is', namelist[index], 'with score', minscore)
    #close 'golfRecord' (golf.txt)
    golfRecord.close()
    return
    
#call main function to preform tasks    
main()    
input("Press Enter to finish")
