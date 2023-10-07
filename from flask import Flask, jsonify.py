from flask import Flask, jsonify
import random

app = Flask(__name__)

def get_random_quote():
    with open('quotes.txt', 'r') as file:
        quotes = file.readlines()
    return random.choice(quotes).strip()

@app.route('/random-quote')
def random_quote():
    quote = get_random_quote()
    return jsonify({'quote': quote})

if __name__ == '__main__':
    app.run()