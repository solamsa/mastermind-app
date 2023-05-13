import random




def create_code():
    """Function that creates the 4 digit code, using random digits from 1 to 8"""


    code = [0, 0, 0, 0]

    for i in range(4):
        value = random.randint(1, 8) # 8 possible digits
        while value in code:
            value = random.randint(1, 8)  # 8 possible digits
        code[i] = value
    # print(code)
    return code
    

def get_answer_input():
    ''' get answer from user and return answer'''

    answer = input("Input 4 digit code: ")
    while len(answer) < 4 or len(answer) > 4:
        print("Please enter exactly 4 digits.")
        answer = input("Input 4 digit code: ")
    return answer


def show_instructions():
    """Shows instructions to the user"""

    print('''4-digit Code has been set. Digits in range 1 to 8. You have 12 turns to break it.''')


def show_results(correct_digits_and_position, correct_digits_only):
    """Show the results from one turn"""

    print('Number of correct digits in correct place:     ' + str(correct_digits_and_position))
    print('Number of correct digits not in correct place: ' + str(correct_digits_only))


def take_turn(code):
    """Handle the logic of taking a turn, which includes:

       * check correctness of answer
    """

    answer = get_answer_input()
    correct_digits_and_position_list = []
    correct_digits_only_list = []
    correct_digits_and_position  = 0
    correct_digits_only = 0

    for i in range(len(answer)):
        if (code[i] == int(answer[i]) and 
        answer[i] not in correct_digits_and_position_list):
            correct_digits_and_position_list.append(answer[i])
            correct_digits_and_position += 1
    
    for i in range(len(answer)):
        if (int(answer[i]) in code and 
        answer[i] not in correct_digits_and_position_list and
        answer[i] not in correct_digits_only_list):

            correct_digits_only_list.append(answer[i])
            correct_digits_only += 1

    return (correct_digits_and_position, correct_digits_only)

    
def show_code(code):
    """Show Code that was created to user"""

    print('The code was: '+str(code))


def check_correctness(correct_digits_and_position, correct, turns):
    """Checks correctness of answer and show output to user"""

    # correct = False

    if correct_digits_and_position == 4:
        correct = True
        print('Congratulations! You are a codebreaker!')
    else:
        print('Turns left: ' + str(12 - turns))
    return correct


def run_game():
    """Main function for running the game"""


    correct = False
    code = create_code()
    show_instructions()

    turns = 0
    while not correct and turns < 12:
        correct_digits_and_position, correct_digits_only = take_turn(code)
        show_results(correct_digits_and_position, correct_digits_only )
        turns += 1
        correct = check_correctness(correct_digits_and_position, correct, turns)

    show_code(code)


if __name__ == "__main__":
    run_game()
