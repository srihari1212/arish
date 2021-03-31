from flask import Flask,request,jsonify, make_response

app = Flask(__name__) 
app.debug = True

@app.route('/',methods=["POST"])
def add2num():
    try:
        a=request.form["number1"]
        b=request.form["number2"]
        c=int(a)+int(b)
        return str(c)
    except:
        return make_response(jsonify(
                {
                    'status' : 'fail',
                    'desc':'Error in adding two numbers',
                    'result' : {}
                }
            ), 207)


if __name__ == '__main__': 
    app.run() 

#http://127.0.0.1:5000/
