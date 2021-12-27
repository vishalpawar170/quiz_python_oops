from question_model import Question
from data import question_data
from quiz_brain import Quizbrain

# list of question objects
question_bank=[]

for question in question_data:
    question_text=question["question"]
    question_ans=question["correct_answer"]
    new_question=Question(question_text,question_ans)
    question_bank.append(new_question)


quiz=Quizbrain(question_bank) 
while quiz.still_has_questions():
    quiz.next_question()   


# print(question_bank)
    
    