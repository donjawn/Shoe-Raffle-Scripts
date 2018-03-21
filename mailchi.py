import requests
from random import getrandbits
url = 'https://mailchi.mp/seftonfashion/air-max-day-raffle-release'

headers = {'User-Agent':
           'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}


# CHANGE the fields as the comments say  
def main(limit):
    for i in range(1, limit+1):
        num = getrandbits(40)
        firstname = 'your name{}'.format(num) # put your name here, don't remove the {}
        lastname = 'your name{}'.format(num) # put your name here, don't remove the {}
        phone = 'cekk'
        email = 'your_email+{}@gmail.com'.format(num) # CHANGE YOUR_EMAIL to your email prefix. don't change the +{} after.
        payload = {
            'action': 'contest',
            'email': email,
            'first name': firstname,
            'last name': lastname,
            'phone number': phone,
            'size': '10', # change your size
        }
        resp = requests.post(url, data=payload, headers=headers)
        print('{}/{} registered.'.format(i, limit))

if __name__ == "__main__":
    x = int(raw_input("How many entries do you want: "))
    main(x)


