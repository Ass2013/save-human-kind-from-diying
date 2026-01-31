from flask import Flask, render_template,request, redirect



app = Flask(__name__)

#Динамичные скиллы
@app.route('/quizz')
def quizz():
    return render_template('quizpage.html')

@app.route('/shop')
def shop():
    return render_template('shoppage.html')

@app.route('/info')
def info():
    return render_template('infopage.html')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/QUIZ11')
def quiz11():
    return render_template('QUIZ11.html')

@app.route('/QUIZ12')
def quiz12():
    return render_template('QUIZ12.html')

@app.route('/QUIZ21')
def quiz21():
    return render_template('QUIZ21.html')

@app.route('/QUIZ22')
def quiz22():
    return render_template('QUIZ22.html')

@app.route('/correct')
def correct():
    return render_template('correct.html')

@app.route('/wrong')
def wrong():
    return render_template('wrong.html')

@app.route('/wrong1')
def wrong1():
    return render_template('wrong1.html')

@app.route('/correct1')
def correct1():
    return render_template('correct1.html')

@app.route('/wrong2')
def wrong2():
    return render_template('wrong2.html')

@app.route('/correct2')
def correct2():
    return render_template('correct2.html')

@app.route('/wrong3')
def wrong3():
    return render_template('wrong3.html')

@app.route('/correct3')
def correct3():
    return render_template('correct3.html')

def process_form():
    button_quiz1 = request.form.get('button_quiz1')
    button_quiz2 = request.form.get('button_quiz2')
    button_quiz3 = request.form.get('button_quiz3')
    button_quiz4 = request.form.get('button_quiz4')
    return render_template('index.html', button_quiz1=button_quiz1, button_quiz2=button_quiz2, button_quiz3=button_quiz3, button_quiz4=button_quiz4)
    


if __name__ == '__main__':
    app.run(debug=True)

