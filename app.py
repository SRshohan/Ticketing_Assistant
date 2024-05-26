from flask import render_template, Flask, request
from ticket_assist import template_of

app = Flask(__name__)

@app.route("/home", methods=['GET', 'POST'])
def home():
    questions = ""
    if request.method == 'POST':
        questions = request.form['user_input']
        result = template_of(question=questions)

    return render_template("paragraph.html", result=result, questions=questions)






if __name__ == '__main__':
    app.run(debug=True)
