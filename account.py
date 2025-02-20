# -*- coding:utf-8 -*-
"""
# Author: Rocky Zhao
# Time: 2024/7/29 11:12
"""
from utils.request_util import BaseMethod
from config.api_key import api_key


class AccountTest(object):
    def __init__(self):
        self.__api_key = api_key()['__api_key']
        self.__secret_key = api_key()['__secret_key']
        self.__passphrase = api_key()['__passphrase']
        self.host = api_key()['host']

    def get_account_balance(self, uri='/deepcoin/account/balances'):
        params = {}
        params['instType'] = 'SWAP'
        account_balance_request = BaseMethod(self.__api_key, self.__secret_key, self.__passphrase, self.host, uri, 'GET')
        r = account_balance_request.request_app(params)
        return r

    def get_account_positions(self, uri='/deepcoin/account/positions'):
        params = {}
        params['instType'] = 'SWAP'

        account_positions_handler = BaseMethod(self.__api_key, self.__secret_key, self.__passphrase, self.host, uri, 'GET')
        r = account_positions_handler.request_app(params)
        return r

    def post_set_leverage(self, inst_id, uri='/deepcoin/account/set-leverage'):
        params = {}
        params['instId'] = inst_id
        params['lever'] = '10'
        params['mgnMode'] = 'cross'
        params['mrgPosition'] = 'merge'

        set_leverage_handler = BaseMethod(self.__api_key, self.__secret_key, self.__passphrase, self.host, uri, 'POST')
        r = set_leverage_handler.request_app(params)
        return r


if __name__ == "__main__":
    account_test = AccountTest()
    account_test.get_account_balance()
