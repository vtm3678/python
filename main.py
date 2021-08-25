import discord
from discord.ext import commands
import time
import random
import datetime
import asyncio
import aiohttp
import json
import requests
from keep_alive import keep_alive
import os
import tweepy
dnd = discord.Status.dnd
activity = discord.Game(name=f'+help')
bot_dev_id = 834974179085385728
client = commands.Bot(command_prefix = "+",status=dnd,activity=activity)
client.remove_command("help")
m = int(os.getenv("iaif"))
answers = [
    "As I see it, yes.", "Ask again later", " Better not tell you now.",
    "Cannot predict now", "Concentrate and ask again.", "Don’t count on it.",
    "You may rely on it.", "Yes – definitely.", " Yes.", " Without a doubt.",
    "Very doubtful.", " Signs point to yes.", "Reply hazy, try again",
    "Outlook good", "Outlook not so good.", "My sources say no.",
    "My reply is no.", "Most likely", "It is decidedly so", "It is certain"
]
quote_list =['Be like Gordon Ramsay- hate everyone equally','In this world, it\'s either yeet or be yeeted.','Everyone dies, but some people really should.','At a certain point, shut up.','It’s gotten to a point where I’m not even procrastinating anymore, I’m just jeopardizing my future.','You are not alone in the universe but none of the cool aliens want to hang out with you.','Instead of always focusing on your superficial differences, think of the things all people have in common, like the tendency to always focus on their superficial differences.','your honor I saw it on tiktok','your honor the light had been green for like five seconds','your honor I thought it\'d be funny','In order to move on, you must actually move on.','your honor it made sense at the time','What feels like losing control is actually your becoming more aware that you never had it.','Someone should do something about the Earth becoming uninhabitable, maybe.','Studies have shown that you’re dumb.','Artificial intelligence will never be a bigger threat to humanity than natural stupidity.','feeling in a very singing mood','I\'m so tired of deciding things ','Stop explaining yourself. Other people only understand from their level of perception','I dislike you.','Best feeling ever is realizing you don\'t care anymore.','Sometimes I don\'t agree with what i said 3 minutes ago.','It might be more effective to call it "weather change"."Climate change" is way too abstract for you dumb-asses.','Knowledge is knowing that a tomato is a fruit but wisdom is knowing not to mix it in a fruit salad.','You’re not as bad as your worst moment, but you aren’t as good as your best moment either. That kinda sucks.','Shit\'s all fucked up.','If u correct people\'s grammar u have a bad personality','shall i compare thee to a silly goose','I need vitamin Cᴬˢʰ','TIME FOR BED','I know it may not always seem that way but deep down, people are fundamentally stupid.','The more things change, the more they scare the shit out of everyone.','The climate keeps changing and people keep not.','Some days I wish I were Batman.','We really don\'t appreciate the fact that email is free.','The best thing about life is that it can always get worse.','I\'m not hiding anything but please don\'t touch my phone','`"are u ok"`- no, i need to get rich','Just get that tattoo, your parents are already disappointed in you','Stop making up quotes that I never said','Discord > Everything else. It\'s a proven fact.']
author_list = ['Gandhi','Socrates','Aristotle','Confucius','René Descartes','Karl Marx','Plato','Alexander The Great','Hippocrates','Albert Einstein','Abraham Lincoln','God.','Stephen Hawking','Isaac Newton','Neil deGrasse Tyson','Benjamin Franklin','Nelson Mandela','Elon Musk','Sun Tzu','Richard Dawkins','Charles Darwin','Carl Sagan','Jonathan Swift','William Shakespeare']
reaction_dict = {
'865603879148453928':'⛔',
'$todaytop':'<:spotify:848783829078769684>',
'$top50':'<:spotify:848783829078769684>',
'wynn':'<:hmm:848787605290221599>',
' 69 ':'<a:nice:848783089219403786>',
' 420 ':"<a:nice:848783089219403786>"
}
banned_ids = []
twtr_access_secret = os.getenv('twtr_access_secret')
twtr_auth_key = os.getenv('twtr_auth_key')
twtr_auth_secret = os.getenv('twtr_auth_secret')
twtr_access_token = os.getenv('twtr_access_token')
auth = tweepy.OAuthHandler(twtr_auth_key,twtr_auth_secret)
auth.set_access_token(twtr_access_token,twtr_access_secret)
api = tweepy.API(auth)
dev_id = os.getenv('dev_id')

