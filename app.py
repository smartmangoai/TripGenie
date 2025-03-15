from flask import Flask, render_template, request
import openai
import os

app = Flask(__name__)

# Get the OpenAI API key from environment variables
openai_api_key = os.getenv("OPENAI_API_KEY")

@app.route('/')
def home():
    return render_template("index.html")

# Route to display the form
@app.route('/ask', methods=['GET', 'POST'])
def ask():
    if request.method == 'POST':
        user_input = request.form['user_input']
        # return f'You typed: {user_input}'  # Display the input after submission
        return f'You typed: {user_input} {openai_api_key} ok'  # Display the input after submission
    return render_template('ask.html')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
