from flask import Flask, render_template

app = Flask(__name__)

# Task 1: Simple Template with "Hello, {{ name }}!"
@app.route('/hello/<name>')
def hello(name):
    return render_template('hello.html', name="Apoorva")

# Task 2: Display a list of fruits
@app.route('/fruits')
def fruits():
    fruit_list = ['Apple', 'Banana', 'Cherry']
    return render_template('fruits.html', fruits=fruit_list)

# Task 3: Add a conditional statement to check age
@app.route('/age/<int:age>')
def age_check(age):
    return render_template('age_check.html', age=age)

if __name__ == '__main__':
    app.run(debug=True)
