#!/usr/bin/env python3
with open('file.txt', 'r') as text:
    strings=text.readlines()
    for string in strings:
        string=string.strip()
        if string[0]=='?':
            question=string[1:]
            print('Question: ' + question)
            print('-----')
        elif string[0]=='-':
            wrong=string[1:]
            print('Wrong answer: ' +wrong)
            #print('-----')
        elif string[0]=='+':
            correct=string[1:]
            print('Correct Answer: ' +correct)
            #print('-----')
    