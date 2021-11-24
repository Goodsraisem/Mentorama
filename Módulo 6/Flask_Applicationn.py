from flask import Flask, render_template, url_for, request, redirect

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def index():
    res = ""
    if request.method == 'POST' and 'val1' in request.form and 'val2' in request.form and 'opr' in request.form:
        val1 = str(request.form.get('val1'))
        val2 = str(request.form.get('val2'))
        opr = str(request.form.get('opr'))

        try:
            if opr == '+':
                res = int(val1) + int(val2)
                return render_template('home.html', res=res)
            elif opr == '-':
                res = int(val1) - int(val2)
                return render_template('home.html', res=res)
            elif opr == '*':
                res = int(val1) * int(val2)
                return render_template('home.html', res=res)
            elif opr == '/':
                res = int(val1) / int(val2)
                return render_template('home.html', res=res)

        except:
            TypeError('Insira todos os valores')



    else:
        return render_template('home.html')


if __name__ == "__main__":
    app.run(debug=True)