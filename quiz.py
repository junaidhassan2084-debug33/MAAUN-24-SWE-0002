import argparse

def main():
    parser = argparse.ArgumentParser(description='Quiz Application')
    parser.add_argument('--question', type=str, help='The question to ask')
    parser.add_argument('--options', type=str, nargs='+', help='List of options')
    parser.add_argument('--answer', type=str, help='Correct answer')

    args = parser.parse_args()
    print(f'Question: {args.question}')
    print('Options:')
    for option in args.options:
        print(f'- {option}')

    user_answer = input('Your answer: ')
    if user_answer.lower() == args.answer.lower():
        print('Correct!')
    else:
        print('Wrong answer.')

if __name__ == '__main__':
    main()