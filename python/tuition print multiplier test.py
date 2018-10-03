antuit = 10000
count = 5
total = 0
x = 15
y = 16
print('UNDERGRADUATE TUITION FOR THE NEXT FIVE YEARS')
print('ACADEMIC YEAR\t\t      TUITION \t INCREASE')
print('-------------\t\t ------------ \t --------')
while count > 0:
    yearIncrease = antuit * 0.03
    antuit += yearIncrease
    total += yearIncrease
    x += 1
    y += 1
    count -=1
    print('20',x,'-',y, sep = '', end = '\t\t\t')
    print('   ', format(antuit, '9.2f'), end = '\t')
    print('  ', format(yearIncrease, '4.2f'))
print('TOTAL TUITION INCREASE\t\t\t', '', format(total, '7.2f'))
    
    
