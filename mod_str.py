import inquirer

class mod_str():
    """ class asks user for string input and operation they want to perform on string.the operation is performed.
    --Attributes--
    message: the message the user inputs
    op: the operation the user wants performed
    """
    message: str
    op: str
    maxlen: int

    def __init__(self, max_len: int) -> None:
        self.maxlen = max_len

        a = str(input("Input your message: "))
        while len(a) > self.maxlen:
            print("String more than length" ,self.maxlen, "not allowed!")
            a = str(input("Input your message: "))
        self.message = a

        self.op = self.ques()

    def operate(self, ):
        if self.op == {'operation': ' length (returns length of string)'}:
            return print(len(self.message))
        elif self.op == {'operation': ' uppercase (returns all alphabets in uppercase)'}:
            return print(self.message.upper())
        elif self.op == {'operation': ' capitalize (converts first character to Capital Letter)'}:
            return print(self.message.capitalize())
        elif self.op == {'operation': ' lowercase (returns all alphabets in lowercase)'}:
            return print(self.message.lower())
        elif self.op == {'operation': ' title case (returns a title cased string)'}:
            return print(self.message.title())
        elif self.op == {'operation': ' all alphabets (checks if all characters are alphabets)'}:
            return print(self.message.isalpha())
        elif self.op == {'operation': ' is lowercase (checks if all alphabets in a string are lowercase alphabets)'}:
            return print(self.message.islower())
        elif self.op == {'operation': ' is uppercase (checks whether or not all characters in a string are uppercased)'}:
            return print(self.message.isupper())
        elif self.op == {'operation': ' all numbers (checks if all characters in a string are numeric characters)'}:
            return print(self.message.isnumeric())
        elif self.op == {'operation': ' all space (checks if there are only whitespace characters in the string)'}:
            return print(self.message.isspace())
        else:
            return print("Invalid Operation")

    def ques(self) -> str:
        questions = [
            inquirer.List("operation",
                          message="What operation would you like to perform?: ",
                          choices=[" length (returns length of string)",
                                   " is uppercase (checks whether or not all characters in a string are uppercased)",
                                   " uppercase (returns all alphabets in uppercase)",
                                   " is lowercase (checks if all alphabets in a string are lowercase alphabets)",
                                   " lowercase (returns all alphabets in lowercase)",
                                   " capitalize (converts first character to Capital Letter)",
                                   " title case (returns a title cased string)",
                                   " all alphabets (checks if all characters are alphabets)",
                                   " all numbers (checks if all characters in a string are numeric characters)",
                                   " all space (checks if there are only whitespace characters in the string)"],
                          ),
        ]
        self.op = inquirer.prompt(questions)
        return self.op


x = mod_str(5)
x.operate()

def opp():
    question = [
        inquirer.List('answer',
                      message="would you like to perform another operation?: ",
                      choices=['yes', 'no'],
                      ),
    ]
    a = inquirer.prompt(question)
    if a=={'answer': 'no'} :
        return None
    if a =={'answer': 'yes'}:
        b = x.ques()
        x.operate()
        opp()
    elif a!= "yes" or a!= "no":
        print("Invalid Input")
        opp()


opp()
