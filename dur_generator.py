'''This script is for generating MMN stimuli
    standard: 100
    deviant: 200
    std:dev = 80:20 '''

import random
numlist = []
dev_counter = 0
j = True
for i in range(1500):
    i = '0'
    numlist.append(i) #create a list of 1500 '0's

while j == True:
    index = random.randint(1,1498) #randomly generate a number bt 1 and 1498
    if numlist[index] == '0':
        if numlist[index-1] != '2' and numlist[index+1] != '2':
            numlist[index] = '2'
            dev_counter = dev_counter + 1
            if dev_counter == 300:
                j = False
                break
            else:
                continue
        else:
            continue
    else:
        continue

for index2 in range(1500):
    if numlist[index2] == '0':
        numlist[index2] = '1'

strlist = []
for number in numlist:
    outnum = str(number)
    strlist.append(outnum)

output = ','.join(strlist)
outwrite = open('out_dur.txt','w')
outwrite.write(output)
outwrite.close()
