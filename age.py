year = int(input(year_input))

if(year<=1600):
    print("")

count=0

for i in range(year-1600):
    if(year/4):
        count = count +1
    if(year/100 )