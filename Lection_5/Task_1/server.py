from flask import Flask, render_template, request, redirect

app = Flask(__name__)
app.config['STATIC_FOLDER'] = 'static'

userData = {"admin": "12345"}
chatList = ['Console: Welcome to chat!']

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    userLogin = request.form['username']
    userPassword = request.form['password']
    if userLogin:
        if userPassword:
            if userLogin in userData and userPassword == userData[userLogin]:
                return redirect(f'/chat/{userLogin}', code=302)
            else:
                return render_template('index.html', check=True)
        else:
            return render_template('index.html', password=True)
    else:
        return render_template('index.html', login=True)

@app.route('/chat/<string:userLogin>')
def chat(userLogin:str):
    if userLogin not in userData:
        return redirect('/')
    url = f"/sendMsg/{userLogin}"
    return render_template('chat.html', chatList=chatList, url=url)

@app.route('/sendMsg/<string:userLogin>', methods=['POST'])
def sendMsg(userLogin:str):
    userLogin = userLogin.strip(",")
    usersMsg = request.form['msg']
    if len(chatList)>=14:
        del chatList[0]
        chatList.append(f"{userLogin}: {usersMsg}")
    else:
        chatList.append(f"{userLogin}: {usersMsg}")
    return redirect(f'/chat/{userLogin}', code=302)

@app.route('/registration')
def registration():
    return render_template('registration.html')

@app.route('/reg', methods=['POST'])
def reg():
    userLogin = request.form['username']
    userPassword = request.form['password']
    if userLogin:
        if userLogin not in userData:
            if len(userLogin)>=3:
                if userPassword and len(userPassword)>=5:
                    userData[userLogin] = userPassword
                else:
                    return render_template('registration.html', password=True)
            else:
                return render_template('registration.html', login_len=True)
        else:
            return render_template('registration.html', unique_login=True)
    else:
        return render_template('registration.html', login=True)
    return redirect(f'/chat/{userLogin}', code=302)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8081)