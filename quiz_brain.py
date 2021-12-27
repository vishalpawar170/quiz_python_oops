#asking the questions
# checking if the  answer was correct 
# checking if we end the quiz
class Quizbrain:
    def __init__(self,q_list):
        self.question_no=0
        self.question_list=q_list

    def still_has_questions(self):
        return self.question_no < len(self.question_list)    

    def next_question(self):
        # print("vis",self.question_list)
        current_question=self.question_list[self.question_no] 
        self.question_no=self.question_no+1
        user=input(f"Q {self.question_no}:{current_question.text} (True/False):") 
        current_answer=current_question.answer
        self.check_answer(user,current_answer) 

    def check_answer(self,user_input,current_answer): 
        score=0
        if(user_input.lower() == current_answer.lower()):
            print("corrrect ans")
            score+=1
        else:
            print("Not correct answer") 
            print(f"correct answer:{current_answer}")      

        


