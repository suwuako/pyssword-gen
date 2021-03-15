#!/usr/bin/env python3
# 
# 
import random
import string

class GeneratePassword:
    def __init__(self):
        self.selection = string.ascii_letters
        self.password = ""
        
        # a SET (dynamic, unordered collection, without repeated elements)
        # storing indices that have already been modified and are therefore
        # RESERVED (these elements must not be overwritten!)
        self.reservedIndices = set()
        
    def generateString(self):
        for i in range(self.totalLen):
            indexValue = random.choice(string.ascii_lowercase)
            self.password += str(indexValue)
        
        print(f'original: \n{self.password}\n')
        
    def customize(self, selection, swapType, cap):
        i = 0
        while i < cap and len(self.reservedIndices) < len(self.password):
            index = random.randint(0, self.totalLen-1)
            
            if index not in self.reservedIndices:
                select = random.choice(selection)
                print(f'replacing {self.password[index]} (index {index}) with {select}')
                updated_password = self.password[0:index] + select + self.password[(index+1):]
                self.password = updated_password
                self.reservedIndices.add(index)
                i += 1
        
        if (i < cap): # len(self.reservedIndices) == len(self.password)):
            print(f'ERR -- could not finish applying {swapType} constraint!')
            print(f'    -- the number of reserved indices ({len(self.reservedIndices)}) apparently leaves no more room to make substitutions.')
            exit(1)
        else:
            print(f'after applying {swapType}:\n{self.password}')

    def getUserInput(self):
        self.totalLen = int(input('How long do u want the password to be? '))
        self.capsAmount = int(input('How many caps do you want? '))
        self.numberAmount = int(input('How many numbers do you want? '))
        self.symbolAmount = int(input('How many symbols do you want? '))
    
    def run(self):
        self.getUserInput()
        self.generateString()
        self.customize(string.digits, 'Numbers', self.capsAmount)
        self.customize(string.ascii_uppercase, 'Caps', self.numberAmount)
        self.customize(string.punctuation, 'Symbols', self.symbolAmount)
    
if __name__ == '__main__':
    gp = GeneratePassword()
    gp.run()

