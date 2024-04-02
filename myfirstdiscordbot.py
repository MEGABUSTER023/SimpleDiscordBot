try:
    import time
    import asyncio

    import aiohttp.client_exceptions
    import discord
    from better_profanity import profanity
    from discord.ext import commands
    from datetime import datetime
    from discord.utils import get
    import os
    from dotenv import load_dotenv
    from testchat import predict, get_response, intents
    from calculation import Calculator
    import base64
    from deepl import DeepLCLI
    deepl = DeepLCLI("auto", "en")
    import re
    from colorama import init, Fore, Back, Style

    init(convert=True)

    def Find(string):
        try:
            regex = r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))"
            url = re.findall(regex, string)
            return [x[0] for x in url]
        except Exception as c:
            print(Fore.RED + f"Something Went Wrong In The Find Section: Error Message Was: {c}")
            print(Fore.WHITE)

    load_dotenv('.env')
    decode = os.getenv('KEY')
    base64_message = decode
    message_bytes = base64.b64decode(base64_message)
    KEY = message_bytes.decode('utf-8')

    intent = discord.Intents.all()
    bot = commands.Bot(command_prefix='!', intents=intent)
    bot.remove_command('help')
    bot_start_time = datetime.now()

    @bot.event
    async def on_ready():
        try:
            print(Fore.GREEN, '{0.user} is up and running'.format(bot))
            print(Fore.GREEN, bot_start_time)
            print(Fore.WHITE)
            await bot.change_presence(activity=discord.Game(name="Ingenting"))
            while True:
                await asyncio.sleep(10)
                with open("Spam_Detect.txt", 'r+') as file:
                    file.truncate(0)
        except Exception as c:
            print(Fore.RED + f"Something Went Wrong In The OnReady Section: Error Message Was: {c}")
            print(Fore.WHITE)


    @bot.command()
    async def poweroff(ctx):
        try:
            Owner = discord.utils.get(ctx.guild.roles, name="Owner")
            Admin = discord.utils.get(ctx.guild.roles, name="Admin")
            Trainy_Admin = discord.utils.get(ctx.guild.roles, name="Trainy Admin")
            Helper = discord.utils.get(ctx.guild.roles, name="Helper")
            Trainy = discord.utils.get(ctx.guild.roles, name="Trainy")
            Member = discord.utils.get(ctx.guild.roles, name="Member")
            if Owner in ctx.author.roles:
                os.startfile("waiting.py")
                exit()
            else:
                await ctx.send(f"Du har ikke adgang til at bruge denne command", delete_after=60)
                print(Fore.CYAN, f"{ctx.author} has tried to use poweroff command but access was denied")
                print(Fore.WHITE)
        except Exception as c:
            print(Fore.RED + f"Something Went Wrong In The Poweroff Section: Error Message Was: {c}")
            print(Fore.WHITE)

    @bot.command()
    async def systemshutdown(ctx):
        try:
            Owner = discord.utils.get(ctx.guild.roles, name="Owner")
            Admin = discord.utils.get(ctx.guild.roles, name="Admin")
            Trainy_Admin = discord.utils.get(ctx.guild.roles, name="Trainy Admin")
            Helper = discord.utils.get(ctx.guild.roles, name="Helper")
            Trainy = discord.utils.get(ctx.guild.roles, name="Trainy")
            Member = discord.utils.get(ctx.guild.roles, name="Member")
            if Owner in ctx.author.roles:
                ctx.send(f"System Is Being Shut Down In 5 Minutes By {ctx.author}", delete_after=5)
                time.sleep(5)
                os.system("shutdown /s /t 1")
            else:
                pass
        except Exception as c:
            print(Fore.RED + f"Something Went Wrong In The Systemshutdown Section: Error Message Was: {c}")
            print(Fore.WHITE)

    @bot.command()
    async def systemrestart(ctx):
        try:
            Owner = discord.utils.get(ctx.guild.roles, name="Owner")
            Admin = discord.utils.get(ctx.guild.roles, name="Admin")
            Trainy_Admin = discord.utils.get(ctx.guild.roles, name="Trainy Admin")
            Helper = discord.utils.get(ctx.guild.roles, name="Helper")
            Trainy = discord.utils.get(ctx.guild.roles, name="Trainy")
            Member = discord.utils.get(ctx.guild.roles, name="Member")
            if Owner in ctx.author.roles:
                ctx.send(f"System Is Being Restarted In 5 Minutes By {ctx.author}", delete_after=5)
                time.sleep(5)
                os.system("shutdown -t 0 -r -f")
            else:
                pass
        except Exception as c:
            print(Fore.RED + f"Something Went Wrong In The Find Systemrestart: Error Message Was: {c}")
            print(Fore.WHITE)

    @bot.command(pass_context=True)
    async def newstat(ctx, *, strings: str):
        try:
            Owner = discord.utils.get(ctx.guild.roles, name="Owner")
            Admin = discord.utils.get(ctx.guild.roles, name="Admin")
            Trainy_Admin = discord.utils.get(ctx.guild.roles, name="Trainy Admin")
            Helper = discord.utils.get(ctx.guild.roles, name="Helper")
            Trainy = discord.utils.get(ctx.guild.roles, name="Trainy")
            Member = discord.utils.get(ctx.guild.roles, name="Member")
            string = strings.lower()
            if Admin in ctx.author.roles or Trainy_Admin in ctx.author.roles:
                if Owner in ctx.author.roles:
                    await bot.change_presence(activity=discord.Game(name=string))
                    await ctx.send(f"Status skifted til Spiller {string}", delete_after=60)
                    print(Fore.CYAN, f"Bot Status has been changed by {ctx.author} to Playing {string}")
                    print(Fore.WHITE)
                else:
                    if profanity.contains_profanity(string):

                        import datetime
                        minutes = 1
                        duration = datetime.timedelta(minutes=minutes)
                        await ctx.timeout(duration)
                        await ctx.send(f"{ctx.mention} er blevet timed out i {minutes} for at prøve at lave om på bot status til noget grimt",
                                       delete_after=60)
                        print(Fore.CYAN, f"{ctx.author} was timed out for {minutes} minutes by {ctx.author}")
                        print(Fore.WHITE)
                    else:
                        await bot.change_presence(activity=discord.Game(name=string))
                        await ctx.send(f"Status skifted til Spiller {string}", delete_after=60)
                        print(Fore.CYAN, f"Bot Status has been changed by {ctx.author} to Playing {string}")
                        print(Fore.WHITE)
            else:
                await ctx.send(f"Du har ikke adgang til at bruge denne command", delete_after=60)
                print(Fore.CYAN, f"{ctx.author} has tried to change status to {string} but access was denied")
                print(Fore.WHITE)

        except Exception as c:
            print(Fore.RED + f"Something Went Wrong In The Newstat Section: Error Message Was: {c}")
            print(Fore.WHITE)

    @bot.command(pass_context=True)
    async def chat(ctx, *, messages: str):
        try:
            message = messages.lower()
            if message == bot.user:
                return
            x = deepl.translate(message)
            ints = predict(x)
            res = get_response(ints, intents)
            with open('user_data.txt', 'w') as file:
                file.write(f"User: {message}" + '\n')
                file.write(f"Bot: {res}" + '\n')
            await ctx.channel.send(res, delete_after=60)
        except Exception as c:
            print(Fore.RED + f"Something Went Wrong In The Chat Section: Error Message Was: {c}")
            print(Fore.WHITE)

    @bot.command()
    async def timeout(ctx, member: discord.Member, minutes: int):
        try:
            Owner = discord.utils.get(ctx.guild.roles, name="Owner")
            Admin = discord.utils.get(ctx.guild.roles, name="Admin")
            Trainy_Admin = discord.utils.get(ctx.guild.roles, name="Trainy Admin")
            Helper = discord.utils.get(ctx.guild.roles, name="Helper")
            Trainy = discord.utils.get(ctx.guild.roles, name="Trainy")
            Member = discord.utils.get(ctx.guild.roles, name="Member")
            if Admin in ctx.author.roles or Helper in ctx.author.roles or Trainy_Admin in ctx.author.roles:
                import datetime
                duration = datetime.timedelta(minutes=minutes)
                await member.timeout(duration)
                await ctx.send(f"{member.mention} er blevet timed out i {minutes} minutter af {ctx.auhor}", delete_after=60)
                print(Fore.CYAN, f"{member} was timed out for {minutes} minutes by {ctx.author}")
                print(Fore.WHITE)
            else:
                await ctx.send("Du har ikke adgang til at bruge denne command", delete_after=60)
                print(Fore.CYAN, f"{ctx.author} tried to use Timeout Command")
                print(Fore.WHITE)
        except Exception as c:
            print(Fore.RED + f"Something Went Wrong In The Timeout Section: Error Message Was: {c}")
            print(Fore.WHITE)

    @bot.command()
    async def kick(ctx, member: discord.Member, *, reason=None):
        try:
            Owner = discord.utils.get(ctx.guild.roles, name="Owner")
            Admin = discord.utils.get(ctx.guild.roles, name="Admin")
            Trainy_Admin = discord.utils.get(ctx.guild.roles, name="Trainy Admin")
            Helper = discord.utils.get(ctx.guild.roles, name="Helper")
            Trainy = discord.utils.get(ctx.guild.roles, name="Trainy")
            Member = discord.utils.get(ctx.guild.roles, name="Member")
            if Admin in ctx.author.roles or Trainy_Admin in ctx.author.roles:
                print(Fore.YELLOW, f"{ctx.author} used kick command")
                print(Fore.WHITE)
                if reason == None:
                    reason = "Ingen grund var fremsat"
                await ctx.guild.kick(member)
                await ctx.send(f"user {member.mention} has been kicked for {reason}", delete_after=60)
            else:
                await ctx.send("Du har ikke adgang til at bruge denne command", delete_after=60)
                print(Fore.YELLOW, f"{ctx.author} tried to use Kick Command")
                print(Fore.WHITE)
        except Exception as c:
            print(Fore.RED + f"Something Went Wrong In The Kick Section: Error Message Was: {c}")
            print(Fore.WHITE)

    @bot.command()
    async def ban(ctx, member: discord.Member, *, reason=None):
        try:
            Bot_Command_Channel = bot.get_channel(1096374409784197202)

            Owner = discord.utils.get(ctx.guild.roles, name="Owner")
            Admin = discord.utils.get(ctx.guild.roles, name="Admin")
            Trainy_Admin = discord.utils.get(ctx.guild.roles, name="Trainy Admin")
            Helper = discord.utils.get(ctx.guild.roles, name="Helper")
            Trainy = discord.utils.get(ctx.guild.roles, name="Trainy")
            Member = discord.utils.get(ctx.guild.roles, name="Member")
            if Admin in ctx.author.roles:
                print(Fore.RED, f"{ctx.author} used ban command")
                print(Fore.WHITE)
                if reason == None:
                    reason = "Ingen grund var fremsat"
                await ctx.guild.ban(member)
                await ctx.send(f"@everyone Bruger {member.author.mention} er blevet banned for {reason}", delete_after=60)
                print(Fore.RED, f"Bruger {member.author} er blevet banned af {ctx.author} for {reason}")
                print(Fore.WHITE)
            else:
                await ctx.send("Du har ikke adgang til at bruge denne command", delete_after=60)
                print(Fore.RED, f"{ctx.author} tried to use Ban Command")
                print(Fore.WHITE)
        except Exception as c:
            print(Fore.RED + f"Something Went Wrong In The Ban Section: Error Message Was: {c}")
            print(Fore.WHITE)

    @bot.command()
    async def calc(ctx, calculate: str):
        try:
            Bot_Calculate_Channel = bot.get_channel(1096375876255486002)
            if ctx.channel.id == Bot_Calculate_Channel:
                calcs = calculate.lower()
                print(Fore.CYAN, f"{ctx.author} used calc command")
                print(Fore.WHITE)
                try:
                    try:
                        try:
                            c = Calculator()
                            out = c.calculate(calcs)
                            await ctx.send(out, delete_after=60)
                        except Exception:
                            await ctx.send("Noget Gik Galt", delete_after=60)
                    except NameError:
                        await ctx.send("Noget Gik Galt", delete_after=60)
                except ValueError:
                    await ctx.send("Nummeret er for stort", delete_after=60)
            else:
                await ctx.send(f"Du kan ikke skrive commands i denne kanal", delete_after=60)
                print(Fore.CYAN,
                      f"{ctx.author} has tried to use calc command but wasn't using the right channel")
                print(Fore.WHITE)

        except Exception as c:
            print(Fore.RED + f"Something Went Wrong In The Calc Section: Error Message Was: {c}")
            print(Fore.WHITE)

    @bot.command()
    async def unban(ctx, user_id : int):
        try:
            Bot_Command_Channel = bot.get_channel(1096374409784197202)

            Owner = discord.utils.get(ctx.guild.roles, name="Owner")
            Admin = discord.utils.get(ctx.guild.roles, name="Admin")
            Trainy_Admin = discord.utils.get(ctx.guild.roles, name="Trainy Admin")
            Helper = discord.utils.get(ctx.guild.roles, name="Helper")
            Trainy = discord.utils.get(ctx.guild.roles, name="Trainy")
            Member = discord.utils.get(ctx.guild.roles, name="Member")
            if Admin in ctx.author.roles:
                print(Fore.CYAN, f"{ctx.author} used unban command")
                print(Fore.WHITE)
                user = await ctx.client.fetch_user(user_id)
                await ctx.guild.unban(user)
                await ctx.send(f"bruger {ctx.mention} er blevet unbanned af {ctx.author.mention}", delete_after=60)
                print(Fore.CYAN, f"{ctx.author} has unbanned {ctx.mention}")
                print(Fore.WHITE)
            else:
                await ctx.send("Du har ikke adgang til at bruge denne command", delete_after=60)
                print(Fore.CYAN, f"{ctx.author} tried to use Unban Command")
                print(Fore.WHITE)

        except Exception as c:
            print(Fore.RED + f"Something Went Wrong In The Calc Section: Error Message Was: {c}")
            print(Fore.WHITE)


    @bot.command()
    async def help(ctx):
        try:
            Bot_Command_Channel = bot.get_channel(1096374409784197202)
            if ctx.channel.id == Bot_Command_Channel:
                embed = discord.Embed(title="Bot Commands", description="Some Useful Commands   ")
                embed.add_field(name="!clear", value="Du kan bruge clear til at rydde chats som vist her !clear 1 < antal linjer at rydde. Rank for at bruge --> (Owner, Admin, Trainy Admin, Helper)")
                embed.add_field(name="!ban", value="Du kan bruge ban til at banne folk som vist her !ban @person. Rank for at bruge --> (Owner, Admin)")
                embed.add_field(name="!kick", value="Du kan bruge kick til at kicke folk som vist her !kick @person. Rank for at bruge --> (Owner, Admin, Trainy Admin)")
                embed.add_field(name="!timeout", value="Du kan bruge timeout til at timeout personer som vist her !timeout @person 1 < et minut. Rank for at bruge --> (Owner, Admin, Trainy Admin, Helper)")
                embed.add_field(name="!unban", value="Du kan bruge unban til at unbanne personer som vist her !unban @person. Rank for at bruge --> (Owner, Admin)")
                embed.add_field(name="!clearall", value="Du kan bruge clearall til at rydde alt i chatten, som der så der på som vist her !clearall. Rank for at bruge --> (Owner, Admin, Trainy Admin)")
                embed.add_field(name="!newstat", value="Du kan bruge newstat til at vælge bottens status som vist her !newstat Minecraft (Owner, Admin, Trainy Admin, Helper)")
                embed.add_field(name="!calc", value="Du kan bruge calc til at regne ting ud som vist her !calc 1+1 = 2")
                embed.add_field(name="!chat", value="Du kan bruge chat til at tale med en artifical inteligent den er ikke særlig klog men du kan godt tale med den som vist her !chat Hi")
                await ctx.send(embed=embed, delete_after=60)
                print(Fore.CYAN, f"{ctx.author} used help command")
                print(Fore.WHITE)
            else:
                await ctx.send(f"Du kan ikke skrive commands i denne kanal", delete_after=60)
                print(Fore.CYAN,
                      f"{ctx.author} has tried to use help command but wasn't using the right channel")
                print(Fore.WHITE)

        except Exception as c:
            print(Fore.RED + f"Something Went Wrong In The Help Section: Error Message Was: {c}")
            print(Fore.WHITE)

    @bot.command()
    async def clear(ctx, amount: int):
        try:
            Bot_Command_Channel = bot.get_channel(1096374409784197202)

            Owner = discord.utils.get(ctx.guild.roles, name="Owner")
            Admin = discord.utils.get(ctx.guild.roles, name="Admin")
            Trainy_Admin = discord.utils.get(ctx.guild.roles, name="Trainy Admin")
            Helper = discord.utils.get(ctx.guild.roles, name="Helper")
            Trainy = discord.utils.get(ctx.guild.roles, name="Trainy")
            Member = discord.utils.get(ctx.guild.roles, name="Member")
            if Helper in ctx.author.roles or Admin in ctx.author.roles or Trainy_Admin in ctx.author.roles:
                amount += 1
                print(Fore.YELLOW, f"{ctx.author} used clear command")
                print(Fore.WHITE)
                await ctx.channel.purge(limit=amount)
            else:
                await ctx.send("Du har ikke adgang til at bruge denne command", delete_after=60)
                print(Fore.YELLOW, f"{ctx.author} tried to use Timeout Command")
                print(Fore.WHITE)
        except Exception as c:
            print(Fore.RED + f"Something Went Wrong In The Clear Section: Error Message Was: {c}")
            print(Fore.WHITE)

    @bot.command()
    async def clearall(ctx):
        try:
            Bot_Command_Channel = bot.get_channel(1096374409784197202)

            Owner = discord.utils.get(ctx.guild.roles, name="Owner")
            Admin = discord.utils.get(ctx.guild.roles, name="Admin")
            Trainy_Admin = discord.utils.get(ctx.guild.roles, name="Trainy Admin")
            Helper = discord.utils.get(ctx.guild.roles, name="Helper")
            Trainy = discord.utils.get(ctx.guild.roles, name="Trainy")
            Member = discord.utils.get(ctx.guild.roles, name="Member")
            if Helper in ctx.author.roles or Admin in ctx.author.roles or Trainy_Admin in ctx.author.roles:
                print(Fore.YELLOW, f"{ctx.author} used clearall command")
                print(Fore.WHITE)
                await ctx.channel.purge(limit=100000**100000)
            else:
                await ctx.send("Du har ikke adgang til at bruge denne command", delete_after=60)
                print(Fore.YELLOW, f"{ctx.author} tried to use Timeout Command")
                print(Fore.WHITE)
        except Exception as c:
            print(Fore.RED + f"Something Went Wrong In The Clearall Section: Error Message Was: {c}")
            print(Fore.WHITE)

    @bot.event
    async def on_message(ctx):
        try:
            guild = ctx.guild
            if not guild:
                pass
            else:
                unspervised_chat = 1082654209490563113
                url_chat = 1084936805666799767
                minecraft_rule_channel = 1085233115884179596

                Owner = discord.utils.get(ctx.guild.roles, name="Owner")
                Admin = discord.utils.get(ctx.guild.roles, name="Admin")
                Trainy_Admin = discord.utils.get(ctx.guild.roles, name="Trainy Admin")
                Helper = discord.utils.get(ctx.guild.roles, name="Helper")
                Trainy = discord.utils.get(ctx.guild.roles, name="Trainy")
                if ctx.author == bot.user:
                    return
                if Owner in ctx.guild.roles:
                    pass
                else:
                    counter = 0
                    with open('Spam_Detect.txt', 'r+') as file:
                        for line in file:
                            if line.strip("\n") == str(ctx.author.id):
                                counter += 1
                        file.writelines(f"{str(ctx.author.id)}\n")
                        if counter > 5:
                            minutes = 5
                            import datetime
                            duration = datetime.timedelta(minutes=minutes)
                            await ctx.channel.purge(limit=counter)
                            await ctx.timeout(duration)
                            await ctx.channel.send(f"{ctx.author.mention} er blevet timed out i {minutes} minutter for at spamme", delete_after=30)
                            print(Fore.CYAN, f"{ctx.author} was timed out for {minutes} minutes for spamming")
                            print(Fore.WHITE)

                if profanity.contains_profanity(ctx.content):
                    if ctx.channel.id == unspervised_chat:
                        pass
                    else:
                        await ctx.channel.send(f"{ctx.author.mention} Opfør dig Ordenligt. Din konsikvens er at du bliver Timeouted i 1 minute", delete_after=10)
                        await ctx.delete()
                        import datetime
                        minutes = 1
                        duration = datetime.timedelta(minutes=minutes)
                        await ctx.author.timeout(duration)
                        await ctx.channel.send(f"{ctx.author.mention} blev timedout i {minutes} minutter", delete_after=60)
                        print(Fore.CYAN, f"{ctx.author} blev timedout i {minutes} minutter")
                        print(Fore.WHITE)
                else:
                    url_check = Find(ctx.content)
                    if url_check:
                        if ctx.channel.id == url_chat:
                            pass
                        else:
                            await ctx.delete()
                            print(Fore.CYAN, f"{ctx.author} tried to send a Link")
                            print(Fore.WHITE)
                            await ctx.channel.send(f"{ctx.author.mention} Hver Sød At Skrive Links I Url Chatten", delete_after=30)
                    else:
                        pass

                if profanity.contains_profanity(ctx.content):
                    if ctx.channel.id == unspervised_chat:
                        pass
                    else:
                        if Owner in ctx.author.roles:
                            pass
                        else:
                            await ctx.channel.send(f"{ctx.author.mention} Opfør dig Ordenligt. Din konsikvens er at du bliver Timeouted i 1 minute", delete_after=10)
                            await ctx.delete()
                            import datetime
                            minutes = 1
                            duration = datetime.timedelta(minutes=minutes)
                            await ctx.author.timeout(duration)
                            await ctx.channel.send(f"{ctx.author.mention} blev timedout i {minutes} minutter", delete_after=60)
                            print(Fore.CYAN, f"{ctx.author} blev timedout i {minutes} minutter")
                            print(Fore.WHITE)
                else:
                    if Owner in ctx.author.roles:
                        pass
                    else:
                        translated = x = deepl.translate(ctx.content)
                        if translated == None:
                            pass
                        else:
                            if profanity.contains_profanity(translated):
                                await ctx.channel.send(
                                    f"{ctx.author.mention} Opfør dig Ordenligt. Din konsikvens er at du bliver Timeouted i 1 minute",
                                    delete_after=10)
                                await ctx.delete()
                                import datetime
                                minutes = 1
                                duration = datetime.timedelta(minutes=minutes)
                                await ctx.author.timeout(duration)
                                await ctx.channel.send(f"{ctx.author.mention} blev timedout i {minutes} minutes", delete_after=60)



                await bot.process_commands(ctx)
        except Exception as c:
            print(Fore.RED + f"Something Went Wrong In The OnMessage Section Error Message Was: {c}")
            print(Fore.WHITE)

    @bot.event
    async def on_member_join(member):
        try:
            guild = bot.get_guild(1077856444700950588) # Everyone Role ID
            channel = guild.get_channel(1077926167438426122) # Welcome Channel ID
            await channel.send(f"Velkommen til serveren {member.mention} ! :partying_face:")
            role = get(member.guild.roles, name='Member')
            await member.add_roles(role)
        except Exception as c:
            print(Fore.RED + f"Something Went Wrong In The On_Member_Join Section: Error Message Was: {c}")
            print(Fore.WHITE)

    @bot.event
    async def on_message_delete(message):
        try:
            z = bot.get_channel(1077972743770878063) # Log Channel ID
            embed = discord.Embed(title=f"{message.author}'s Message was Deleted", description=f"Deleted Message: {message.content}\nAuthor: {message.author.mention}\nLocation: {message.channel.mention}", timestamp=datetime.now(), color=discord.Color.red())
            embed.set_author(name=message.author.name, icon_url=message.author.display_avatar)
            await z.send(embed=embed)
        except Exception as c:
            print(Fore.RED + f"Something Went Wrong In The On_Message_Delete Section: Error Message Was: {c}")
            print(Fore.WHITE)

    @bot.event
    async def on_message_edit(before, after):
        try:
            from datetime import datetime

            unspervised_chat = 1082654209490563113
            url_chat = 1084936805666799767
            minecraft_rule_channel = 1085233115884179596

            Owner = discord.utils.get(before.guild.roles, name="Owner")
            Admin = discord.utils.get(before.guild.roles, name="Admin")
            Trainy_Admin = discord.utils.get(before.guild.roles, name="Trainy Admin")
            Helper = discord.utils.get(before.guild.roles, name="Helper")
            Trainy = discord.utils.get(before.guild.roles, name="Trainy")

            z = bot.get_channel(1077972743770878063) # Log Channel ID
            embed = discord.Embed(title=f"{before.author}'s Edited Their Message",
                                  description=f"Before: {before.content}\nAfter: {after.content}\nAuther: {before.author.mention}\nLocation: {before.channel.mention}\nLocation",
                                  timestamp=datetime.now(), color=discord.Color.blue())
            embed.set_author(name=after.author.name, icon_url=after.author.display_avatar)
            await z.send(embed=embed)
            if profanity.contains_profanity(before.content):
                if before.channel.id == unspervised_chat:
                    pass
                else:
                    if Owner in before.author.roles:
                        pass
                    else:
                        await before.channel.send(
                            f"{before.author.mention} Opfør dig Ordenligt. Din konsikvens er at du bliver Timeouted i 1 minute",
                            delete_after=10)
                        await before.delete()
                        import datetime
                        minutes = 1
                        duration = datetime.timedelta(minutes=minutes)
                        await before.author.timeout(duration)
                        await before.channel.send(f"{before.author.mention} blev timedout i {minutes} minutter",
                                               delete_after=60)
                        print(Fore.CYAN, f"{before.author} blev timedout i {minutes} minutter")
                        print(Fore.WHITE)
            else:
                if Owner in before.author.roles:
                    pass
                else:
                    translated = deepl.translate(before.content)
                    if translated == None:
                        pass
                    else:
                        if profanity.contains_profanity(translated):
                            await before.channel.send(
                                f"{before.author.mention} Opfør dig Ordenligt. Din konsikvens er at du bliver Timeouted i 1 minute",
                                delete_after=10)
                            await before.delete()
                            import datetime
                            minutes = 1
                            duration = datetime.timedelta(minutes=minutes)
                            await before.author.timeout(duration)
                            await before.channel.send(f"{before.author.mention} blev timedout i {minutes} minutes",
                                                   delete_after=60)
        except Exception as c:
            print(Fore.RED + f"Something Went Wrong In The On_Message_Edit Section: Error Message Was: {c}")
            print(Fore.WHITE)


    @bot.event
    async def on_member_update(ctx, after):
        try:
            global embed
            z = bot.get_channel(1077972743770878063) # Log Channel ID
            if len(ctx.roles) > len(after.roles):
                role = next(role for role in ctx.roles if role not in after.roles)
                embed = discord.Embed(title=f"{ctx}'s Role has been Removed", description=f"{role.name} was removed from {ctx.mention}", timestamp=datetime.now(), color=discord.Color.red())
            elif len(after.roles) > len(ctx.roles):
                role = next(role for role in after.roles if role not in ctx.roles)
                embed = discord.Embed(title=f"{ctx}'s Got a new role",
                                      description=f"{role.name} was added to {ctx.mention}",
                                      timestamp=datetime.now(), color=discord.Color.green())
            elif ctx.nick != after.nick:
                nickname = deepl.translate(after.nick)
                if profanity.contains_profanity(nickname.lower()):
                    await ctx.edit(nick=ctx.nick)
                else:
                    embed = discord.Embed(title=f"{ctx}'s Nickname changed",
                                          description=f"{ctx.nick}\nAfter: {after.nick}",
                                          timestamp=datetime.now(), color=discord.Color.blue())
            else:
                return
            embed.set_author(name=after.name, icon_url=after.display_avatar)
            await z.send(embed=embed)
        except Exception as c:
            print(Fore.RED + f"Something Went Wrong In The On_Member_Update Section: Error Message Was: {c}")
            print(Fore.WHITE)

    bot.run(KEY)
except Exception as c:
    print(Fore.RED + f"Something Went Wrong In The Startup of the Script: Error Message Was: {c}")
    print(Fore.WHITE)