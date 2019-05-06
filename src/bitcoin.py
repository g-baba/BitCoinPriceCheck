import requests
import json

coins = [
            [1,  'BTC',  'btc_jpy'],
            [2,  'ETH',  'eth_jpy'],
            [3,  'ETC',  'etc_jpy'],
#            [4,  'DAO',  'dao_jpy'], Not available
            [5,  'LSK',  'lsk_jpy'],
            [6,  'FCT',  'fct_jpy'],
#            [7,  'XMR',  'xmr_jpy'], Not available
#            [8,  'REP',  'rep_jpy'], Not available
            [9,  'XRP',  'xrp_jpy'],
#            [10, 'ZEC',  'zec_jpy'], Not available
            [11, 'XEM',  'xem_jpy'],
            [12, 'LTC',  'ltc_jpy'],
#            [13, 'DASH', 'dash_jpy'], Not available
            [14, 'BCH',  'bch_jpy'],
        ]

urlbase = 'https://coincheck.com/api/rate/'

def main():
    for i in range(len(coins)):
        response = requests.get(urlbase+coins[i][2])
        if response.status_code != 200:
            raise Exception('return status code is {}'.format(response.status_code))

        rate = json.loads(response.text)

        print("%-4s : \%-10s" % (coins[i][1], rate['rate']))

if __name__ == "__main__":
    main()
