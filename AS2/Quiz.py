#!/usr/bin/env python3
import random

def getQuestions(file):
    questions=[]
    this=None
    with open(file, 'r') as text:
        strings=text.readlines()
        for string in strings:
            string=string.strip()
            if string[0]=='?':
                this=[string[1:],[],None]
                questions.append(this)

                # print('-----')
            elif string[0]=='-':
                this[1].append((string[1:], False))
                # wrong=string[1:]
                # print('Wrong answer: ' +wrong)
                #print('-----')
            elif string[0]=='+':
                this[1].append((string[1:], True))
                this[2] = len(this[1]) - 1
                # correct=string[1:]
                # print('Correct Answer: ' +correct)
                #print('-----')
    return questions
    
def getUserInput(questions):
    for q in questions:
        print('Question: ' + q[0])
        for i in range(len(q[1])):
            answer = q[1][i][0]
            print(f"{chr(65+i)}) {answer}")

        userinput = input("Your answer: ")
        index = ord(userinput.upper()) - 65
        if index == q[2]:
            print("Correct!")
        else:
            print(f"Incorrect. The correct answer is: {chr(65 + q[2])}")

def main():
    questions = getQuestions('file.txt')
    getUserInput(questions)

if __name__ == "__main__":
    main()
    