from flask import Flask, render_template, request, session
import openai

app = Flask(__name__)
app.secret_key = 'some-secret-key'  
openai.api_key = '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'
messages = [
    {"role": "system", "content": "You are a helpful and kind AI Assistant and specialize in the field of Chemical Engineering, particularly in Transport Phenomena."},
]

@app.route('/')
def home():
    if 'history' not in session:
        session['history'] = []
    return render_template('index.html', history=session['history'])

@app.route('/ask', methods=['POST'])
def ask():
    question = request.form['question']
    messages.append({"role": "user", "content": question})
    chat = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", messages=messages
        )
    entry = {
        "question": question,
        "answer": chat.choices[0].message.content,
    }
    session['history'].append(entry)
    session.modified = True  # Ensure the session knows it has been modified
    return render_template('index.html', history=session['history'])

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/howtouse')
def howtouse():
    return render_template('howtouse.html')

@app.route('/contactus')
def contactus():
    return render_template('contactus.html')

if __name__ == '__main__':
    app.run(debug=True)




