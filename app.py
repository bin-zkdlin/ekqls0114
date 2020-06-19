from flask import Flask, request, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return '메인페이지'

@app.route('/hello')
def hello():
    return 'Hello, World!'

@app.route('/hello/<name>')
def hellolovar(name):
    return 'Hello, {}!'.format(name)

@app.route('/input/<int:num>')
def input_num(num):
    if num == 1:
        return "도라에몽"
    elif num == 2:
        return "진구"
    elif num == 3:
        return "퉁퉁이"
    else:
        return "없어요"
    #return 'Hello, {}!'.format(num)

@app.route('/naver')
def naver():
    return render_template("naver.html")

@app.route('/img')
def img():
    return render_template("image.html")

#로그인
@app.route('/login',methods=['GET','POST'])
def login():
    if request.method =='GET':
        return render_template('login.html')
    else:
        id = request.form['id']
        pw = request.foem['pw']
        print (id,type(id))
        print (pw,type(pw))
        #id와 pw가 임의로 정한 값이랑 비교 해서 맞으면 맞다 틀리면 틀리다
        if id == 'abc' and pw == '1234':
            return "안녕하세요~ {} 님".format(id)
        else:
            return "아이디 또는 패스워드를 확인 하세요."

@app.route('/form')
def form():
    return render_template('test.html')

@app.route('/method', methods=['GET','POST'])
def method():
    if request.method =='GET':
        return 'GET 으로 전송이다.'
    else:
        num = request.form['num']
        name = request.form['name']
        print(num, name)
        return 'POST 이다. 학번은: {} 이름은:{}'.format(num, name)

if __name__ == '__main__':
    app.run(debug=True)