@client.event
async def on_ready():
  print('Logged in as {0.user}'.format(client))

@client.event
async def on_member_join(member):
  try: 
    guild = member.guild
    await guild.system_channel.send(f'Welcome to {guild.name}, <@{member.id}>.')
  except:
    print('error: no systemchannel found??')
@client.event
async def on_member_remove(member):
  try:
    guild = member.guild
    await guild.system_channel.send(f'oof {member.name} left the server?')
  except:
    print('no system chhannel')
@client.event
async def on_guild_join(guild):
    bot_dev = await client.fetch_user(bot_dev_id)
    embed = discord.Embed(title='⚠ Event: Joined Guild',description=f'''
    Joined Guild **{guild.name}**
    Member Count: {guild.member_count}
    ID: `{guild.id}`
    Owner ID: {guild.owner_id}
    ''')
    embed.set_thumbnail(url=guild.icon_url)
    await bot_dev.send(embed=embed)
    await guild.system_channel.send('https://i.kym-cdn.com/entries/icons/original/000/034/581/Untitled-5.png')

@client.event
async def on_message(message):
    msga = message.author
    await client.process_commands(message)
    if msga == client.user:
        return
    msg = message.content
    if msga.bot == False:
      for reaction in reaction_dict.keys():
        if reaction in msg.lower():
          await message.add_reaction(reaction_dict.get(reaction))

@client.command()
async def prefix(ctx):
  await ctx.reply(f"The default prefix is `{client.command_prefix}`. Per-server prefixes aren't supported yet.")

@client.command()
async def poll(ctx):
  await ctx.reply("oof this command is still under development - we'll release it after perfecting it, sowee!")

@client.command()
@commands.has_permissions(manage_messages=True)
async def clear(ctx,amount=3):
  await ctx.send('<a:loading1:848783085982187550> Clearing Messages...')
  amount_actual = amount + 2
  await ctx.channel.purge(limit = amount_actual)
  await ctx.send('Messages cleared <a:done:848783086925905930>',delete_after=3.0)

@client.command()
async def predict(ctx,*,question=None):
  if question == None:
    await ctx.reply('Dude, I need a question to determine the answer. Don\'t be stupid.')
  else:
    await ctx.reply(random.choice(answers))


@client.command()
async def gif(ctx,*,search_term=None):
  if search_term == None:
    await ctx.reply('You tryna play games? Input a valid search term.')
  else:
    try:
      session = aiohttp.ClientSession()
      gif_embed = discord.Embed(title=f'Top gif for `{search_term}` on Giphy <a:giphy:864518958902935562>',colour=discord.Colour.blurple())
      api_key = os.getenv('giphy_api_key')
      response = await session.get(f'http://api.giphy.com/v1/gifs/search?q={search_term}&api_key={api_key}&limit=2')
      data = json.loads(await response.text())
      gif_embed.set_image(url=data['data'][0]['images']['original']['url'])
      gif_embed.set_thumbnail(url='https://image.ibb.co/b0Gkwo/Poweredby_640px_Black_Vert_Text.png')
      await session.close()
      await ctx.reply(embed=gif_embed)
    except:
      await ctx.reply(f'you have conquered giphy - apparently there\'s no gifs for "{search_term}"')

