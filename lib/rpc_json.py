from bitcoinrpc.authproxy import AuthServiceProxy

recipients = {}

class wallet_rpc(object):
    def connect(self):
        try:
            return AuthServiceProxy("http://%s:%s@127.0.0.1:8331" % ('discordairdrop1', 'discordairdrop1'),timeout=120)
        except BrokenPipeError:
            return AuthServiceProxy("http://%s:%s@127.0.0.1:8331" % ('discordairdrop1', 'discordairdrop1'), timeout=120)

wallet = wallet_rpc()

# add participant to the airdrop.
def addParticipant(address, amount):
    recipients[address] = amount

# validate the address a user gives is valid and not invalid.
def validateaddress(address):
    try:
        return wallet.connect().validateaddress(address)
    except Exception as rpc_error:
        return rpc_error
    
def getinfo():
    try:
        return wallet.connect().getblockchaininfo()
    except Exception as rpc_error:
        return rpc_error

# total amount of blocks
def getTotalBlocks():
    try:
        return wallet.connect().getblockcount()
    except Exception as rpc_error:
        return rpc_error

# get wallet balance
def getBalance():
    try:
        return wallet.connect().getbalance()
    except Exception as rpc_error:
        return rpc_error

# get wallet address
def getAddress():
    try:
        return wallet.connect().getnewaddress()
    except Exception as rpc_error:
        return rpc_error

# check confirmations
def txConfirmation():
    try:
        last_confirmed_tx = len(wallet.connect().listtransactions()) - 1
        return wallet.connect().listtransactions()[last_confirmed_tx]['confirmations']
    except Exception as rpc_error:
        return rpc_error

# get transaction id that awaits confirmation
def txId():
    try:
        last_confirmed_tx = len(wallet.connect().listtransactions()) - 1
        return wallet.connect().listtransactions()[last_confirmed_tx]['txid']
    except Exception as rpc_error:
        return rpc_error

# send tokens from account
def sendCoins():
    try:
        return wallet.connect().sendmany('', recipients, 16)
    except Exception as rpc_error:
        return rpc_error

# clear recipients
def clearRecipients():
    recipients.clear()