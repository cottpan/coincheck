import requests
import ast

"""
document: https://coincheck.com/documents/exchange/api
"""

base_url = "https://coincheck.com"
api_urls = { 'ticker'     : '/api/ticker',
             'trades'     : '/api/trades',
             'order_books': '/api/order_books',
             'rate_btc'   : '/api/rate/btc_jpy',
             'rate_eth'   : '/api/rate/eth_jpy',
             'rate_etc'   : '/api/rate/etc_jpy',
             'rate_dao'   : '/api/rate/dao_jpy',
             'rate_lsk'   : '/api/rate/lsk_jpy',
             'rate_fct'   : '/api/rate/fct_jpy',
             'rate_xmr'   : '/api/rate/xmr_jpy',
             'rate_rep'   : '/api/rate/rep_jpy',
             'rate_xrp'   : '/api/rate/xrp_jpy',
             'rate_zec'   : '/api/rate/zec_jpy',
             'rate_xem'   : '/api/rate/xem_jpy',
             'rate_ltc'   : '/api/rate/ltc_jpy',
             'rate_dash'  : '/api/rate/dash_jpy'
             }

class Market(object):
    def __init__(self):
        pass


    def public_api(self,url):
        ''' template function of public api'''
        try :
            url in api_urls
            return ast.literal_eval(requests.get(base_url + api_urls.get(url)).text)
        except Exception as e:
            print(e)

    def ticker(self):
        '''get latest information of coincheck market'''
        return self.public_api('ticker')

    def trades(self):
        '''get latest deal history of coincheck market'''
        return self.public_api('trades')

    def orderbooks(self):
        '''get latest asks/bids information of coincheck market'''
        return self.public_api('order_books')

    def rate(self, currency_pair):
        '''get latest currency rate of coincheck market'''
        return self.public_api('rate_' + currency_pair)


if __name__ == '__main__':
    pass
