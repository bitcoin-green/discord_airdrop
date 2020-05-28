from bitcoinrpc.authproxy import AuthServiceProxy

recipients = {}

class Rpc(object):
    def connect(self):
        try:
            return AuthServiceProxy("http://%s:%s@127.0.0.1:8331" % ('discordairdrop1', 'discordairdrop1'),timeout=120)
        except BrokenPipeError:
            return AuthServiceProxy("http://%s:%s@127.0.0.1:8331" % ('discordairdrop1', 'discordairdrop1'), timeout=120)

rpc = Rpc()

# add participant to the airdrop.
def addParticipant(address, amount):
    recipients[address] = amount

# validate the address a user gives is valid and not invalid.
def validateaddress(address):
    return rpc.connect().validateaddress(address)

def getinfo():
    return rpc.connect().getblockchaininfo()

# total amount of blocks
def getTotalBlocks():
    return rpc.connect().getblockcount()

# get wallet balance
def getBalance():
    return rpc.connect().getbalance()

# get wallet address
def getAddress():
    return rpc.connect().getnewaddress()

# check confirmations
def txConfirmation():
    last_confirmed_tx = len(rpc.connect().listtransactions()) - 1
    return rpc.connect().listtransactions()[last_confirmed_tx]['confirmations']

# get transaction id that awaits confirmation
def txId():
    last_confirmed_tx = len(rpc.connect().listtransactions()) - 1
    return rpc.connect().listtransactions()[last_confirmed_tx]['txid']

# check confirmations
def test():
    return rpc.connect().listtransactions('', 1)[0]['confirmations']

# send tokens from account
def sendCoins():
    return rpc.connect().sendmany('', recipients, 16)

# clear recipients
def clearRecipients():
    recipients.clear()