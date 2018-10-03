#Tuition 5-year projection
#By Treye Chaney
#date: 10-20-2016
#calculate and show tuition for the next 5 years of a college students tuitions and the increase per year as well as overall increase from starting tuition.


#program start
#Variable for subsequent checks and to begin loop
runAgain = 'yes'
#repeat as long as the user types 'yes' at the end of program
while runAgain == 'Yes' or runAgain == 'yes' or runAgain == 'YES' or runAgain == 'yES' or runAgain == 'yeS' or runAgain == 'YEs' or runAgain =='yEs' or runAgain == 'y' or runAgain == 'Y' or runAgain == 'YeS':
    #ask user for type of residency in form of 'I' 'O' or 'G' or their lowercase forms
    residency = input("""Type of Residency? Input "I" for in-state, "O" for Out-of-state, or "G" for Graduate: """)
    #initialize total variable
    totalIncrease = 0
    #initialize academic year beginning
    YearStart = 15
    #initialize academic year end
    YearEnd = 16
    #initialize count for calculation and print loop
    count = 5
    #assign "AnTuition" for starting annual tuition according to input
    if residency == "I" or residency == "i":
        AnTuition = 10000
    elif residency == "O" or residency == "o":
        AnTuition = 24000
    elif residency == "G" or residency == "g":
        AnTuition = 40000
    #if user enters a string that is not from the listed (I,i,O,o,G,g) repeat asking until an appropriate input is given
    else:
        while residency != "I" and residency != "i" and residency != "O" and residency != "o" and residency != "G" and residency != "g":
            residency = input("""Please input a provided answer. "I" for in-state, "O" for out-of-state, or "G" for Graduate: """)
            if residency == "I" or residency == "i":
                AnTuition = 10000
            elif residency == "O" or residency == "o":
                AnTuition = 24000
            elif residency == "G" or residency == "g":
                AnTuition = 40000
            else:
                residency = 0
    #determine header based off input            
    if residency == "G" or residency == "g":
        print('GRADUATE TUITION FOR THE NEXT FIVE YEARS')
    else:
        print('UNDERGRADUATE TUITION FOR THE NEXT FIVE YEARS')
    #Table header
    print('ACADEMIC YEAR\t\t      TUITION \t INCREASE')
    print('-------------\t\t ------------ \t --------')
    #calculate each years cost based off the initial value
    #repeat calculations and print exactly 5 times (as long as count is 5)
    while count > 0:
        #find 3% increase for next year
        yearIncrease = AnTuition * 0.03
        #assign new years tuition to AnTuition
        AnTuition += yearIncrease
        #accumulate total change year by year
        totalIncrease += yearIncrease
        #add one year to start year
        YearStart += 1
        #add one year to end year
        YearEnd += 1
        #reduce count
        count -=1
        #print year column
        print('20',YearStart,'-',YearEnd, sep = '', end = '\t\t\t')
        #print the year's annual tuition
        print('   ', format(AnTuition, '9.2f'), end = '\t')
        #print increase year to year
        print('  ', format(yearIncrease, '4.2f'))
    #if condition to ensure proper alignment of table and display the total change over all years.
    if residency == "G" or residency == "g":
        print('TOTAL TUITION INCREASE\t\t', '', format(totalIncrease, '16.2f'))
    else:
        print('TOTAL TUITION INCREASE\t\t', '', format(totalIncrease, '15.2f'))
    #ask user if they would like to check another residency type (or run again)
    runAgain = input('Would you like to check another tuition? Yes or No: ')
    #ask again if input is not a yes or no (or 'y' or 'n') and variants of capitalization.
    #arguably more trouble than it was worth to make work using what we know, but if I was going this far didn't want the user experience ruined by being picky on inputs.
    while runAgain != 'Yes' and runAgain != 'yes' and runAgain != 'YES' and runAgain != 'yES' and runAgain != 'yeS' and runAgain != 'YEs' and runAgain !='yEs' and runAgain != 'YeS' and runAgain != 'y' and runAgain != 'Y' and runAgain != 'No' and runAgain != 'no' and runAgain != 'NO' and runAgain != 'oN'and runAgain != 'n' and runAgain != 'N':
        runAgain = input("""Please enter 'yes' or 'no'. Would you like to check another tuition?""")
#Thanks and goodbye user!
print('Thank you and goodbye!')
#end program


