from flask import render_template, Flask, request
from ticket_assist import template_of

app = Flask(__name__)


@app.route("/home", methods= ['GET', 'POST'])
def para():
    question = ''
    result = None
    if request.method == 'POST':
        question = request.form['user_input']

        result = template_of(question=question)

    return render_template('paragraph.html', user_input=question, result=result) 

if __name__ == '__main__':
    app.run(debug=True)