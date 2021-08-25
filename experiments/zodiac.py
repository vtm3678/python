toggle_view = str(input("Would you like to know more about yourself (yes/no)?"))
if toggle_view.lower() == ("yes"):
    zodiac0 = input("Please enter your zodiac sign:")
    if zodiac0.lower() == ("capricorn"):
        zinfo = '''> Capricorn ♑
        Born between Dec 22 and Jan 21
        Element - Earth
        You are:
        Hardworking
        Straightforward
        Stubborn '''
        print(zinfo)
    elif zodiac0.lower() == ("aquarius"):
        zinfo = '''> Aquarius ♒
        Born between Jan 22 and Feb 21
        Element - Air
        You are:
        Innovative
        Admired
        Eccentric '''
        print(zinfo)
    elif zodiac0.lower() == ("pisces"):
        zinfo = '''> Pisces ♓
        Born between Feb 22 and Mar 21
        Element - Water
        You are:
        Free
        Sensual
        Sensitive '''
        print(zinfo)
    elif zodiac0.lower() == ("aries"):
        zinfo = '''> Aries ♈
        Born between Mar 22 and Apr 21
        Element - Fire
        You are:
        Brave
        Independent
        Impulsive '''
        print(zinfo)
    elif zodiac0.lower() == ("taurus"):
        zinfo = '''> Taurus ♉
        Born between Apr 22 and May 21
        Element - Earth
        You are:
        A person with good taste
        Sensual
        Down to Earth
        Stubbon '''
        print(zinfo)
    elif zodiac0.lower() == ("gemini"):
        zinfo = '''> Gemini ♊
        Born between May 22 and Jun 21
        Element - Air
        You are:
        Dynamic
        A Multi-talented person
        A game lover '''
        print(zinfo)
    elif zodiac0.lower() == ("cancer"):
        zinfo = '''> Cancer ♋
        Born between Jun 22 and Jul 21
        Element - Water
        You are:
        Sensitive
        Friend-oriented
        Practical '''
        print(zinfo)
    elif zodiac0.lower() == ("leo"):
        zinfo = '''> Leo ♌
        Born between Jul 22 and Aug 21
        Element - Fire
        You are:
        Creative
        Popular
        Faithful '''
        print(zinfo)
    elif zodiac0.lower() == ("virgo"):
        zinfo = '''> Virgo ♍
        Born between Aug 22 and Sep 21
        Element - Earth
        You are:
        Successful
        Creative
        Clever '''
        print(zinfo)
    elif zodiac0.lower() == ("libra"):
        zinfo = '''> Libra ♎
        Born between Sep 22 and Oct 21
        Element - Air
        You are:
        Irresistible
        Adventurous
        Indecisive '''
        print(zinfo)
    elif zodiac0.lower() == ("scorpio"):
        zinfo = '''> Scorpio ♏
        Born between Oct 22 and Nov 21
        Element - Water
        Congratulations! You belong to the best Zodiac Sign - #Scorpio ♏
        You are:
        Self-reliant
        Powerful
        Dominant '''
        print(zinfo)
    elif zodiac0.lower() == ("sagittarius"):
        zinfo = '''> Sagittarius ♐
        Born between Nov 22 and Dec 21
        Element - Fire
        You are:
        Open-minded
        Loving
        Insensitive '''
        print(zinfo)
    else:
        print("Error: Unrecognised Zodiac Sign.")
elif toggle_view.lower() == ("no"):
    print("If you change your mind, please do restart the program.")
    print("For now, however, bye.")
else:
    print("Sorry, that wasn't [yes] or [no].")
    print("To retry, please restart.")
