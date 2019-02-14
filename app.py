from flask import Flask, session, request, render_template
import surveys

app = Flask(__name__)
app.secret_key = "Vive La France"


@app.route('/')
def landing_screen():
    '''display screen with title, instructions, and start button'''
    title_of_survey = surveys.satisfaction_survey.title
    survey_instructions = surveys.satisfaction_survey.instructions
    session['answers'] = []
    return render_template('landing_page.html', title_of_survey=title_of_survey, survey_instructions=survey_instructions)


@app.route('/questions/<question_index>', methods=["POST"])
def testing(question_index):
    '''Present first question, POST response on submit.'''
    q_at_index = surveys.satisfaction_survey.questions[question_index]
    question_text = q_at_index.question
    choices = q_at_index.choices

    answers = session['answers']
    answers.append[f'{choice}']
    session['answers'] = answers
    return render_template('base.html')