from flask import Flask, render_template

app = Flask(__name__, static_folder='static', template_folder='templates')

@app.route('/')
def index():
    return render_template('ui.html')  # Serves the main HTML file

if __name__ == "__main__":
    app.run(port=5000, debug=True)  # Main UI runs on port 5000
