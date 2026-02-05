#echo.py

def echo(text: str, repetitions: int = 3) -> str:
    '''Imitate a real like echo.'''
    result = []
    for i in range(repetitions):
        result.append(text[-3+i:])

    return '\n'.join(result) + '\n.'


if __name__ == '__main__':
    text = input('Yell something at a mountain: ')
    print(echo(text))

