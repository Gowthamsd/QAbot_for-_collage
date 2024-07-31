from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

class AdmissionChatbot:
    def __init__(self):
        self.context = {}
        self.responses = {
            "admission procedure": "The admission procedure involves filling out an application form, submitting required documents, and attending an interview.",
            "admission requirements": "You need to have completed high school with a minimum GPA of 3.0, and provide standardized test scores such as SAT or ACT.",
            "application deadline": "The application deadline is March 31st.",
        }

    def remember(self, key, value):
        self.context[key] = value

    def recall(self, key):
        return self.context.get(key, None)

    def greet(self):
        return "Hello! How can I assist you with your college admission queries today?"

    def respond_to_question(self, question):
        for key in self.responses:
            if key in question.lower():
                return self.responses[key]
        return "I'm sorry, I don't have information on that topic. Can you please specify your question?"

    def farewell(self):
        return "Goodbye! Feel free to reach out if you have more questions about college admissions."

    def handle_error(self, input_text):
        return "I'm sorry, I didn't understand that. Can you please rephrase?"

chatbot = AdmissionChatbot()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get('message')
    response = chatbot.respond_to_question(user_input)
    if response == "I'm sorry, I don't have information on that topic. Can you please specify your question?":
        response = chatbot.handle_error(user_input)
    return jsonify({"response": response})

if __name__ == '__main__':
    app.run(debug=True)
