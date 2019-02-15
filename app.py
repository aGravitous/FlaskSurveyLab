from flask import Flask, session, request, render_template, redirect, flash
import surveys
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)
app.secret_key = "Vive La France"

debug = DebugToolbarExtension(app)

@app.route('/')
def landing_screen():
    '''display screen with title, instructions, and start button'''
    title_of_survey = surveys.satisfaction_survey.title
    survey_instructions = surveys.satisfaction_survey.instructions
    session['answers'] = []
    return render_template('landing_page.html',
                           title_of_survey=title_of_survey,
                           survey_instructions=survey_instructions)


@app.route('/questions/<int:question_index>')
def survey_start(question_index):
    '''Present first question, POST response on submit.'''
    q_at_index = surveys.satisfaction_survey.questions[question_index]
    question_text = q_at_index.question
    choice_list = q_at_index.choices

    return render_template('survey_page.html',
                           question_text=question_text,
                           choice_list=choice_list,
                           new_question_i=question_index)


@app.route('/questions/<int:question_index>', methods=["POST"])
def survey_continue(question_index):
    '''Present first question, POST response on submit.'''

    answer = request.form["choice"]

    answers = session['answers']
    answers.append(answer)
    session['answers'] = answers
    new_question_i = question_index + 1

    if new_question_i == len(surveys.satisfaction_survey.questions):
        flash('''Thank you for participating in this survey.
                        We appreciate your time and effort.''')
        return redirect('/thank_you_page')
    else:
        return redirect(f'/questions/{new_question_i}')


@app.route('/thank_you_page')
def thank_you():
    '''Thank user, offer new survey.'''

    return render_template('thank_you_page.html')