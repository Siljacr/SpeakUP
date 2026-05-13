from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    answer = request.form['answer']

    word_count = len(answer.split())

    feedback = []

    if word_count < 30:
        feedback.append("Try to speak more confidently and add more points.")

    if "um" in answer.lower() or "uh" in answer.lower():
        feedback.append("Avoid filler words like 'um' and 'uh'.")

    if len(feedback) == 0:
        feedback.append("Good communication and sentence formation.")

    model_answer = "A good answer should contain introduction, key points, examples, and conclusion."

    return render_template(
        'index.html',
        feedback=feedback,
        model_answer=model_answer,
        answer=answer
    )

if __name__ == '__main__':
    app.run(debug=True)