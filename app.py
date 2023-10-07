from flask import Flask

app = Flask(__name__)

@app.route('/',methods=['GET','POST','PUT'])
def helloWorld():
    return "Hello World!"
@app.route('/pricing')
def pricing():
    return "10000"
@app.route("/aboutus")
def aboutus():
    return "aboutus!!"

@app.route("/pallindromornot")
def pal():
    num = int(input("Enter the number"))
    temp = num
    rev = 0
    while (num > 0):
        dig = num % 10
        rev = rev * 10 + dig
        num = num // 10
    if (temp == rev):
        return "The number is a palindrome!"
    else:
        return "The number isn't a palindrome!"

if __name__ == "__main__":
    app.run(debug=True)