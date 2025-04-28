from flask import Flask, render_template, request, redirect, url_for
app= Flask(__name__)
@app.route('/',methods=['GET'])
def welcome():
    return "Sandy's Git Practice"
@app.route('/index',methods=['GET'])
def index():
    return "Welcome to the index page!"
#variable routing
@app.route('/success/<int:score>',methods=['GET'])
def success(score):
    return f"Your score is {score} it's a success!"
@app.route('/failure/<int:score>',methods=['GET'])
def failure(score):
    return f"Your score is {score} it's a failure!"
@app.route('/form',methods=['GET','POST'])
def forms():
    if request.method == "GET":
        return render_template('forms.html')
    else:
        maths=float(request.form['maths'])
        science=float(request.form['science'])
        history=float(request.form['history'])
        average=(maths+science+history)/3
        if average >= 50:
            res="success"
        else:
            res="failure"
        return redirect(url_for(res,score=average))

        #return render_template('forms.html',score=average)



if __name__ == '__main__':
    app.run(debug=True)