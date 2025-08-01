import requests 
import random
import html

EDUCATION_CATEGORY_ID= 9
API_URL = f"https://opentdb.com/api.php?amount=10&category={EDUCATION_CATEGORY_ID}&type=multiple"

def get_education_questions():
    response= requests.get(API_URL)
    if response.status_code == 200:
        data = response.json()
        if data['response_code'] == 0 and data ['results']:
            return data['results']
    return None

def run_quiz():
    questions = get_education_questions()
    if not questions:
        print("failed to fetch questions.")
        return
    
    score = 0
    print("Welcome to the Education Quiz!")
    for i,q in enumerate(questions,1):
        question=html.unescape(q['question'])
        correct=html.unescape(q['correct_answer'])
        incorrects = [html.unescape(ans) for ans in q['incorrect_answers']]
        options = incorrects + [correct]
        random.shuffle(options)

        print(f"\nQuestion {i}: {question}")
        for idx, option in enumerate(options, 1):
            print(f"{idx}. {option}")

        while True:
            try:
                choice= int(input("\n Enter your choice (1-4): "))
                if 1 <= choice <= 4:
                    break
            except ValueError:
                pass
            print("Invalid Input")

        if options[choice - 1] == correct:
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The correct answer is: {correct}")

        print(f"Final score: {score}/{len(questions)}")
        print(f"percentage: {score / len(questions) * 100:.1f}%")


if __name__ == "__main__":
    run_quiz()