@client.command()
async def rm(ctx):
  if ctx.author.id == 834974179085385728:
    await ctx.guild.leave()
  else:
    embed = discord.Embed(description="You're using a forbidden/private command. Refrain from using it in the future, as excessive using of this command can lead to your banning. Thank you.")
    await ctx.author.send(embed=embed)
    dev = await client.fetch_user(834974179085385728)
    await dev.send(f"{ctx.author} just used `+leave`, in guild {ctx.guild.name}.")

@client.command()
async def top50(ctx):
  await ctx.reply('''Top Songs Streamed On Spotify Globally:
  https://open.spotify.com/playlist/37i9dQZEVXbMDoHDwVN2tF?si=9e0fc3db437f4cc5''')
@client.command()
async def define(ctx,*,phrase=None):
  if phrase == None:
    await ctx.message.reply('whatcha doing it\'s `+define [word]` not just `+define`')
  else:
    try:
      url = "https://mashape-community-urban-dictionary.p.rapidapi.com/define"
      querystring = {"term":phrase}
      headers = {
        'x-rapidapi-key': os.getenv('UD_TOKEN'),
        'x-rapidapi-host': "mashape-community-urban-dictionary.p.rapidapi.com"
      }
      response = requests.request("GET", url, headers=headers, params=querystring)
      x = json.loads(response.text)
      y=x.get("list")
      z = y[0]
      z = dict(z)
      word_def = z.get('definition')
      word_def_link = z.get('permalink')  
      qrttt = discord.Embed(title =f'Definition For {phrase.title()}:',description=f'*"{word_def}"*',url=word_def_link)
      qrttt.set_footer(text = 'From Urban Dictionary')
      await ctx.message.reply(embed=qrttt)
    except:
      await ctx.message.reply('Whoops, no definition found.')

@client.command()
async def help(ctx):
  help_embed = discord.Embed(title = 'Help | Wynn',description='''
  You need help. I shall provide.
  **Commands**:

  > **Utility Commands** ⚙️:
  • `+serverinfo` : *Provides info about the server*
  • `+info [member]`: *Provides info about a member*
  • `+timer [time]`: *Sets a timer.* Use Syntax `+timer [amount][unit]`, like `+timer 2m` will set a timer for 2 minutes. Available Units: `s`, `m`, `h` and `d`.
  • `+feedback [feedback]` *Gives feedback to my boss*
  • `+report [bug/issue]` *Reports a bug/issue*
  • `+ping` *The Bot's Current Latency*
  • `+ask [question]` *Creates a simple poll, with yes/no*
  • `+av [member]` *Returns a person's avatar*

  > **Moderation Commands** 🛠️:
  • `+kick [member]`: kicks a member
  • `+ban [member]`: bans a member
  • `+clear [amount]`: clears the *amount* of messages
  • `+nuke`: Nukes a channel, that is, clears a hell lotta messages. (10000, to be exact.)
  • `+prefix`: You tryna change my prefix?
  • `+AAAH`: Just kidding this isn't a command- (~~or is it?~~)

  > **Other Commands** 🔑:
  • `+quote`: Inspires you with a quote.
  • `+insult [member]`: insults a member. 
  • `+top50`: Top 50 songs streamed on spotify this week <:spotify:848783829078769684>
  • `+gif [search term]` Searches Giphy <a:giphy:864518958902935562> for your search term. 
  • `+predict [question]`: Like an 8ball. I use my prophetic powers to answer your question.
  • `+define [word/phrase]`: Defines the *word/phrase* that you specify. Uses urban dictionary.
  ''')
  await ctx.reply(embed=help_embed)


