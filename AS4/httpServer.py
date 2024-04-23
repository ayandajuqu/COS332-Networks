import socket
import random

class QuizServer:
    def __init__(self):
        self.session = {}

    def get_questions(self, file):
        questions = []
        this = None
        with open(file, 'r') as text:
            strings = text.readlines()
            for string in strings:
                string = string.strip()
                if string[0] == '?':
                    this = [string[1:], [], None]
                    questions.append(this)
                elif string[0] == '-':
                    this[1].append((string[1:], False))
                elif string[0] == '+':
                    this[1].append((string[1:], True))
                    this[2] = len(this[1]) - 1
            if this[2] is None:
                this[1].append(("None of the above", True))
                this[2] = len(this[1]) - 1
        return questions

    def evaluate_quiz(self, request):
        questions = self.get_questions('file.txt')

        # Retrieve the current question and score from the session
        question = self.session.get('question')
        score = self.session.get('score', 0)
        
        if not question:
            # If there's no question in the session, choose a new random question
            question = random.choice(questions)
            self.session['question'] = question
        
        response = 'HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n'
        response += '<html><body>'
        
        if request.startswith('GET'):
            response += f'<h1>Question: {question[0]}</h1>'
            response += '<form method="POST">'
            for i, (answer, _) in enumerate(question[1]):
                response += f'<input type="radio" name="answer" value="{i}">{answer}<br>'
            response += '<input type="submit" value="Submit">'
            response += '</form>'
        elif request.startswith('POST'):
            # Parse the request body to extract form data
            content_length_index = request.find('Content-Length:')
            blank_line_index = request.find('\r\n\r\n')
            if content_length_index != -1 and blank_line_index != -1:
                content_length_line = request[content_length_index:blank_line_index]
                content_length = int(content_length_line.split()[1])
                request_body = request[blank_line_index + 4:]
                form_data = request_body[:content_length]
                user_answer_index = int(form_data.split('=')[1])
                
                if user_answer_index == question[2]:
                    response += '<h1>Correct!</h1>'
                    score += 1
                else:
                    response += f'<h1>Incorrect. The correct answer is: {chr(65 + question[2])}</h1>'
            
            # Choose a new random question for the next round
            question = random.choice(questions)
            self.session['question'] = question
        
        # Display a "Next" link to fetch a new question
        response += '<a href="/">Next Question</a>'
        
        # Update the session score
        self.session['score'] = score
        
        # Display the total score
        response += f'<h2>Your score: {score}</h2>'
        response += '</body></html>'
        return response.encode()

    def main(self):
        host = 'localhost'
        port = 55555

        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
            server_socket.bind((host, port))
            server_socket.listen()
            print(f"Server listening on {host}:{port}")

            while True:
                client_socket, client_address = server_socket.accept()
                print(f"Connection accepted from {client_address}")

                with client_socket:
                    request_data = client_socket.recv(1024).decode()
                    print(f"Request received:\n{request_data}")

                    if request_data:
                        response = self.evaluate_quiz(request_data)
                        client_socket.sendall(response)
                    else:
                        print("Empty req received")


if __name__ == "__main__":
    server = QuizServer()
    server.main()
