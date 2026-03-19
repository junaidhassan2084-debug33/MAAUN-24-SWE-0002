from flask import Flask, render_template, request, redirect, session
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Sample test bank
questions = [
    {'question': 'What is the capital of France?', 'options': ['Paris', 'London', 'Berlin', 'Madrid'], 'answer': 'Paris'},
    {'question': 'What is 2 + 2?', 'options': ['3', '4', '5', '6'], 'answer': '4'},
    {'question': 'What is the capital of Japan?', 'options': ['Seoul', 'Tokyo', 'Beijing', 'Bangkok'], 'answer': 'Tokyo'},
    {'question': 'What is the largest ocean?', 'options': ['Atlantic', 'Indian', 'Arctic', 'Pacific'], 'answer': 'Pacific'},
    {'question': 'What is the chemical symbol for Water?', 'options': ['O2', 'H2O', 'CO2', 'N2'], 'answer': 'H2O'}
]

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/start')
def start():
    session['score'] = 0
    session['current_question'] = 0
    session['start_time'] = datetime.utcnow()
    return redirect('/question')

@app.route('/question')
def question_display():
    current_question = session.get('current_question', 0)
    if current_question >= len(questions):
        return redirect('/results')
    question = questions[current_question]
    return render_template('question.html', question=question, question_number=current_question + 1)

@app.route('/answer', methods=['POST'])
def answer():
    selected_option = request.form['option']
    current_question = session['current_question']
    if selected_option == questions[current_question]['answer']:
        session['score'] += 1
    session['current_question'] += 1
    return redirect('/question')

@app.route('/results')
def results():
    score = session.get('score', 0)
    total_questions = len(questions)
    end_time = datetime.utcnow()
    duration = end_time - session.get('start_time')
    return render_template('results.html', score=score, total=total_questions, duration=duration)

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)
