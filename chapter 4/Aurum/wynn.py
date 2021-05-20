import discord
import time
import random

client = discord.Client()
answers = [
    "As I see it, yes.", "Ask again later", " Better not tell you now.",
    "Cannot predict now", "Concentrate and ask again.", "Don’t count on it.",
    "You may rely on it.", "Yes – definitely.", " Yes.", " Without a doubt.",
    "Very doubtful.", " Signs point to yes.", "Reply hazy, try again",
    "Outlook good", "Outlook not so good.", "My sources say no.",
    "My reply is no.", "Most likely", "It is decidedly so", "It is certain"
]

oofl = ['https://media.tenor.com/images/a937ec68af3ce4c3ed000fc0a0847424/tenor.gif','https://cdn.discordapp.com/attachments/836442267328839730/837525602806398976/01e.jpg','https://cdn.discordapp.com/attachments/836442267328839730/837527661214433331/output-onlinepngtools3.png','https://cdn.discordapp.com/attachments/836442267328839730/837528032939737108/633-6332768_oof-logo-hd-png-download.png']
forbiddenl = ['broccoli','']

@client.event
async def on_ready():
  print('Logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  msga = message.author
  guild = message.guild
  if msga == client.user:
    return
  msg = message.content
  msgc = message.channel
  if msg == "f" or msg == ("F"):
    await msgc.send('f')

  if msg.startswith('$facts'):
    await message.reply('https://cdn.discordapp.com/emojis/844920741614452756.png')

  if msg.startswith('$invite'):
    await msga.send('https://discord.com/api/oauth2/authorize?client_id=844205956740677663&permissions=8&scope=bot')

  if msg.startswith('$8ball') or msg.startswith('$predict'):
    await msgc.send(random.choice(answers))
  
  if "lol" in msg.lower():
    await msgc.send('lol')

  if "lmao" in msg.lower():
    await msgc.send('lmaoo')

  if "i am" in msg.lower() or "i'm" in msg.lower():
    await msgc.send('https://i.imgflip.com/4fvxku.gif')

  if msg.startswith('$mydp') or msg.startswith('$mypfp'):
    await msgc.send(msga.avatar_url)

  if msg.startswith('$mytag'):
    await msgc.send(msga)
    
  if msg.startswith('$myname'):
    await msgc.send("You don't know your own name smh")
    await msgc.send("||⬇️ That's your name, dumbass.||")
    await msgc.send(msga.name)

  if "bruh" in msg.lower():  
    await msgc.send('bruuuh..')
    await msgc.send('https://pbs.twimg.com/media/EiPXixpXkAA0pXv.jpg')

  if "844205956740677663" in msg:
    await msgc.send("I don't like pings. Try using a command instead.")
    await message.add_reaction('⛔')

  if "oof" in msg.lower():
    await msgc.send(random.choice(oofl))


  if msg.startswith('$dm'):
    await msga.create_dm()
    await message.add_reaction('👍')
    await message.reply('A direct message channel has been established.')
    await msga.send('Wassup')
    await msga.send('u can try any command')
    await msga.send('it should work, hopefully.')

  if msg.startswith('$help'):
    await msgc.send('No.')
    time.sleep(3)
    await msgc.send("Just kidding, I'll help.")
    await msgc.send("I'm Wynn, an annoying bot. If you'd like to know how to use me, Try `$commands`. Also, I hate pings.")
    a = str(msga)
    await msgc.send('||⬇️ this dude sucks||')
    await msgc.send(a.split('#')[0])

  if msg.startswith('$prefix'):
    prefix1 = discord.Embed(title="DONT TRY AND CHANGE MY PREFIX",url='',colour=0)
    prefix1.set_image(url='https://media1.tenor.com/images/c39b0d1ed640fa411a61ee906c895a90/tenor.gif')
    await message.reply(embed=prefix1)


  if 'yay' in msg.lower():
    await msgc.send('https://i.pinimg.com/originals/3f/5e/73/3f5e73826e68e777ba980635016bd87c.gif')

  if 'noice' in msg.lower():
    await msgc.send('https://i.giphy.com/media/8Odq0zzKM596g/giphy.webp')

  if 'uptown funk' in msg.lower():
    await msgc.send('https://open.spotify.com/track/32OlwWuMpZ6b0aN2RZOeMS')
    await message.add_reaction('📀')
    


  
  if msg.startswith('$commands'):
    await msgc.send('> Okay cool so these are the commands:')
    await msgc.send('''
    > `$commands` ||(Obviously.)||
    > `$annoy`  ||pings the person u specify a random number of times||
    > `$prefix`  ||Gives you some info about my prefix||
    > `$help`  ||Provides some much-needed help to your dum dum brain ||
    > `$serverpfp` ||Your server's pfp ||
    > `$serverid` || Your server's ID ||
    > `$inspire` || gives u some much needed wisdom. also works with `$quote` || 
    > `$myname` ||Reminds you what your name is||
    > `$mytag` ||Gives you your complete discord username||
    > `$myid`  ||Gives you your discord ID ||
    > `$mydp`  ||Shows off your dp in full glamour||
    > `$count` || number of ppl in that server||
    > `$dm`  || I message you personally. ||
    > `$feedback`  || Gives my boss some feedback about me||
    > `$leave` || I leave the server. ||
    > `$joined`  || Tells you when you joined ||
    > `$8ball` (Or `$predict`)  || I use my prophetic powers ||
    > `$mention` || try the command and you'll understand ||
    > ~~More commands coming soon, relax~~
    ''')
  if msg.startswith('$mention-o') or msg.startswith('$ping-o'):
    await msgc.send('@here ')

  if 'cringe' in msg.lower():
    message.reply('https://tenor.com/view/dies-of-cringe-cringe-gif-20747133')

  if msg.startswith('$offline'):
    if msga.id == 834974179085385728:
      await msgc.send('going offline...')
    else:
      await message.reply('why wud i listen to u')
      await message.add_reaction('🥱')
  if msg.startswith('$quote') or msg.startswith('$inspire'):
    quote = discord.Embed(title='Best Quote Ever',description='''*"In this world, it's either yeet or be yeeted."* ''',color=0x00ff00)
    quote.set_author(name='a wise guy',url='https://thecalloftheuniverse.wordpress.com/2021/05/11/life-a-philosophical-review/',icon_url='https://i.pinimg.com/originals/99/e5/94/99e59449b7554b81bd40770ce32aa322.gif')
    await msgc.send(embed=quote)

  if msg.startswith('$count'):
    q = "there's like "
    p = ' members is this server.'
    r = str(guild.member_count)
    s = q+r+p
    await message.reply(s)


  if msg.startswith('$leave'):
    if msga.id == guild.owner_id:
      await message.reply('whatever dude ur loss')
      await msgc.send('https://i.redd.it/8yrmn7r799g51.jpg')
      await guild.leave()
    else:
      await message.reply('who u kidding pal u not the owner of the server.')
      await msgc.send('so yea, no, i aint gonna just leave ')
      

  if msg.startswith('$myid'):
    a = 'Your Discord ID is `'
    c = str(msga.id)
    d = '`'
    b = a+c+d
    await message.reply(b)

  if msg.startswith('$mention-e') or msg.startswith('$ping-e'):
    await msgc.send('@everyone ')
  
  if 'smort'in msg:
    await msgc.send('https://i.giphy.com/media/hFROvOhBPQVRm/giphy.webp')

  if msg == '$mention' or msg == '$ping':
    await msgc.send('''
    > Use this command when you're to lazy to ping someone.
    > `$mention-o` or `$ping-o` [Pings online members]
    > `$mention-e` or `$ping-e` [Pings everyone]
    > `$pingme` [Pings yourself. Why would u use this? idk.]
    ''')

  if '😂' in msg:
    await message.add_reaction('😂')

  if 'wynn' in msg.lower():
    await message.add_reaction('🤨')

  if 'best gif' in msg.lower():
    await message.reply('THE BEST GIF IS:')
    await msgc.send('https://tenor.com/view/langostino19gif-go-back-iwant-to-be-monkey-gif-19679655')
  
  

  if 'lefishe' in msg.lower():
    await message.reply('https://www.youtube.com/watch?v=lPGipwoJiOM')

  if 'coffin dance' in msg.lower():
    await message.reply('https://www.youtube.com/watch?v=j9V78UbdzWI')

  if 'dancin' in msg.lower():
    await message.reply('https://www.youtube.com/watch?v=UcRtFYAz2Yo')

  if msg.startswith('$serverpfp'):
    pfp = discord.Embed(title=guild.name,url=guild.splash_url,colour=0x00ff00)
    giu = str(guild.icon_url)
    pfp.set_image(url=giu)
    await msgc.send(embed=pfp)

  if msg.startswith('$serverid'):
    await message.reply(message.guild.id)    
    
  if msg.startswith('$feedback'):
    await message.reply('Your feedback has been received!')
    print(message.author,'says',msg)

  if msg.startswith('$annoy'):
    if '@' in msg:
      msg.split()
      y = msg.split()[1]
      x = random.randint(1,90)
      a = x*y
      await msgc.send(a)
    else:
      await message.reply('mention who u want to annoy u dumdum')

  if msg.startswith('!gaw'):
    gaw1 = discord.Embed(title='🎉 **GIVEAWAY!!** 🎉',url='',description='from this dude: 1 pepe statue worth like 5 to 200 mil lmao',colour=0x71368a)
    gaw1.set_footer(text='Winners : 1 • Today at some time')
    message1 = await msgc.send(embed=gaw1)
    await message1.add_reaction('🎉')
    
  if '$pingme' in msg.lower():
    author_id = str(msga.id)
    q = '<'
    r = '@'
    s = '>'
    p = q+r+author_id+s
    await msgc.send(p)

  if msg.startswith('$joined'):
    await msgc.send(msga.joined_at)
client.run('ODQ0MjA1OTU2NzQwNjc3NjYz.YKPCEA.mVAhcGzY3kfFR7BWLm5cEthD3fw')  