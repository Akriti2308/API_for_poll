from flask import Flask, render_template, request
import random, copy

app = Flask(__name__)

original_questions = {
 'Taj Mahal':['Agra','New Delhi','Mumbai','Chennai'],
 'Great Wall of China':['China','Beijing','Shanghai','Tianjin'],
 'Petra':['Maan Governorate','Amman','Zarqa','Jerash'],
 'Machu Picchu':['Cuzco Region','Lima','Piura','Tacna']
}
questions = copy.deepcopy(original_questions)

def shuffle(q):
 selected_keys = []
 i = 0
 while i < len(q):
  current_selection = random.choice(q.keys())
  if current_selection not in selected_keys:
   selected_keys.append(current_selection)
   i = i+1
 return selected_keys

@app.route('/')
def quiz():
 questions_shuffled = shuffle(questions)
 for i in questions.keys():
  random.shuffle(questions[i])
 return render_template('main.html', q = questions_shuffled, o = questions)


@app.route('/quiz', methods=['POST'])
def quiz_answers():
 correct = 0
 for i in questions.keys():
  answered = request.form[i]
  if original_questions[i][0] == answered:
   correct = correct+1
 return '<h1>Correct Answers: <u>'+str(correct)+'</u></h1>'

if __name__ == '__main__':
 app.run(debug=True)