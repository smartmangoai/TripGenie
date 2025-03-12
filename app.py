from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

# Route to display the form
@app.route('/ask.html', methods=['GET', 'POST'])
def ask():
    if request.method == 'POST':
        user_input = request.form['user_input']
        return f'You typed: {user_input}'  # Display the input after submission
    return render_template('ask.html.html')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
