import traceback
from os import listdir
import discord, asyncio
import lib.rpc_json as rpc_json
from discord.ext import commands
from os.path import isfile, join
import lib.utility_func as utility_func

client = commands.Bot(command_prefix='$', description="Discord Airdrop bot")
client.remove_command('help')  # replaced with $cmd

async def currentBlockHeight():
    while not client.is_closed():
        try:
            await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f"Block Height: {rpc_json.getTotalBlocks()}"))
            await asyncio.sleep(60)
        except Exception as currBlockHeight_err:
            print (f"Exception raised: currentBlockHeight - {currBlockHeight_err}")
            await asyncio.sleep(60)

@client.event
async def on_ready():
    print('BitGreen airdrop client starting')
    print('[>>] %s' % (client.user.name))
    print('[>>] %s' % (client.user.id))
    await client_extensions()
    client.loop.create_task(currentBlockHeight())

async def client_extensions():
    for extension in [f.replace(".py", "") for f in listdir("cogs") if isfile(join("cogs", f))]:
        try:
            if not "__init__" in extension:
                print("[++] loading extension: {}".format(extension))
                client.load_extension("cogs.%s" % (extension))
        except Exception as e:
            print ("[!!] failed to load extension {}".format(extension))
            traceback.print_exc()

if __name__ == '__main__':
    client.run(utility_func.load_json('./config/authenticate.json')['discord-code'])
