# generating random numbers

import random
from flask import flask, jsonify 


app = flask.Flask(_name_)
@app.route('/prng')
def random_number(): 
    return jsonify(random.randint(1, 15))
if __name__ == '__main__':
    app.run(port=5000)  # Runs the server on localhost:5000
    

