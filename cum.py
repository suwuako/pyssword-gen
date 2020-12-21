import random
import string

class generatePassword:
    def __init__(self):
        self.selection = string.ascii_letters
        self.password = []
        self.rngBag = []
        
        
        
    def display(self):
        self.displayString = ''
        
        for i in self.password:
            self.displayString += str(i)
    
    def generateString(self):
        for i in range(self.totalLen):
            indexValue = random.choice(string.ascii_lowercase)
            self.password.append(indexValue)
        
        self.display()
        
        print(f'original: \n{self.displayString}\n')
        
    def customize(self, selection, swapType, cap):
        self.i = 0
        while self.i != cap:
            index = random.randint(0, self.totalLen-1)
            
            if index not in self.rngBag:
                select = random.choice(selection)
                print(f'replacing {self.password[index]} (index {index}) with {select}')
                self.password[index] = select
                self.rngBag.append(index)
                self.i += 1
            
        
        self.display()
        print(f'after {swapType}:\n{self.displayString}')

    def getUserInput(self):
        self.totalLen = int(input('How long do u want the password to be? '))
        self.capsAmount = int(input('How many caps do u want? '))
        self.numberAmount = int(input('How many numbers do u want? '))
        self.symbolAmount = int(input('How many symbols do u want? '))
    
    def run(self):
        self.getUserInput()
        self.generateString()
        self.customize(string.digits, 'Numbers', self.capsAmount)
        self.customize(string.ascii_uppercase, 'Caps', self.numberAmount)
        self.customize(string.punctuation, 'Symbols', self.symbolAmount)

        
    
if __name__ == '__main__':
    gp = generatePassword()
    gp.run()
