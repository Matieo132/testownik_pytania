# functions.py

import os

def save_to_file(filename, content):
    with open(filename, 'w') as file:
        file.write(content)

def format_question(question):
    question = question.strip()
    if question:
        question = question[0].upper() + question[1:]
    if not question.endswith('?'):
        question += '?'
    return question

def get_next_number(directory):
    existing_files = [f for f in os.listdir(directory) if f.startswith("Question_") and f.endswith(".txt")]
    if not existing_files:
        return 1
    max_number = 0
    for filename in existing_files:
        try:
            number = int(filename.split('_')[1].split('.')[0])
            if number > max_number:
                max_number = number
        except ValueError:
            continue
    return max_number + 1

def save_each_qna_separately(directory, questions_and_answers):
    if not os.path.exists(directory):
        os.makedirs(directory)

    start_number = get_next_number(directory)

    for i, (question, answers) in enumerate(questions_and_answers, start=start_number):
        filename = os.path.join(directory, f"Question_{i}.txt")
        content = f"{i}. {format_question(question)}\n\n"
        for index, answer in enumerate(answers, start=ord('a')):
            content += f"{chr(index)}) {answer}\n"
        content += "\n" + "-"*40 + "\n\n"
        save_to_file(filename, content)

def reset_counter(label):
    global question_count
    question_count = 0
    label.configure(text=f"Questions Added: {question_count}")
