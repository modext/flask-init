from flask import Flask, render_template, url_for, redirect, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/success/<int:score>')
def success(score):
    return render_template("result.html",result=score)

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

@app.route('/submit',methods=['POST','GET'])
def submit(): 
    total_score=0
    if request.method== 'POST':
        science=float(request.form['science'])
        math=float(request.form['math'])
        english=float(request.form['english'])
        programming=float(request.form['programming'])
        total_score=(science+math+english+programming)/4
    res=""
          
    return redirect(url_for('success',score=total_score))





if __name__ == '__main__':
    app.run(debug=True)
    
    
    # let us do this one to check if its working
