from flask import Flask, render_template, request
from openai import OpenAI
import os

app = Flask(__name__)

client = OpenAI(
    # This is the default and can be omitted
    api_key=os.environ.get("OPENAI_API_KEY"),
)

@app.route('/')
def home():
    return render_template("index.html")

# Route to display the form
@app.route('/ask', methods=['GET', 'POST'])
def ask():
    answer = ""
    if request.method == 'POST':
        user_input = request.form['user_input']
        answer = get_openai_answer(user_input)
    return render_template('ask.html', answer=answer)

def get_openai_answer(question):
    try:
        response = client.responses.create(
            model="gpt-4o",
            instructions="You are a friendly, respectful person who likes to chat.",
            input=question,
        )
        return response.output_text
    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
