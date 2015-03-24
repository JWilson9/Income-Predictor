################################################
#                                              #
#                   FUNCTIONS                  #
################################################
#### NUMBER OF LINES IN THE FILE#####
def number_of_people(num):
    for line in file_txt:##### goes through each file line by line until the end of the file
        num+=1
        array.append( line )### appending the linr to the array
    return(num)##returning number of line

#####Getting the average of all the int attributes in the line 
def averageInt(seventy_percent, TotalFile,n):
    i=0
    countUnder = 0
    countOver = 0
    totalUnder = 0
    totalOver = 0
    median=0    
    while(i<seventy_percent):###while i is smaller than the 70% of the file
        words = TotalFile[i].split(', ')
        if(TotalFile[i].find('<=50K') != -1):####### if the line founds <=50k increments the counter also adds ints together
            totalUnder = totalUnder + int(words[n])
            countUnder += 1
        else:
            totalOver = totalOver + int(words[n])#######else if not <=50k increments  50k same rule applies
            countOver += 1
        i+=1
    totalOver = round(totalOver/countOver)######rounding them up total ages divided by the ammount of times it appeared
    totalUnder = round(totalUnder/countUnder)#######same but for the under 50K
    median = (totalUnder + totalOver)/2 #####getting the median add two together and divide by 2
    return(int(median))
########## CALCULATE WEGHTS FOR THE ATTRIBUTE STRINGS ####################
def weights(seventy_percent,TotalFile,n):
    i=0
    weightDictionary = {} ######creating a empty weight dictionary
    att_array = [] ###creating an array 
    
    while(i < seventy_percent):###### while i smaller then 70%
        words = TotalFile[i].split(', ') ##### the 15 attributes in the line split by (, )
        attribute=words[n] ######attribute is = to one of thouse words(attributes)
        if(attribute in weightDictionary): ######## if the attribute is in the dictionary
            weightDictionary[attribute]+=1 #######increments
        else:
            weightDictionary[attribute]=1 ##### adds 1 to attribute
            att_array.append(attribute) ########attribute is is appended to the attribute array
        i+=1

    i=0
    for att_array[i] in weightDictionary: ###### For each attibute array[i] e.g male in dictionary
        weightDictionary[att_array[i]] = weightDictionary[att_array[i]]/seventy_percent ####### giving attribute value / 70%
    return(weightDictionary)
############ IF ATTRIBUTES ARE ABOVE OR BELOW 50K ##########
def aboveRbelow(seventy_percent,arry,n, WeightDictionary):
    i = 0
    numOver = 0
    numUnder = 0
    countOver = 0
    countUnder = 0
    MidPointDict = {} # make dictionary midpoint
    
    while(i < seventy_percent):
            words = arry[i].split(', ')
            attribute=words[n]
            if(array[i].find(">50K") != -1):
               numOver = numOver + WeightDictionary[attribute] ###### giving weight for above + count times
               countOver += 1
            else:
                numUnder = numUnder + WeightDictionary[attribute]########weight for below
                countUnder += 1
            i += 1
    numOver = numOver/countOver
    numUnder = numUnder/countUnder
    MidPointDict = (numOver + numUnder)/2 ########getting midpoint between under + over
    return(MidPointDict)
#####################################################################
#                                                                   #
#                               MAIN                                #
#####################################################################
file_txt = open('sampledata.txt','r')
NoOfPeople = 0
array = [] ##### array for the total file
NoOfPeople = number_of_people(NoOfPeople) ###calling function to get total number of people

###########          70%        ######
seventy_percent = int(NoOfPeople * .7)
########################################
#                                      #
#            INTS                      #
#                                      #
########################################
### average age
n=0 ###poisiton 
medianAge = averageInt(seventy_percent,array,n)
### education number
n=4
educationNumber = averageInt(seventy_percent,array,n)
#####capital gain
n=10
capGain= averageInt(seventy_percent,array,n)
#####capital loss
n=11
capLoss= averageInt(seventy_percent,array,n)
#####hours
n=12
hours= averageInt(seventy_percent,array,n)
##################################
#                                #
#            STRINGS             #
#                                #
##################################
###workclass
n=1
workClassDict = weights(seventy_percent,array,n)
MidWork = aboveRbelow(seventy_percent,array,n, workClassDict)
######marriage
n=5
marriageDict = weights(seventy_percent,array,n)
MidMar = aboveRbelow(seventy_percent,array,n, marriageDict)
######occupation#################################
n=6
occupationDict = weights(seventy_percent,array,n)
MidOcc = aboveRbelow(seventy_percent,array,n, occupationDict)
#######relatonship###################################
n=7
relDict = weights(seventy_percent,array,n)
MidRel = aboveRbelow(seventy_percent,array,n, relDict)
####### Race#########################
n=8
raceDict = weights(seventy_percent,array,n)
MidRace = aboveRbelow(seventy_percent,array,n, raceDict)
######gender########################################
n=9
genderDict = weights(seventy_percent,array,n)
MidGen = aboveRbelow(seventy_percent,array,n, genderDict)
#############################################################
##                                                         ##
##                    TESTING                              ##
##                                                         ##
#############################################################
correct = 0
overall = 0
count = 0
while(seventy_percent < NoOfPeople ): ####70% < 100%
    under = 0
    over = 0
    att = array[seventy_percent].split(', ') #the attribute = the array of 70%
    if(int(att[0]) > medianAge): ### is attribute at position 0 bigger then median age
        over += 1 ######increments over
    else:
        under += 1 ######increments under
        
    if(int(att[4]) > educationNumber):
        over += 1
    else:
        under += 1
        
    if(int(att[10]) > capGain):
        over += 1
    else:
        under += 1

    if(int(att[11]) > capLoss):
        over += 1
    else:
        under += 1
        
    if(int(att[12]) > hours):
        over += 1
    else:
        under += 1

    if(float(workClassDict[att[1]]) < MidWork): ## if att at poistion 1 smaller then Middle point work
        over += 1 ####increments over
    else:
        under += 1 ####increments under

    if(float(marriageDict[att[5]]) > MidMar):
        over += 1
    else:
        under += 1

    if(float(occupationDict[att[6]]) > MidOcc):
        over += 1
    else:
        under += 1

    if(float(relDict[att[7]]) > MidRel):
        over += 1
    else:
        under += 1

    if(float(raceDict[att[8]]) > MidRace):
        over += 1
    else:
        under += 1

    if(float(genderDict[att[9]]) > MidGen):
        over += 1
    else:
        under += 1

    if(over > under):
        answer = '>50K'
    else:
        answer = '<=50K'
            
    if(array[seventy_percent].find(answer) != -1):
        correct += 1
    else:
        correct += 0
        
    seventy_percent += 1 ## increments the 70% 
    count += 1
    overall = round((correct / count)*100) #### get accuracy 
print("accuracy",overall,"%")  
