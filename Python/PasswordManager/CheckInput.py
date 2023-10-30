class CheckInput:

    @staticmethod

    def getCorrectInput(userInput,listOfAnswers,question):
        while not (userInput in listOfAnswers):
            question = print(f"{question}\n")
            userInput=input(f"user: ")
        return userInput
