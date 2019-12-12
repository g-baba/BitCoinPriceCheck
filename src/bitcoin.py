import requests
import json

coins = [
            [1,  'BTC',  'btc_jpy'],
            [2,  'XEM',  'xem_jpy'],
            [3,  'MONA', 'mona_jpy'],
        ]

urlbase = 'https://api.zaif.jp/api/1/last_price/'

def main():
    for i in range(len(coins)):
        response = requests.get(urlbase+coins[i][2])
        if response.status_code != 200:
            raise Exception('return status code is {}'.format(response.status_code))

        rate = json.loads(response.text)

        print("%-4s : \%-10s" % (coins[i][1], rate['last_price']))

if __name__ == "__main__":
    main()