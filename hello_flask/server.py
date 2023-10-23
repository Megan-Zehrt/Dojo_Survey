from flask import Flask, render_template, request, redirect, url_for, session # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"
app.secret_key = 'the secret key, key the secret of the secret key I think?'

@app.route('/')          # The "@" decorator associates this route with the function immediately following
def form():
    return render_template('form.html')  # Return the string 'Hello World!' as a response


@app.route('/processing', methods=['POST'])
def submit_form():
    if request.method == 'POST':
        session['name'] = request.form['name']
        session['state_select'] = request.form.get('state_select')
        session['lang_select'] = request.form.get('lang_select')
        session['commenting'] = request.form.get('commenting')

       # return redirect(url_for('result'))
        return render_template('result.html')

@app.route('/result')
def result():
    return render_template('result.html')



if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.