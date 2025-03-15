from flask import Flask, render_template, request
import openai
import os

app = Flask(__name__)

# Get the OpenAI API key from environment variables
openai.api_key = os.getenv("OPENAI_API_KEY")

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
        response = openai.Completion.create(
            engine="text-davinci-003",  # Use your desired OpenAI model
            prompt=question,
            max_tokens=150
        )
        return response.choices[0].text.strip()
    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
