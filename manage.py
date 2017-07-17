from flask import Flask, render_template, request

app = Flask("MyApp")

@app.route("/")
def welcome():
    return render_template("hello.html")

@app.route("/signup", methods=["POST"])
def sign_up():
    print("hello")
    form_data = request.form
    print("hello2")

    email = form_data["email"]
    name = form_data["name"]
    surname = form_data["surname"]
    fav_color = form_data["fav_color"]
    print(email)
    print(name)
    print(surname)
    print(fav_color)
    return "All OK. Your name is {} {} and your email is {}. Your favorite color is {}!".format(name, surname, email, fav_color)
    #return "hello world {}".format(email)
app.run(debug=True)
