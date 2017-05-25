#Scott Hansford
#CSC110
#HW#6 - Tornadoes in Alabama
def main():
    try:
        print("Welcome to the Tornado data program!")
        print("*"*30)
        fileName = input("What file would you like to use?: ")
        readFile = open(fileName,'r')
        outfile = open('REPORT-'+fileName,'w') #open new output file with REPORT prefix
        line = readFile.readline()
        firstYear = int(line)

        #Tornado
        minTor = 1000
        maxTor = 0
        maxTor_Year = 0
        minYear_Tor = 1000
        totalTor = 0
        avTor = 0

        #Fatalities
        minFat = 1000
        maxFat = 0
        minFat_Year = 0
        maxFat_Year = 0
        totalFat = 0
        avFat = 0

        #Injuries
        minInj = 1000
        maxInj = 0
        minInj_Year = 0
        maxInj_Year = 0
        totalInj = 0
        avInj = 0
        countofyears = 0
        while line != "":
#Tornados
            countofyears += 1 #stuggled with the averaging section until I got help with this part
            lastYear = int(line)
            tornado = int(readFile.readline())   #Tornados
            if tornado > maxTor:
                maxTor = tornado
                maxTor_Year = lastYear
            elif tornado < minTor:
                minTor = tornado
                minYear_Tor = lastYear
            totalTor+=tornado

#Fatalities
            fatal = int(readFile.readline())
            if fatal > maxFat:
                maxFat = fatal
                maxFat_Year = lastYear
            elif fatal < minFat:
                minFat = fatal
                minFat_Year = lastYear
            totalFat+=fatal
#Injuries
            injuries = int(readFile.readline())
            if injuries > minInj:
                maxInj = injuries
                maxInj_Year = lastYear
            elif injuries < minInj:
                minInj = injuries
                minInj_Year = lastYear
            totalInj+=injuries
            line = readFile.readline()
        avTor = int(totalTor/countofyears)
        avInj = int(totalInj/countofyears)
        avFat = int(totalFat/countofyears)
        print("For period from",firstYear,"to",lastYear,"in the State of Alabama were:")
        print(totalTor, "is your total tornados")
        print(totalFat,"is your total fatalities")
        print(totalInj, "is your total injuries:")
        print("*"*30)
        #Average tornadoes, fatalities, and injuries
        print(avTor,"Is your average tornadoes")
        print(avFat,"is your avverage fatalities")
        print(avInj, "Is your average injuries")
        print("*"*30)
        #print max and min tornados
        print(minTor,"is your Minimum Tornadoes in,",minYear_Tor)
        print(maxTor,"is your Maximum Tornadoes in,",maxTor_Year)
        print("*"*30)
        #print max and min fatalities
        print(maxFat,"Is your minimum Fatalities in,",maxFat_Year)
        print(minFat,"Is your max Fatalities in,",minFat_Year)
        print("*"*30)
        #print max and min injuries
        print(totalInj,"Is your maximum Injuries,",maxInj_Year)
        print(minInj,"Is your minimum Injuries in year,",minInj_Year)
        print("You have finished using:",fileName)
        
        outfile.write(str(firstYear) + " First year"'\n')
        outfile.write(str(lastYear) + " End year"'\n')
        outfile.write(str(totalFat) + " :Total Fatalities"'\n')
        outfile.write(str(minFat) + " :Minimum Fatalities"'\n')
        outfile.write(str(totalTor)+ " is your total tornados"'\n')
        outfile.write(str(totalFat)+ " is your total fatalities"'\n')
        outfile.write(str(avTor)+ " is your average tornadoes"'\n')
        outfile.write(str(avFat)+ " is your avverage fatalities"'\n')
        outfile.write(str(avInj)+ " is your average injuries"'\n')
        outfile.write(str(minTor)+ " is your Minimum Tornadoes in,"'\n')
        outfile.write(str(maxTor)+ " is your Maximum Tornadoes in,"'\n')
        outfile.write(str(maxFat)+ " is your minimum Fatalities in,"'\n')
        outfile.write(str(minFat)+ " is your max Fatalities in,"'\n')
        outfile.write(str(totalInj)+ " is your maximum Injuries,"'\n')
        outfile.write(str(minInj)+ " is your minimum Injuries in year,"'\n')


    #exception handling
    except ValueError as err:
        print(err)
    except IOError as err:
        print(err)
    except TypeError as err:
        print(err)
        outfile.close()
        readFile.close()
        
main()


#learned how to concat a filename
#struggling with looping through to properly display the data from the file.
#I can display the first set of numbers properly but am lacking the range of years and the
#proper grouping of the data sets.

#Is there a way to write to the consol and print to a file on the same line?
