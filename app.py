from flask import Flask, render_template, request, session, redirect, url_for

app = Flask(__name__)
app.secret_key = "some_random_secret_key"  # for session management

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Calculate VAT and covered amounts based on input percentages
        amount = float(request.form['amount'])
        vat_amount = float(request.form['vat_amount']) if 'vat_amount' in request.form else 0
        coverage = float(request.form.get('coverage', 100)) / 100
        covered_amount = amount * coverage

        # Add the new expense to the session
        expense = {
            'date': request.form['date'],
            'description': request.form['description'],
            'merchant': request.form['merchant'],
            'amount': amount,
            'vat_amount': vat_amount,
            'covered_amount': covered_amount
        }
        if 'expenses' not in session:
            session['expenses'] = []
        session['expenses'].append(expense)
        return redirect(url_for('index'))

    expenses = session.get('expenses', [])
    return render_template('index.html', expenses=expenses)

@app.route('/clear', methods=['GET'])
def clear():
    session.clear()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
