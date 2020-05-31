import lib.cron as cron
from discord.ext import commands
import lib.utility_func as utility_func

roles = utility_func.load_json('./config/roles.json')['discord-roles']

class cronJob_commands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.config = utility_func.load_json('./config/setup.json')
        self.twitter = utility_func.load_json('./config/twitter-config.json')
        self.color = 0x1e7180
        self.error = 0xcc0000

    @commands.command()
    @commands.has_any_role(*roles)
    async def setup_batch_cron(self, ctx):
        cron.create_cronjob()

    @commands.command()
    @commands.has_any_role(*roles)
    async def enable_batch_airdrop(self, ctx):
        cron.enable_batch_airdrop()

    @commands.command()
    @commands.has_any_role(*roles)
    async def disable_batch_airdrop(self, ctx):
        cron.disable_batch_airdrop()

def setup(bot):
    bot.add_cog(cronJob_commands(bot))