@client.command()
async def info(ctx,member:discord.Member=None):
  if member == None:
    dude= ctx.author
    dude_created_at = dude.created_at
    dude_crtd = dude_created_at.strftime("%x")
    member_info = discord.Embed()
    member_info.set_author(name=dude,url=dude.avatar_url,icon_url=dude.avatar_url)
    member_info.add_field(name='Avatar',value=f'[Avatar URL]({dude.avatar_url}) | For more info use `+av`')
    if ctx.channel.type != discord.ChannelType.private:
      dude1 = dude.joined_at
      dude_joined_at = dude1.strftime("%x")
      member_info.add_field(name='Server Info:',value=f'''
      Joined this server On: **{dude_joined_at}**
      Nickname: **{dude.nick}**''')
    if dude.id == 834974179085385728:
      member_info.add_field(name='Dev Team:',value=f'This user is part of the dev team: **{dude}** <:BlurpleVerified:866314289324883978>')
      x = "You don't know your own info smh."
    else:
      x = "You don't know your own info smh. Anyway, here you go:"
    member_info.set_thumbnail(url=dude.avatar_url)
    member_info.set_footer(text=f"ID: {dude.id} • Joined Discord On: {dude_crtd}")
    await ctx.reply(x,embed=member_info)
  elif member != None:
    dude= member
    dude_created_at = dude.created_at
    dude_crtd = dude_created_at.strftime("%x")
    member_info = discord.Embed()
    member_info.set_author(name=dude,url=dude.avatar_url,icon_url=dude.avatar_url)
    member_info.add_field(name='Avatar',value=f'[Avatar URL]({dude.avatar_url}) | For more info use `+av`')
    if ctx.channel.type != discord.ChannelType.private:
      dude1 = dude.joined_at
      dude_joined_at = dude1.strftime("%x")
      member_info.add_field(name='Server Info:',value=f'''
      Joined this server On: **{dude_joined_at}**
      Nickname: **{dude.nick}**''')
    if dude.id == 834974179085385728:
      member_info.add_field(name="Highest Role:",value=dude.top_role.name)
      member_info.add_field(name='Dev Team',value=f'This user is part of the Wynn Developer Team: **{dude}** <:verified_dev:874836013560762389>')
    elif dude.id != 834974179085385728:
      member_info.add_field(name="Highest Role:",value=dude.top_role.name)
    member_info.set_thumbnail(url=dude.avatar_url)
    member_info.set_footer(text=f"ID: {dude.id} • Joined Discord On: {dude_crtd}")
    if member == ctx.author:
      await ctx.reply("You don't know your own info smh. Anyway, here you go:",embed=member_info)
    elif member != ctx.author:
      await ctx.reply(embed=member_info)
    
@client.command()
async def unban(ctx,id):
  try:
    id = int(id)
    user = await client.fetch_user(id)
    await ctx.message.guild.unban(user)
    await ctx.reply(f'Unbanned {user}, good for them.')
  except:
    await ctx.reply('There seems to be an error, ig I don\'t have enough permissions??')


@client.command()
async def av(ctx, member:discord.Member = None):
  if member == None:
    user = await client.fetch_user(ctx.author.id)
    png = user.avatar_url_as(format='png')
    jpg = user.avatar_url_as(format='jpg')
    webp = user.avatar_url_as(format='webp')
    jpeg = user.avatar_url_as(format='jpeg')
    av_e = discord.Embed()
    av_e.set_image(url=user.avatar_url)
    if user.is_avatar_animated() == True:
      gif = user.avatar_url_as(format='gif')
      av_e.add_field(name=f'{user.name}',value=f'Image As: [PNG]({png}) | [GIF]({gif}) | [JPG]({jpg}) | [WEBP]({webp}) | [JPEG]({jpeg})',inline=True)
      await ctx.reply(embed=av_e)
    elif user.is_avatar_animated() == False:
      av_e.add_field(name=f'{user.name}',value=f'Image As: [PNG]({png}) | [JPG]({jpg}) | [WEBP]({webp}) | [JPEG]({jpeg})',inline=True)
      await ctx.reply(embed=av_e)
  else:
    user = await client.fetch_user(member.id)
    png = user.avatar_url_as(format='png')
    jpg = user.avatar_url_as(format='jpg')
    webp = user.avatar_url_as(format='webp')
    jpeg = user.avatar_url_as(format='jpeg')
    av_e = discord.Embed()
    av_e.set_image(url=user.avatar_url)
    if user.is_avatar_animated() == True:
      gif = user.avatar_url_as(format='gif')
      av_e.add_field(name=f'{user.name}',value=f'Image As: [PNG]({png}) | [GIF]({gif}) | [JPG]({jpg}) | [WEBP]({webp}) | [JPEG]({jpeg})',inline=True)
      await ctx.reply(embed=av_e)
    elif user.is_avatar_animated() == False:
      av_e.add_field(name=f'{user.name}',value=f'Image As: [PNG]({png}) | [JPG]({jpg}) | [WEBP]({webp}) | [JPEG]({jpeg})',inline=True)
      await ctx.reply(embed=av_e)

