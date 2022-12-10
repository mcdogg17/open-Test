import requests
import toxicity_test

url = 'localhost'
port = '80'

positive_message = {"text": "Ты добрый человек",
                    "neutral": 0.1441,
                    "positive": 0.8279,
                    "negative": 0.0280
                    }
neutral_message = {"text": "hello",
                   "neutral": 0.8264,
                   "positive": 0.1148,
                   "negative": 0.0588}
negativ_message = {"text": "Ты ужасный",
                   "neutral": 0.1806,
                   "positive": 0.0678,
                   "negative": 0.7516}
empty_message = {"text": '',
                 "neutral": 0.7128,
                 "positive": 0.1686,
                 "negative": 0.1185}


def go_tests():
    posit = requests.post(f'http://{url}:{port}/toxicity', data=positive_message['text'].encode('utf-8')).json()
    if posit['positive'] > 80:
        print('Test Positive passed')
    else:
        print('Test Positive failed')
    neutral = requests.post(f'{url}:{port}/toxicity', data=neutral_message['text'].encode('utf-8')).json()
    if neutral['neutral'] > 80:
        print('Test Neutral passed')
    else:
        print('Test Neutral failed')
    negative = requests.post(f'{url}:{port}/toxicity', data=negativ_message['text'].encode('utf-8')).json()
    if negative['negative'] > 75:
        print('Test Negative passed')
    else:
        print('Test Negative failed')
    empty = requests.post(f'{url}:{port}/toxicity', data=empty_message["text"].encode('utf-8')).json()
    if empty['neutral'] > 70:
        print('Test Empty passed')
    else:
        print('Test Empty failed')


go_tests()
