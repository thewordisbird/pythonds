import random

characters = list('abcdefghijklmnopqrstuvwxyz ')

def generate_string(string_length, string):
    
    for i in range(string_length):
        if string[i] == '':
            string[i] = random.choice(characters)

    return string


def check_string(string, target):
    correct_chars = 0
    for i, letter in enumerate(string):
        if letter == target[i]:
            correct_chars += 1
        else:
            string[i] = ''

    #print(f'{correct_chars} | {len(target)} | {correct_chars/len(target)}')
    return correct_chars/len(target)

def engine (target):
    top_score = 0
    top_string = ""

    string_length = len(target)
    string = [''] * string_length
    
    for n in range(100):
        generate_string(string_length, string)

        string_score = check_string(string, target)
        if string_score > top_score:
            top_score = string_score
            top_string = string

    return top_score, ''.join(top_string)


if __name__ == '__main__':
    target = "methinks it is like a weasel"
    #target = 'test'
    
    print(f'Target: "{target}" | Guess: "{engine(target)[1]}" | Score: {engine(target)[0]} ')