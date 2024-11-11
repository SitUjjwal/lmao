from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/register', methods=["POST", "GET"])
def register():
    if request.method == "POST":
        username = request.form["username"]
        email = request.form['email']
        mobile = request.form['mobile']
        password = request.form['password']
        cpassword = request.form['cpassword']
        img = request.files["img"]
        

        if password == cpassword:
            if len(username) < 3:
                return render_template('index.html', message="User name should be contain atleast 3 characters")
            else:
                if len(str(mobile)) == 10:
                    return render_template('index.html', message="Registered Successfully !!!",
                                           username=username, password=password, email=email, mobile=mobile,
                                           img=img)
                else:
                    return render_template('index.html',
                                           message="Mobile number Should Contains Exactly 10 number")
        else:
            return render_template('index.html',
                                   message="Confirm password is not match")


if __name__ == "__main__":
    app.run(debug=True)
