import json
import requests

# Given headers
headers = {
    'Content-Type': 'application/x-www-form-urlencoded',
    'User-Agent': 'AndroidTranslate/5.3.0.RC02.130475354-53000263 5.1 phone TRANSLATE_OPM5_TEST_1',
}

# Given query params
payload = {
    'iid': '1dd3b944-fa62-4b55-b330-74909a99969e',
    'client': 'at',
    'dt': ['t', 'ld', 'qca', 'rm', 'bd'],
    'dj': '1',
    'hl': '%s',
    'ie': 'UTF-8',
    'oe': 'UTF-8',
    'inputm': '2',
    'otf': '2',
    'sl': 'pt',
    'tl': 'en',
}

def read(filename):
    """Read the source text to be translated."""

    with open(filename, 'r') as file:
        source = file.read().strip()

    return source

def write(filename, data):
    """Write the targeted translation."""

    with open(filename, 'w') as file:
        file.write(data)
        file.write('\n')

def main():
    source = read('source.txt')

    payload['q'] = source

    response = requests.get('https://translate.google.com/translate_a/single', headers=headers, params=payload)

    if response.status_code != 200:
        # Exit if request fails
        raise SystemExit('Oops! Request has failed')

    sentences = response.json()['sentences']

    target = [item['trans'] for item in sentences]  # Get the translated sentences
    target = ''.join(target)

    # write('target.txt', target)  # Write the output file

    print('Source [PT] ::', source)
    print('Target [EN] ::', target)

if __name__ == '__main__':
    main()
