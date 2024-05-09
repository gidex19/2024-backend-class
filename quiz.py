import json
import random

selected_index = []

def create_unselected_question(start_point, end_point):
    rand = random.randint(start_point, end_point)
    if rand in selected_index:
        create_unselected_question(start_point, end_point)
    else:
        return rand    

f = open("q.json", "r")
# print(f.read())
q_and_a_json = f.read()

q_and_a_list = json.loads(q_and_a_json)

n_of_q = len(q_and_a_list)
score = 0


print("Your Exam has just started")
for i in range(10):
    q_index = create_unselected_question(0, 46)
    question = q_and_a_list[q_index]
    print(f"QUESTION {i+1}: {question['question']}\n A: {question['A']}\nB: {question['B']}\nC: {question['C']}\nD: {question['D']}\n")
    selected_answer = input("Enter your Answer: ").strip()
    if selected_answer == question["answer"]:
        score += 1
print(f"Exam completed\nYou scored {score}/10")   

