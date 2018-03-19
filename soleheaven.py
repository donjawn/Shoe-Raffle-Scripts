import requests
from random import getrandbits
url = 'https://www.soleheaven.com/pages/wotherspoon-raffle'

headers = {'User-Agent':
           'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}


# CHANGE the fields as the comments say  
def main(limit):
    for i in range(1, limit):
        num = getrandbits(40)
        name = 'mark ramirez{}'.format(num) # put your name here, don't remove the {}
        email = 'markakadon+{}@gmail.com'.format(num) # CHANGE YOUR_EMAIL to your email prefix. don't change the +{} after.
        payload = {
            'action': 'contest',
            'email': email,
            'size': '10.5', # change your size
        }
        resp = requests.post(url, data=payload, headers=headers)
        print('{}/{} registered.'.format(i, limit))

if __name__ == "__main__":
    main(100000)
