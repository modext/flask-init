from flask import Flask, render_template, url_for, redirect

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/success/<int:score>')
def success(score):
    return "Ther person has passed and the mark is"+ str(score)

@app.route('/fail/<int:score>')
def fail(score):
    return "Ther person has failed and the mark is "+ str(score)

@app.route('/result/<int:marks>')
def result(marks):
    result = ""
    if marks<50:
        result="fail"
    else:
        result= 'success'
    return redirect(url_for(result,score=marks))

@app.route('/men/')
def men_page():
    return render_template('men.html')
    # return render_template('men.html')

if __name__ == '__main__':
    app.run(debug=True)
    
    
    # let us do this one to check if its working