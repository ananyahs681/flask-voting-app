from flask import Flask, jsonify

app = Flask(__name__)
votes = {}

@app.route('/')
def home():
    return "Welcome to the App"

@app.route('/health')
def health():
    return "App is running"


@app.route('/vote/<name>')
def vote(name):
    if name in votes:
        votes[name] += 1
    else:
        votes[name] = 1
    return f"Vote recorded for {name}. Total votes: {votes[name]}"


@app.route('/results')
def results():
    return jsonify(votes)

@app.route('/reset')
def reset():
    votes.clear()
    return jsonify({"msg": "All votes have been reset"})

if __name__ == '__main__':
    app.run(debug=True)