@client.command()
async def send(ctx,channel_id,*,cont):
  if ctx.channel.id == m:
    channel_id = int(channel_id)
    channel = await client.fetch_channel(channel_id)
    await channel.send(cont)
  else:
    return

@client.command()
async def serverinfo(ctx):
    if ctx.channel.type != discord.ChannelType.private:
      x = 0
      for channel in ctx.guild.channels:
        channel_type = str(type(channel))
        if channel_type != "<class 'discord.channel.CategoryChannel'>":
          x+=1
      server_cat = ctx.guild.created_at
      server_created_at = server_cat.strftime("%x")
      serverinfo = discord.Embed(title=f'Server Info | {ctx.guild.name}',colour = discord.Colour.blurple())
      human_members = 0
      bot_members = 0
      for member in ctx.guild.members:
        if member.bot == True:
          bot_members += 1
        elif member.bot == False:
          human_members += 1
      serverinfo.add_field(name="Owner",value=ctx.guild.owner)
      serverinfo.add_field(name="Members",value=f'''
      Members: {ctx.guild.member_count}
      Humans: {human_members}
      Bots: {bot_members}''')
      serverinfo.add_field(name='Info',value=f'''
      Verification Level: {ctx.guild.verification_level}
      Voice Region: {ctx.guild.region}''')
      serverinfo.add_field(name='Roles',value=f'{len(ctx.guild.roles)} roles')
      serverinfo.add_field(name="Channels",value=f'''
      **Channels:** {x}
      📂 {len(ctx.guild.categories)}
      <:TextChannel:866314289316495390> {len(ctx.guild.text_channels)}
      <:VoiceChannel:866341964230950962> {len(ctx.guild.voice_channels)}''')
      serverinfo.set_thumbnail(url=ctx.guild.icon_url)
      serverinfo.set_footer(text=f'ID: {ctx.guild.id} • Created On: {server_created_at}')
      await ctx.message.reply(embed=serverinfo)
    else:
      await ctx.reply('Buddy, this is NOT a server. So it naturally follows that I cannot provide `serverinfo`. Like, c\'mon')

@client.command()
async def reply(ctx,channel_id,message_id,*,cont):
  if ctx.channel.id == m:
    channel = await client.fetch_channel(int(channel_id))
    message_id = int(message_id)
    message = await channel.fetch_message(message_id)
    await message.reply(cont)
  else:
    return

@client.command()
async def quote(ctx,aliases=['inspire']):
  quote = random.choice(quote_list)
  author = random.choice(author_list)
  await ctx.message.reply(f'''>>> *"{quote}"*
   ~**{author}**''')

@client.command()
@commands.has_permissions(kick_members=True)
async def leave(ctx):
  await ctx.message.reply('https://i.redd.it/8yrmn7r799g51.jpg')
  await ctx.message.add_reaction('<:sad_cat:848783085146865715>')
  await ctx.message.author.send(f'If you want to add me to **{ctx.message.guild.name}** again, use this link, all right? : https://discord.com/api/oauth2/authorize?client_id=865603879148453928&permissions=8&scope=bot')
  await ctx.message.guild.leave()

