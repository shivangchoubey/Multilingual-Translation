from flask import Flask, request, jsonify, render_template, redirect, url_for, session
from translator import translate_text
from speech import speak_text
import logging

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Needed for session management

@app.route('/')
def home():
    # Check if user is logged in, if not redirect to login page
    if 'logged_in' in session and session['logged_in']:
        return render_template('index.html')
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        # Validate credentials
        if username == '12315910' and password == '123':
            session['logged_in'] = True
            return redirect(url_for('home'))
        else:
            return render_template('login.html', error="Invalid username or password.")

    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    return redirect(url_for('login'))

@app.route('/translate', methods=['POST'])
def translate():
    try:
        data = request.get_json()
        if not data or 'text' not in data or 'lang' not in data:
            return jsonify({"error": "Missing 'text' or 'lang' parameter"}), 400

        text = data.get('text', '').strip()
        target_lang = data.get('lang', 'en').strip()

        if not text:
            return jsonify({"error": "Text cannot be empty"}), 400

        translated_text = translate_text(text, target_lang)
        return jsonify({"translated_text": translated_text})
    except Exception as e:
        return jsonify({"error": f"Translation failed: {str(e)}"}), 500

@app.route('/speak', methods=['POST'])
def speak():
    try:
        data = request.get_json()
        text = data.get('text', '').strip()

        if not text:
            return jsonify({"error": "Text cannot be empty"}), 400

        result = speak_text(text)
        if not result:
            return jsonify({"error": "Speech synthesis failed"}), 500

        return jsonify({"status": "Spoken successfully"})
    except Exception as e:
        return jsonify({"error": f"Speech synthesis failed: {str(e)}"}), 500

if __name__ == '__main__':
    app.run(debug=True)
