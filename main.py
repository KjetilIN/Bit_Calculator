import math
from typing import BinaryIO

## FUNCTION EXPLANATION 
#  1. isBitValue
#    - Checks if you the string contains integers
#  2. bitSolve4
#    - takes an string that is contains 4 binary numbers 
#    - returns the decimal value of the numbers 
#  3. endlessbit
#    - takes a string
#    - uses the formula to calculate the value of an infinte binary string 
#  4. convert4BitToHexi
#    - takes an string that is contains 4 binary numbers
#    - returns the hex value of the string 
#  5. BitToHex 
#    - first parameter takes the binary string 
#    - second parameter takes the binary size (8,16,32 or 64)






class Check():
    def isBitValue(givenStr): #Check if the input is good
        if((len(givenStr)<= 0) or (givenStr == "")): #not empty 
            #print("CHECK: Empty or too small")
            return False 
        elif not(givenStr.isdecimal()): #all the numbers are not zeros 
            return False
        else:
            return True
            

class Solve():
    def bitSolve4(givenStr):
        ans = 0
        if(Check.isBitValue(givenStr)): #DEBUG(kjetil): change to function that checks
            ans = 0
            for i in range(0, len(givenStr)):
                isZero = bool((givenStr[len(givenStr)-1-i]) == '0')
                isOne = bool(givenStr[len(givenStr)-1-i] == '1')
                if(isZero or isOne):
                    ans += int(givenStr[len(givenStr)-1-i])*math.pow(2,i)
                else: 
                    ans = -1
                    print("ONE OR MULTIPLE NON BINARY DIGITS")
                    break
            return ans 
        else: 
            print("ERORR: A none bit value was entered")
    
    def endlessBit(givenStr):
        valueBitString = 0
        for i in range(0,len(givenStr)):
            valueBitString += int(givenStr[len(givenStr)-1-i])*math.pow(2,i)
        return valueBitString
    
    def convert4BitToHexi(givenStr):
        result = ""
        if(Check.isBitValue(givenStr)):
            bitValue = Solve.bitSolve4(givenStr)
            if bitValue == -1:
                return -1
            else:
                #replaces the bitvalue with the hex symbol:
                if(bitValue == 0):
                    result+="0"
                elif(bitValue == 1):
                    result+="1"
                elif(bitValue == 2):
                    result+="2"
                elif(bitValue == 3):
                    result+="3"
                elif(bitValue == 4):
                    result+="4"
                elif(bitValue==5):
                    result+="5"
                elif(bitValue == 6):
                    result+="6"
                elif(bitValue == 7):
                    result+="7"
                elif(bitValue == 8):
                    result+="8"
                elif(bitValue == 9):
                    result+="9"
                elif(bitValue == 10):
                    result+="A"
                elif(bitValue == 11):
                    result+="B"
                elif(bitValue== 12):
                    result+="C"
                elif(bitValue == 13):
                    result+="D"
                elif(bitValue == 14):
                    result+="E"
                elif(bitValue == 15):
                    result+="F"
                else:
                    print("WRONG") #Ony happen if something went very wrong
                
                return result

    def BitToHex(givenStr,type): # only 8-16-32-64
        result = ""
        endVal = int(type / 4)
        for k in range(0, endVal):
            bitSting = ""
            for i in range(0,4):
                bitSting+= givenStr[i+k*4]
            hexi = Solve.convert4BitToHexi(bitSting)
            result += hexi
    
        return result
                



def main():
    ##Enter code her! Use functions made above 
    print(Solve.BitToHex(input("Enter bite: "),32))



#this runs the program 
if __name__ == "__main__":
    main()



