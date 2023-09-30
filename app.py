from flask import Flask, render_template, request, session, redirect, url_for

app = Flask(__name__)
app.secret_key = "some_random_secret_key"  # for session management

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Add the new expense to the session
        expense = {
            'date': request.form['date'],
            'description': request.form['description'],
            'merchant': request.form['merchant'],
            'amount': float(request.form['amount'])
        }
        if 'expenses' not in session:
            session['expenses'] = []
        session['expenses'].append(expense)
        return redirect(url_for('index'))

    expenses = session.get('expenses', [])
    return render_template('index.html', expenses=expenses)

if __name__ == '__main__':
    app.run(debug=True)