@client.command()
async def invite(ctx):
  invite_embed = discord.Embed(title='Wynn | Invite Link',url='https://discord.com/api/oauth2/authorize?client_id=865603879148453928&permissions=8&scope=bot',colour=discord.Colour.blurple(),description=f'''
  Hey {ctx.author.name}, if you want to add me to one of your servers, you can use this link: https://discord.com/api/oauth2/authorize?client_id=865603879148453928&permissions=8&scope=bot ''')
  invite_embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/855280629015904297/865630585991987220/inde1x.jpg')
  await ctx.send(embed=invite_embed)

@client.command()
async def ask(ctx,*,question=None):
    if question == None:
      await ctx.reply('Hey genius, what exactly do you want to ask? The syntax for this command is `+ask [question]`, like `+ask Do you like pineapple on pizza`.')
    else:
      author_thingy_22 = 'from '+ ctx.author.name+':'
      poll_qtt = question+'?'
      poll = discord.Embed(title = poll_qtt,colour = 0x3498db, description = 'React to this embed with your answer/opinion/whatever')
      poll.set_author(name = author_thingy_22,icon_url = ctx.author.avatar_url)
      poll_m = await ctx.send(embed=poll)
      await ctx.message.delete()
      await poll_m.add_reaction('✅')
      await poll_m.add_reaction('<:meh:853230140901687389>')
      await poll_m.add_reaction('<:disagree:848783083821203458>')
  
@client.command()
async def insult(ctx,member:discord.Member):
  if member.id == client.user.id:
    await ctx.message.reply('Nice try, pal, but you\'re not gonna get me to insult myself.')
  elif member.id == ctx.message.author.id:
    await ctx.message.reply('Why would you even wanna insult yourself, my poor friend?')
  else:
    try:
      url = "https://insult.mattbas.org/api/insult"
      response = requests.request("GET",url)
      await ctx.send(f'{member.mention}, {response.text}.')
    except:
      await ctx.message.reply('That\'s not how it works, genius. You use it like `+insult @member`.')

@client.command()
async def timer(ctx,amount,*,name=None):
  if name == None:
    rn = 'your timer is complete '
    rn1 = 'Timer has been set.'
  else:
    rn = f'your timer for `{name}` is complete.'
    rn1 = f'Timer for `{name}` has been set.'
  
  if 's' in amount:
    amountl = amount.split('s')[0]
    amountl = int(amountl)
    await ctx.message.reply(f'{rn1}')
    await asyncio.sleep(amountl)
    await ctx.send(f'{ctx.message.author.mention}, {rn}')
    await ctx.message.author.send(f'{ctx.message.author.mention}, {rn}')
  if 'm' in amount:
    amountl = amount.split('m')[0]
    amountl = int(amountl)
    await ctx.message.reply(f'{rn1}')
    await asyncio.sleep(amountl*60)
    await ctx.send(f'{ctx.message.author.mention}, {rn}')
    await ctx.message.author.send(f'{ctx.message.author.mention}, {rn}')
  if 'h' in amount:
    amountl = amount.split('h')[0]
    amountl = int(amountl)
    await ctx.message.reply(f'{rn1}')
    await asyncio.sleep(amountl*3600)
    await ctx.send(f'{ctx.message.author.mention}, {rn}')
    await ctx.message.author.send(f'{ctx.message.author.mention}, {rn}')
  if 'd' in amount:
    amountl = amount.split('d')[0]
    amountl = int(amountl)
    await ctx.message.reply(f'{rn1}')
    await asyncio.sleep(amountl*3600*24)
    await ctx.send(f'{ctx.message.author.mention}, {rn}')
    await ctx.message.author.send(f'{ctx.message.author.mention}, {rn}')

