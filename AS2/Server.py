#!/usr/bin/env python3 
import socket
import telnetlib
import random
import os

def playSound():
    os.system('mpg123 yay-6326.mp3')


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

def evaluateQuiz(connection):
    #pygame.mixer.init()
    #sound = pygame.mixer.Sound('score_sound.wav')

    GREEN = '\033[92m'  
    RED = '\033[91m'    
    RESET = '\033[0m'
    questions = getQuestions('file.txt')
    score=0

        
    while True:
        question = random.choice(questions)
        connection.sendall(('Question: ' + question[0] + '\n').encode())
        for i, (answer, _) in enumerate(question[1]):
            connection.sendall((f"{chr(65+i)}) {answer}\n").encode())

        user_answer = connection.recv(1024).decode().strip()
        user_index = ord(user_answer.upper()) - 65
        if user_index == question[2]: 
            connection.sendall((GREEN + "Correct! \n" + RESET).encode())
            score += 1
            playSound()
        else:
            connection.sendall((RED +f"Incorrect. The correct answer is: {chr(65 + question[2])}\n" + RESET).encode())
        
        # Ask the user if they want to continue
        connection.sendall("Do you want to continue? (yes/no): ".encode())

        continue_answer = connection.recv(1024).decode().strip()
        if continue_answer.lower() != 'yes':
            break
    # Display the user's score
    connection.sendall(f"Your score: {score}\n".encode())
    


#Listening for clients


def main():
    adrs=('localhost', 55555)
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as socketServer:
        socketServer.bind(adrs)
        socketServer.listen()
        print(" server listening on port 55555")

        while True:
            connection, address=socketServer.accept()
            print(" server accepted on client address: ", address)
            try:
                    evaluateQuiz(connection)
            except EOFError:
                    print("CLIENT LOST")
            finally:
                    connection.close()
                    print("CONNECTION CLOSED")

if __name__ == "__main__":
    main()



