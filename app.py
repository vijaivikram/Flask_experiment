from flask import Flask,render_template,request,jsonify

#object initialized
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/calculatemarks', methods=['GET','POST'])
def calculatemarks():
    if request.method=='GET':
        return render_template('marks.html')
    else:
        maths = float(request.form['Maths'])
        science = float(request.form['Science'])
        history = float(request.form['History'])
        
        average_marks = (maths+science+history)/3
        
        return render_template('calculate.html',results=average_marks)
    

@app.route('/cal')
def add():
    operation = request.json['operation']
    number_1 = request.json['number_1']
    number_2 = request.json['number_2']
    
    if operation == 'addition':
        res = int(number_1) + int(number_2)
    elif operation == 'multiplication':
        res = int(number_1) * int(number_2)     
    
    return jsonify(res)
        
        
        
if __name__=="__main__":
    app.run(debug=True )