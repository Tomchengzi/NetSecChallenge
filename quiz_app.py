from flask import Flask, render_template, jsonify, request, abort
import pandas as pd
import random
import os

app = Flask(__name__)

# 使用相对路径加载文件
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
df1 = pd.read_excel(os.path.join(BASE_DIR, 'data', '题库1.xlsx'))
df2 = pd.read_excel(os.path.join(BASE_DIR, 'data', '题库2.xlsx'))

class QuestionSystem:
    def __init__(self, df):
        self.df = df

    def format_question(self, row):
        question = row['题目']
        options = {
            'A': row['选项A'],
            'B': row['选项B'],
            'C': row['选项C'],
            'D': row['选项D']
        }
        answer = row['答案']
        return {'question': question, 'options': options, 'answer': answer}

    def get_random_questions(self, num_questions):
        num_questions = min(num_questions, len(self.df))
        random_rows = self.df.sample(n=num_questions).reset_index(drop=True)
        return [self.format_question(row) for _, row in random_rows.iterrows()]

first_level = QuestionSystem(df1)
second_level = QuestionSystem(df2)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_questions/first', methods=['GET'])
def get_first_level_questions():
    try:
        num_questions = int(request.args.get('num_questions', 7))
        if num_questions <= 0:
            abort(400, description="Invalid number of questions.")
        questions = first_level.get_random_questions(num_questions)
        return jsonify(questions)
    except ValueError:
        abort(400, description="Invalid parameter.")

@app.route('/get_questions/second', methods=['GET'])
def get_second_level_questions():
    try:
        num_questions = int(request.args.get('num_questions', 5))
        if num_questions <= 0:
            abort(400, description="Invalid number of questions.")
        questions = second_level.get_random_questions(num_questions)
        return jsonify(questions)
    except ValueError:
        abort(400, description="Invalid parameter.")

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, threaded=True)
