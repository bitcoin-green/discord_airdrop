#!/usr/bin/env python3

import os, json
from datetime import datetime
import lib.rpc_json as rpc_json
import lib.utility_func as utility_func

class task():
    def __init__(self):
        self.relative_path = os.path.dirname(os.path.abspath(__file__))
        self.config = utility_func.load_json('%s/config/setup.json' % (self.relative_path))
        self.sent = utility_func.load_json('%s/data/persistent-sent.json' % (self.relative_path))
        self.airdropConf = utility_func.load_json('%s/data/current-airdrop.json' % (self.relative_path))
        self.wallet = utility_func.load_json('%s/config/wallet-config.json' % (self.relative_path))
        self.batch_log = '%s/batch-log.txt' % (self.relative_path)

    # debugging; log time each batch task has been completed
    def task_logging(self):
        batch_log = open(self.batch_log, 'a')
        batch_log.write('[%s] - Batch airdrop complete!\n' % (datetime.now()))

    def batch_airdrop(self):
        if self.airdropConf['twitter-bounty']:
            for user in self.airdropConf['airdrop-users']:
                self.sent['sent'].append(user)

            # "[1:]" added to remove . <- period from filepath
            update_sent = json.dumps(self.sent)
            utility_func.jsonfile(self.relative_path + self.config['sent'][1:], update_sent)

            if self.airdropConf['active']:
                if rpc_json.txConfirmation() >= self.wallet['confirmations']:
                    for user in self.airdropConf['airdrop-users']:
                        if len(self.airdropConf['airdrop-users']) == 0:
                            break
                        else:
                            rpc_json.addParticipant(user['address'], self.airdropConf['amount'])

                    # send transactions
                    rpc_json.sendCoins()
                    rpc_json.clearRecipients()

                    # change 'current-airdrop.json' by moving participants to 'persistent-sent.json'
                    self.airdropConf['airdrop-users'] = []
                    update_airdropConf = json.dumps(self.airdropConf)
                    utility_func.jsonfile(self.relative_path + self.config['airdrop'][1:], update_airdropConf)
                    self.task_logging()
                else:
                    print ("Not enough confirmations")
            else:
                print ("Not private, this shouldn't print. If it does.. something broke")
        else:
            print ("Airdrop isn't persistent.")

task().batch_airdrop()