import requests 
import random
import html

EDUCATION_CATEGORY_ID = 9
TRIVIA_API_URL = f"https://opentdb.com/api.php?amount=10&category={EDUCATION_CATEGORY_ID}&type=multiple"
FUN_FACTS_API_URL = "http://numbersapi.com/random/trivia"

def get_education_questions():
    response = requests.get(TRIVIA_API_URL)
    if response.status_code == 200:
        data = response.json()
        if data['response_code'] == 0 and data['results']:
            return data['results']
    return None

def get_fun_fact():
    """Fetch a random fun fact from Numbers API"""
    try:
        response = requests.get(FUN_FACTS_API_URL)
        if response.status_code == 200:
            return response.text
    except:
        pass
    return "Did you know? Learning is fun!"

def display_fun_fact():
    """Display a fun fact between questions"""
    fact = get_fun_fact()
    print(f"\n🎯 Fun Fact: {fact}")
    input("Press Enter to continue...")

def run_quiz():
    questions = get_education_questions()
    if not questions:
        print("Failed to fetch questions.")
        return
    
    score = 0
    print("Welcome to the Education Quiz with Fun Facts!")
    
    for i, q in enumerate(questions, 1):
        # Show fun fact every 3 questions
        if i > 1 and (i - 1) % 3 == 0:
            display_fun_fact()
        
        question = html.unescape(q['question'])
        correct = html.unescape(q['correct_answer'])
        incorrects = [html.unescape(ans) for ans in q['incorrect_answers']]
        options = incorrects + [correct]
        random.shuffle(options)

        print(f"\nQuestion {i}: {question}")
        for idx, option in enumerate(options, 1):
            print(f"{idx}. {option}")

        while True:
            try:
                choice = int(input("\nEnter your choice (1-4): "))
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

    # Final fun fact and results
    print("\n" + "="*40)
    display_fun_fact()
    print(f"\nFinal score: {score}/{len(questions)}")
    print(f"Percentage: {score / len(questions) * 100:.1f}%")

if __name__ == "__main__":
    run_quiz()