@client.command()
@commands.has_permissions(manage_messages=True)
async def warn(ctx, member: discord.Member,*,reason):
  try:
    await member.send(f'You have been warned in {member.guild} for {reason}.')
    await ctx.send(f'{member.name} has been warned. ')
  except:
    await member.send(f'You have been warned in {member.guild}.')
    await ctx.send(f'{member.name} has been warned.')

@client.command()
async def feedback(ctx,*,feedback=None):
  if feedback == None:
    await ctx.reply("Buddy, it's good and all that you want to give my boss some feedback, but I think it would be more helpful if you actually give some feedback. The Syntax is `+feedback [feedback]`, not just `+feedback`.")
  else:
    bot_dev = await client.fetch_user(834974179085385728)
    fb_embed = discord.Embed(title = 'Feedback Message:',description=f"*{feedback}*")
    fb_embed.set_footer(text=f'{ctx.message.author}')
    await bot_dev.send(embed=fb_embed)
    await ctx.message.reply('Your feedback has been received and recorded.')

@client.command()
async def report(ctx,*,problem=None):
  if problem == None:
    await ctx.reply('''Use `+report` to report a bug/issue with the bot. Please refrain from reporting the same issue multiple times. Common Issues include, but are not limited to:
    • Bot unresponsive to a specific Command
    • Bot has large response times
    • Unexpected Command Response
    ''')
  else:
    bot_dev = await client.fetch_user(834974179085385728)
    report = discord.Embed(title='Wynn | Issue/Bug Report',description=problem, colour = discord.Colour.red())
    report.set_footer(text=f'Reported by: {ctx.author}')
    await bot_dev.send(embed=report)
    await ctx.reply("Thank you for submitting your report. Our dev team will be looking into it soon.")

@client.command()
async def ping(ctx):
  latency_ms = float(client.latency) *1000
  pong = discord.Embed(title = 'Wynn | Current Latency',description = f'My current latency/ping is currently {latency_ms} ms.')
  if latency_ms >= 167:
    await pong.set_footer('<:lag:866250123762466847> High Delay: If the Bot takes large amounts of time to respond, use +')
  await ctx.reply(embed=pong)

@client.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member):
  try:
    await member.kick()
    await ctx.send(f"**{member.name} has been kicked by {ctx.author.name}, lmaoo**")
  except:
    await ctx.message.reply(f'u dont have enough permissions for this, pal. contact a mod or someone idk if u wanna kick {member.display_name}')

@client.command()
@commands.has_permissions(manage_channels=True)
async def lock(ctx, channel : discord.TextChannel=None):
  channel = channel or ctx.channel
  overwrite = channel.overwrites_for(ctx.guild.default_role)
  overwrite.send_messages = False
  await channel.set_permissions(ctx.guild.default_role, overwrite=overwrite)
  await ctx.send('Channel locked for `@everyone`.')

@client.command()
@commands.has_permissions(manage_channels=True)
async def unlock(ctx, channel : discord.TextChannel=None):
  channel = channel or ctx.channel
  overwrite = channel.overwrites_for(ctx.guild.default_role)
  overwrite.send_messages = True
  await channel.set_permissions(ctx.guild.default_role, overwrite=overwrite)
  await ctx.send('Channel unlocked for `@everyone`.')

@client.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, member: discord.Member):
  try:
    await member.ban()
    await ctx.send(f"{member.name} has been banned by {ctx.author.name}, lmaoo")
  except:
    ctx.message.reply(f'u dont have enough permissions for this, pal. contact a mod or someone idk if u wanna kick {member.display_name}')

@client.command()
@commands.has_permissions(manage_messages=True)
async def nuke(ctx,amount=10000):
  await ctx.send('<a:loading1:848783085982187550> Nuking channel...')
  await ctx.channel.purge(limit=amount)
  await ctx.send(f'<a:nuke:848783088594714664> Channel Nuked by {ctx.author}, lmao.')

 
keep_alive()
client.run(os.getenv('TOKEN'))