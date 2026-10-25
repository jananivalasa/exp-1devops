from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']

        # For this experiment, we are only receiving the data.
        # In a real application, store it securely in a database.
        print("Name:", name)
        print("Email:", email)

        return render_template('success.html')

    return render_template('register.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)