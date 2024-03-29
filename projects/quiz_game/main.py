from projects.quiz_game.question import Question
from projects.quiz_game.data import question_data
from projects.quiz_game.quiz_game import Quiz_Game

question_bank = []


def populate_question_bank():
    for entry in question_data:
        # access via .get() is a bit safer as returns none if not present. direct access throws KeyError
        # question_bank.append(Question(entry.get("text"), entry.get("answer")))
        question_bank.append(Question(entry["text"], entry["answer"]))


def start_quiz_game():
    quiz_game = Quiz_Game(question_bank)
    while(quiz_game.still_has_questions()):
         quiz_game.next_question()
    print("Completed quiz_game")
    print(f"Total score is {quiz_game.score}/{quiz_game.question_number}" )

if __name__ == '__main__':
    populate_question_bank()
    start_quiz_game()
