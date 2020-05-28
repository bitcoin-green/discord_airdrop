import time
import discord
import asyncio
import traceback
import json
import lib.utility_func as utility_func
import lib.rpc_json as rpc_json
from os import listdir
from discord.ext import commands
from os.path import isfile, join

client = commands.Bot(command_prefix='$', description="Airdrop - Sending coins to all!")
client.remove_command('help')
thrdPartyAuthConfig = utility_func.load_json('./config/authenticate.json')
messages = 0

async def reset_message_activity(hrs):
    while not client.is_closed():
        try:
            msg_reset_24hr = {'discord-user': []}
            indent_data = json.dumps(msg_reset_24hr, indent=4)
            utility_func.jsonfile('./data/message_activity_24hr.json', indent_data)
            await asyncio.sleep(3600*hrs)
        except Exception as error:
            print (f"Exception raised: reset_message_activity()\nError:{error}")

async def currentBlockHeight():
    while not client.is_closed():
        try:
            await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f"Block Height: {rpc_json.getTotalBlocks()}"))
            await asyncio.sleep(60)
        except Exception as currBlockHeight_err:
            print (f"Exception raised: currentBlockHeight - {currBlockHeight_err}")

@client.event
async def on_ready():
    print('BitGreen airdrop client starting')
    print('[>>] %s' % (client.user.name))
    print('[>>] %s' % (client.user.id))
    await client_extensions()
    client.loop.create_task(currentBlockHeight())

@client.event
async def on_message(message):
    msgActivityLog = utility_func.load_json('./data/message_activity_24hr.json')
    tmp_ids = []

    for i in range(0, len(msgActivityLog['discord-user'])):
        for id in msgActivityLog['discord-user'][i].keys():
            tmp_ids.append(id)

    if not utility_func.check_duplicate(str(message.author.id), tmp_ids):
        msgActivityLog['discord-user'].append(({str(message.author.id):[{"messages": 1}]}))
        update = json.dumps(msgActivityLog)
        utility_func.jsonfile('./data/message_activity_24hr.json', update)
    else:
        if not '$join' in message.content:
            #print (f"User: {message.author.id}\nMessage: {message.content}\n-------")
            total_msg = msgActivityLog['discord-user'][tmp_ids.index(str(message.author.id))][str(message.author.id)][0]['messages']
            total_msg += 1
            msgActivityLog['discord-user'][tmp_ids.index(str(message.author.id))][str(message.author.id)][0]['messages'] = total_msg
            update = json.dumps(msgActivityLog)
            utility_func.jsonfile('./data/message_activity_24hr.json', update)

    await client.process_commands(message)

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
    try:
        client.run(thrdPartyAuthConfig['discord-code'])
    except BaseException:
        time.sleep(10)
        client.run(thrdPartyAuthConfig['discord-code'])