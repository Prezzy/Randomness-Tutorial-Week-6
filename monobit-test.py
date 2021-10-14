import sys
import math

def main():

    with open(sys.argv[1]) as f:

        alpha = float(sys.argv[2])

        randnumset = f.readlines()

        numtests = len(randnumset)

        testresults = []

        for num in randnumset:
            S = 0
            num = num.rstrip('\n')
            num = bin(int(num,16))
            length = len(num[2:])

            for i in num[2:]:
                if i == '1':
                    S += 1
                elif i == '0':
                    S += -1

            teststat = abs(S)/math.sqrt(length)

            pvalue = teststat/math.sqrt(2)

            if pvalue < alpha:
                testresults.append(0)
            else:
                testresults.append(1)

    
        print(f"{sum(testresults)} out of {numtests} passed test: {(sum(testresults)/(numtests))*100}")

        
main()






    




