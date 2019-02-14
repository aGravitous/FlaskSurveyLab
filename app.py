from flask import Flask, session, request, render_template
import surveys

app = Flask(__name__)
app.secret_key = "Vive La France"


@app.route('/')
def landing_screen():
    '''display screen with title, instructions, and start button'''
    title_of_survey = surveys.satisfaction_survey.title
    survey_instructions = surveys.satisfaction_survey.instructions
    return render_template('landing_page.html', title_of_survey=title_of_survey, survey_instructions=survey_instructions)

