from flask import Flask,render_template,request,session
import random


app = Flask(__name__)
app.secret_key = '1234'



@app.route('/',methods=['GET',"POST"])
def roman():
    if request.method=="POST":
        try:
            s = request.form['roman'].upper()
            d = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
            le = len(s) 
            ans = 0
            for i in range (0,le):
                if ( (i+1)!= len(s)) and ( d[s[i]] < d[s[i+1]] ):
                    ans = ans - d[s[i]]
                    
                else:
                    ans = ans + d[s[i]]
            result ={'inp':'Input : ' +str(s),'out':'Result : '+ str(ans)}
        except:
            result ={'inp':'Input not in required format' }
              
        return render_template('roman.html',result =result)
    

    inp = out =''
    result ={'inp':inp,'out': out}
    return render_template('roman.html',result=result)

       
if __name__ == '__main__':
    app.run(debug=True)
