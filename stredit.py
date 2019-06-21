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

        self.op = None

    def operate(self,argument):
        switcher = {
            str({'operation': ' length (returns length of string)'}): print(len(self.message)),
            str({'operation': ' uppercase (returns all alphabets in uppercase)'}): print(self.message.upper()),
            str({'operation': ' capitalize (converts first character to Capital Letter)'}): print(self.message.capitalize()),
            str({'operation': ' lowercase (returns all alphabets in lowercase)'}): print(self.message.lower()),
            str({'operation': ' title case (returns a title cased string)'}): print(self.message.title()),
            str({'operation': ' all alphabets (checks if all characters are alphabets)'}): print(self.message.isalpha()),
            str({'operation': ' is lowercase (checks if all alphabets in a string are lowercase alphabets)'}): print(self.message.islower()),
            str({'operation': ' is uppercase (checks whether or not all characters in a string are uppercased)'}): print(self.message.isupper()),
            str({'operation': ' all numbers (checks if all characters in a string are numeric characters)'}): print(self.message.isnumeric()),
            str({'operation': ' all space (checks if there are only whitespace characters in the string)'}): print(self.message.isspace()),

        }
        return switcher.get(argument, "Invalid Operation")

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
        self.op = str((inquirer.prompt(questions)))
        return self.op


x = mod_str(5)
o = x.ques()
x.operate(o)

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
        o = x.ques()
        x.operate(o)
        opp()
    elif a!= "yes" or a!= "no":
        print("Invalid Input")
        opp()


opp()