# Credits:
# 1. Aditya Bhattacharya (github: /AdityaBhattacharya1)
# 2. Garv Sachdev (github: /gavkujo)
# =====================================================
# Indent system: 4 spaces (= 1 tab). Peace is among us.

import os
import random
import re
from os.path import dirname, join

import discord
from dotenv import load_dotenv

client = discord.Client()

dotenv_path = join(dirname(__file__), ".env")
load_dotenv(dotenv_path)
DISCORD_TOKEN = os.environ.get("DISCORD_TOKEN")
pattern = (
    "(electrical)(?! (engineering|engg))|sus|amogus|gus(?! (fring|fing|johnson))|imposter|vent|us$|bay$|crewmate|baka"
)


class Susbot:
    def __init__(self, pattern: str, token: str) -> None:
        self.pattern = pattern
        self.token = token

    @client.event
    async def on_ready() -> None:
        print(f"We have logged in as {client.user}")

    @client.event
    async def on_message(message: str):

        easter_eggs = {
            "dude random": "dude random is the best fucking youtuber seriously man wth. <:yoyo:838836197055922177> <:dadude:838834466289090640>",
            "suketu patni gaming": "suketu pati gayming channel hits 69420 billion subscibers !!!!!1!1111!111 <:hmm:838812033759707176><:hmm:838812033759707176><:hmm:838812033759707176>",
            "anhad": "lionl anhdad fotnite gaying channel hit 69 subs!!! <:op:844131961949388841><:op:844131961949388841><:op:844131961949388841>",
            "jaggu": "jaggu bandar is so mast kalandar that he committed mass genocide <:colgate:844166443583275019>",
            "jediporg": "jihadi p**n barah suprmacy !!!1!1111 katihar chalenge ;) ;) karachi boizzzzzzzzzzz <:mishbadababy:838806751188484167><:mishbadababy:838806751188484167><:convertible:845722150789971988><:convertible:845722150789971988>",
            "mighty raju": "maity raju supremacy. M SE HOTA HAI MAITY R SE HOTA HAI RAJU RAJU RAJU RAJu <:shaktiman:844258104299225118><:shaktiman:844258104299225118><:shaktiman:844258104299225118>",
            "motu": "Motu Patlu: The best anime of all time. I want to shed light onto the uncultured swines who do not know of the Indian anime Motu Patlu. Motu Patlu is a anime with the characters Motu, Patlu and the citizens of their suburban indian residence. Motu is a thicc boy-o who everybody loves because he is motu. Patlu is motu's sidekick who thinks he is such a smarty pants. Motu saves his town from the villanous John the Dohn. John is a stupid bully who picks on motu using india's own professor jhatika's gadjets against motu. Motu always wins because he is best boy-o. Like in many other animes the characters get different forms and motu patlu is no exception. Motu has many forms some including SUPER DOG MAN MOTU!, Onion Motu, Regular Motu and his final form..... He can only enter his final form when he eats a samosa his favorite snack which he eats on a frequent basis. His final form can sent someone 5x his weight flying into space and coming back down to earth! Motu then saves the day (and patlu from danger) while officer Chingnam arrests him and puts him in his jail called the web since Nobody could escape chingnam's web. In conclusion motu patlu has many elements many modern day animes don't have (I'm looking at you richard and mortimer) heart, an unstoppable duo, character arcs and development and who could forget Anime Betrayals. I give this anime 11 samosas out of 10! I am hyped for the next episode of Motu Patlu it's gonna be great!",
            "chutki": "chutki is fucking cringe. she is the most generic fucking character ive ever seen.",
            "tun": "devy and shifa we are still waiting on the om x dholu fanfic <:eboy:844132023224107018>",
            "dio": "joseph is better stfu ",
            "dutta": "man when are you gon fight with disha again. we are seriously looking forward to the next fight <:technically:847106049935671357><:technically:847106049935671357>",
            "unplayable": "ffs if you say that again i will steal one of your terracotta elephants",
            "roy": "man black ops 1 is such a cringe game i uninstalled it bcoz there was an amogus reference in the game <:trollge:845728232119730186>",
            "dholu": "<:dukh:844185997678870559><:dard:844131868190048267>",
            "bholu": f"<:hmm:838812033759707176><:op:844131961949388841><:op:844131961949388841> {message.author.mention}",
            "bri'ish": "so you call these things 'chips'? instead of crispity crunchy munchie crackerjack snacker nibbler snap crack n pop westpoolchestershireshire queen's lovely jubily delights? That's rather bit cringe, innit bruv <:hmm:838812033759707176><:hmm:838812033759707176><:hmm:838812033759707176>",
            "technically": "<:technically:847106049935671357>" * 10,
            "1984": "LiTeRaLlY nInEtEeN eIgHtY-fOuR - George Orwell, 1948",
            "based": """Based? Based on what? On your dick? Please shut the fuck up and use words properly you fuckin troglodyte, do you think God gave us a freedom of speech just to spew random words that have no meaning that doesn't even correllate to the topic of the conversation? Like please you always complain about why no one talks to you or no one expresses their opinions on you because you're always spewing random shit like poggers based cringe and when you try to explain what it is and you just say that it's funny like what? What the fuck is funny about that do you think you'll just become a stand-up comedian that will get a standing ovation just because you said 'cum' in the stage? HELL NO YOU FUCKIN IDIOT, so please shut the fuck up and use words properly.""",
            "weeb": f"""You will never be Japanese. You have no ancestry, you have no citizenship, you have no skills that would make Japan ever want you. You are a shut-in self-hating white man twisted by delusions of mythical Japanese superiority and exposure to Japanese media into a disgusting mockery of nature’s perfection. All 'validation' you get from other people in this position couldn't be worse in making you believe that spending years of your life learning a globally useless language to a first-grader's level was a worthwhile use of your time, but one can't expect that an individual as pathetic as you will ever know the value of the youth you threw away in doing that. Actual Japanese are utterly repulsed by you. Thousands of years of linguistic evolution have allowed natives to identify frauds from mannerisms and vocabulary alone. Even if your written text of self-hatred and attention begging akin to a stray dog's somehow passes as normal (it won't), any Japanese person will immediately cut all ties when they hear the voice and accent of someone who is not only a basic Japanese speaker at best, but worth no more than garbage in skills, accomplishments, and likeability. You will never be happy. You wrench out a fake smile and laugh to yourself believing that watching a content creator that you understand 20% of at best is somehow superior than watching your own kind, as you project your disgusting traits onto your entire kind. However, deep inside you feel the depression creeping up like a weed, ready to crush you under the unbearable weight, and you know that. You know that all you do now is have an entirely new linguistic medium in which to be ignored, and not even the exotic trait of being foreign makes up for just how uninteresting of a person you are. yeah im talking to you, {message.author.mention}. fucking cringe weaboo""",
            "krunker": "Krunker.io Akimbo 🔫👩 Uzi 🔫 is a two-handed automatic 🤖 weapon 🔫🏹. Many 🔢 players 🎮 prefer 👍🙋 this weapon ❌🔫🔪 because it can fire 🔥 quickly 🏃🏻💨. Detailed features 🎥 of this weapon 🗡 will be mentioned 🌲👇🏼🚘 below 👇🏻. The best 👌 thing 🕑 about 💦 a 3D 🤩‼ FPS 🔫🖱💣 gun 🔫 game 🎮 is that you 👈 will enjoy 👌🏽💯😌 a lot 💯🔥 of action 🎭. Not only that but 🍑 you 👉💦 will get 🉐 access 🔖 to various 🤓🧐 types ⌨ of weapons 🗡⚔ that can be used 🎶 inside 💠 the game 🎱📛. All 💯 these weapons 🔫🏹 have their benefits 👍 for drawbacks. Once you 👈🏼 understand ❓📚 the use 🏻 of these weapons 🗡🚮 in you 👈🏻 will surely 👍 love 😳❤ playing 🎮 with it. You 👉 can easily 👅 find 🔎 information ℹ🗺 about 💦 Krunker.io Akimbo 🔫👩 Uzi 🔫 which is a great 👍🏼👌🏼 weapon 🗡🔫💣 for close 🚫💦 combat 🗡🔫🏹. There are different ⁉ types ⌨ of things 🕑 that you 👉😘 can enjoy 👌💯 when ⏰ you 👈 use 😏 the Uzi 🔫 in the game 🎮🎲. It is a great 🇬🇧 weapon 🔫🏹 that is loved ❤ by most people 👬👫👭 for its firing 🔫🔥 speed 🏎👺💨 and dual-wielding ability 💪.",
            "jonathan": f"""haha {message.author.mention}, you are banging my daughter. ⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⢀⣤⣤⣄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄ ⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⣴⣤⣤⣤⣴⣾⣿⣿⣿⣿⡄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄ ⠄⠄⠄⠄⠄⠄⠄⠄⠠⠾⢿⣿⣿⠟⠋⠁⠤⣬⣽⣿⡇⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄ ⠄⠄⠄⠄⠄⠄⠄⠄⡄⠄⠄⢀⣽⣦⡎⠁⠒⠒⢻⣿⣿⣄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄ ⠄⠄⠄⠄⠄⠄⠄⢀⣧⡀⢀⣾⣿⣿⣧⣦⣴⣾⣿⣿⣿⣿⣧⠄⠄⣠⣴⣆⠄⠄⠄⠄ ⠄⠄⠄⠄⠄⠄⠄⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⡻⣿⣿⣿⣿⣧⢸⣿⣿⣿⠄⠄⠄⠄ ⠄⠄⠄⠄⠄⠄⠘⠿⠿⣿⣿⣿⣿⣿⣿⣿⣿⣸⣿⣿⣿⣿⣿⣿⣿⣝⣿⡟⠄⠄⠄⠄ ⠄⠄⠄⠄⠄⠄⠄⠸⣄⢺⣿⠿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡏⠄⠄⠄⠄⠄ ⠄⠄⠄⠄⠄⠄⠄⠄⢿⠄⡀⠄⣸⣿⡿⣻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠄⠄⠄⠄⠄ ⠄⠄⠄⠄⠄⠄⠄⠄⠸⡆⠄⣀⣛⣫⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠄⠄⠄⠄⠄ ⠄⠄⠄⠄⠄⠄⠄⠄⠄⠇⠄⣿⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠄⠄⠄⠄⠄ ⠄⠄⠄⠄⠄⠄⠄⠄⠄⠐⠄⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠄⠄⠄⠄⠄ ⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠄⠄⠄⠄⠄ ⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⢹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠃⠄⠄⠄⠄⠄ ⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠄⠄⠄⠄⠄⠄ ⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠈⠿⠽⠿⢿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠄⠄⠄⠄⠄⠄ ⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⢸⣿⣿⣿⡿⠟⠛⠉⠄⠄⠄⠄⠄⠄⠄⠄""",
            "bad": """⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣤⣶⣶⣶⣦⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ ⠀⠀⠀⠀⠀⠀⠀⠀⣀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀ ⠀⠀⠀⠀⠀⠀⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⡀⠀⠀⠀⠀⠀⠀ ⠀⠀⠀⠀⠀⣼⣿⣿⣿⣿⣿⣿⣿⡿⡱⡿⣿⣿⣿⣿⣿⣿⣿⣷⡀⠀⠀⠀⠀⠀ ⠀⠀⠀⠀⢰⣿⣿⣿⣿⡟⠟⠛⠁⠄⠂⠀⠓⠋⢟⣿⣿⣿⣿⣿⣇⠀⠀⠀⠀⠀ ⠀⠀⠀⠀⢸⣿⣿⣿⠜⢖⣁⣀⣀⡀⠀⢀⣐⢠⣴⣟⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀ ⠀⠀⠀⠀⢸⣿⣿⣷⣛⠿⠻⠉⠯⣉⠠⠹⠚⠺⠿⢿⣟⣿⣿⣿⣿⠀⠀⠀⠀⠀ ⠀⠀⠀⢐⣿⣿⡿⡿⣿⣷⠆⠀⠐⠀⠀⠀⠀⢠⣼⣶⣿⣿⣿⣿⣿⡶⠀⠀⠀⠀ ⠀⠀⠀⠘⣿⡟⠻⣋⢉⣉⠁⣀⢀⣄⣠⣄⡀⠀⣉⣉⣙⠻⢻⣿⣿⡷⠀⠀⠀⠀ ⠀⠀⠀⠀⣿⣿⣾⡏⠑⠓⠉⢉⣾⣿⣿⣿⣯⠑⠚⠓⢛⣾⣼⣿⣿⡇⠀⠀⠀⠀ ⠀⠀⠀⠀⢹⣿⡿⠻⠠⢤⣔⣼⣿⣿⣾⣿⣿⣲⣄⠀⠘⠻⣿⣿⡟⠀⠀⠀⠀⠀ ⠀⠀⠀⠀⠘⣿⣧⠀⣀⠟⠃⠡⣿⠿⠞⠽⣿⠈⠛⣶⣀⣇⣿⡿⠃⠀⠀⠀⠀⠀ ⠀⠀⠀⠀⠀⢹⣿⣾⣯⠃⢠⣴⣦⠀⠀⣠⣴⣦⡀⠘⣿⡷⣿⠁⠀⠀⠀⠀⠀⠀ ⠀⠀⠀⠀⠀⠀⣿⣾⡇⢠⡿⡿⠻⠁⢠⠸⠻⢿⢷⠀⢸⣿⠏⠀⠀⠀⠀⠀⠀⠀ ⠀⠀⠀⠀⠀⠀⠘⣿⡇⠊⣠⣤⣤⣤⣤⣶⣦⣤⣀⠃⣾⡟⠀⠀⠀⠀⠀⠀⠀⠀ ⠀⠀⠀⠀⠀⠀⠀⠘⣧⣬⡶⠀⠀⠀⠀⠀⠀⠸⣿⣦⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀ ⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣿⣿⡿⡛⢟⢶⣶⣽⡿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠛⠿⢶⣴⡿⠟⠋⠀⠀⠀⠀""",
            "good": "⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⢄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ ⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠖⠁⠀⠀⠀⠀⠀⠈⠋⠳⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀ ⠀⠀⠀⠀⠀⠀⠀⣠⣾⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠙⢦⠀⠀⠀⠀⠀⠀⠀ ⠀⠀⠀⠀⠀⢠⣿⡿⢁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⠸⣷⣀⠀⠀⠀⠀⠀ ⠀⠀⠀⠀⠀⣿⣿⡧⢕⠂⠀⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⠀⣿⣿⡄⠀⠀⠀⠀ ⠀⠀⠀⠀⢸⣿⣿⠏⠃⠈⠉⠀⠀⠀⠀⠀⠀⠈⠈⠀⠀⠀⠐⣿⣿⡇⠀⠀⠀⠀ ⠀⠀⠀⠀⢸⣿⣿⣿⣿⣴⣶⡆⠀⠀⠀⠀⠀⠀⠀⣴⣴⣴⣄⣿⣿⣇⠀⠀⠀⠀ ⠀⠀⠀⠀⣿⣿⣿⣦⣤⣤⠌⣻⣦⣤⡀⢀⣤⡠⢔⡀⢀⣀⣉⢻⢿⣿⠇⠀⠀⠀ ⠀⠀⠀⠀⢿⣿⠋⡟⠙⠛⠚⠘⠋⢉⠁⠈⠙⠋⠃⠿⠟⠛⠩⠹⣿⡿⠀⠀⠀⠀ ⠀⠀⠀⠀⢸⣿⡎⡐⠙⠓⠚⠉⠠⣾⡆⠀⢰⠀⠒⠒⠒⠂⡀⢺⣿⠇⠀⠀⠀⠀ ⠀⠀⠀⠀⢸⣿⣿⡁⠀⠀⠀⡤⠔⡎⠂⠀⠈⡖⣀⡀⠀⠀⠨⠄⢿⠂⠀⠀⠀⠀ ⠀⠀⠀⠀⠈⣷⣿⣧⣠⡖⠁⠀⣿⣧⣀⣀⣠⣷⠀⠉⢦⣤⣤⣷⡗⠁⠀⠀⠀⠀ ⠀⠀⠀⠀⠀⢻⣸⠉⠛⢿⣶⣄⡨⠻⢿⣿⣿⣅⣄⣶⣾⠿⠛⣿⡇⠀⠀⠀⠀⠀ ⠀⠀⠀⠀⠀⠘⢿⣦⠀⠀⠈⠻⢍⠙⠉⠋⠋⠉⡿⠋⠀⠀⣼⡿⠁⠀⠀⠀⠀⠀ ⠀⠀⠀⠀⠀⠀⠈⠞⣦⠀⢬⢧⣄⣀⡁⠉⣀⣠⡽⠁⠀⡼⠅⠀⠀⠀⠀⠀⠀⠀ ⠀⠀⠀⠀⠀⠀⠀⠀⠻⣧⣄⡉⠛⠛⠛⠛⠛⠋⠀⢠⣼⠋⠀⠀⠀⠀⠀⠀⠀⠀ ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣷⡄⠈⠀⠀⢀⢀⣤⡿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀ ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠻⠶⠼⠟⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀",
            "china": "⣿⣿⣿⣿⣿⠟⠋⠄⠄⠄⠄⠄⠄⠄⢁⠈⢻⢿⣿⣿⣿⣿⣿⣿⣿ ⣿⣿⣿⣿⣿⠃⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠈⡀⠭⢿⣿⣿⣿⣿ ⣿⣿⣿⣿⡟⠄⢀⣾⣿⣿⣿⣷⣶⣿⣷⣶⣶⡆⠄⠄⠄⣿⣿⣿⣿ ⣿⣿⣿⣿⡇⢀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⠄⠄⢸⣿⣿⣿⣿ ⣿⣿⣿⣿⣇⣼⣿⣿⠿⠶⠙⣿⡟⠡⣴⣿⣽⣿⣧⠄⢸⣿⣿⣿⣿ ⣿⣿⣿⣿⣿⣾⣿⣿⣟⣭⣾⣿⣷⣶⣶⣴⣶⣿⣿⢄⣿⣿⣿⣿⣿ ⣿⣿⣿⣿⣿⣿⣿⣿⡟⣩⣿⣿⣿⡏⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿ ⣿⣿⣿⣿⣿⣿⣹⡋⠘⠷⣦⣀⣠⡶⠁⠈⠁⠄⣿⣿⣿⣿⣿⣿⣿ ⣿⣿⣿⣿⣿⣿⣍⠃⣴⣶⡔⠒⠄⣠⢀⠄⠄⠄⡨⣿⣿⣿⣿⣿⣿ ⣿⣿⣿⣿⣿⣿⣿⣦⡘⠿⣷⣿⠿⠟⠃⠄⠄⣠⡇⠈⠻⣿⣿⣿⣿ ⣿⣿⣿⣿⡿⠟⠋⢁⣷⣠⠄⠄⠄⠄⣀⣠⣾⡟⠄⠄⠄⠄⠉⠙⠻ ⡿⠟⠋⠁⠄⠄⠄⢸⣿⣿⡯⢓⣴⣾⣿⣿⡟⠄⠄⠄⠄⠄⠄⠄⠄ ⠄⠄⠄⠄⠄⠄⠄⣿⡟⣷⠄⠹⣿⣿⣿⡿⠁⠄⠄⠄⠄⠄⠄⠄⠄ ⠄⠄⠄⠄⠄⠄⣸⣿⡷⡇⠄⣴⣾⣿⣿⠃⠄⠄⠄⠄⠄⠄⠄⠄⠄ ⠄⠄⠄⠄⠄⠄⣿⣿⠃⣦⣄⣿⣿⣿⠇⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄ ⠄⠄⠄⠄⠄⢸⣿⠗⢈⡶⣷⣿⣿⡏⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄",
            "gav": "joe biden. joe biden. joe biden. joe biden. this message from mohammad khanaqin, full face of kurdistan, for you, joe biden. you go check up on a doctor, you have 2 yil. your life is 2 yil. 2 yil from now, from today, to 2 yil uh 1 yil in 6 months. 2 yil. your life. after this one you will pass away. you go check up on a doctor, this message from mohammad khanaqin, full face of kurdistan. you do - do you - good job for the usa for the [unintelligible] in 2 yil, you do [unintelligible] you wanna kurdistan cannon, new country, no more iran, no more iraq, no more turkey, no more syria. full face of kurdistan will give you-",
            "bhatta": "Need robux to fund boblos empire. Pls donate ⣿⣿⣿⣿⣿⡿⠿⠻⠿⠿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠿⠻⠻⠟⠻⢿⣿⣿⣿⣿ ⣿⣿⡟⠁⢀⣠⣤⣤⣤⣤⣄⣀⣀⣀⣹⣿⣿⣷⣄⣀⣀⣀⣀⣤⣤⣤⣤⣀⠐⢽⣿⣿⣿ ⣿⣿⣿⣶⣿⡿⣛⡒⠒⠒⢒⠒⣲⠙⣿⣿⣿⣿⠟⣵⡒⢒⠒⠒⡀⣘⡻⣿⣿⣾⣿⣿⣿ ⣿⣿⣿⣿⣏⣞⡛⠃⠀⠀⠸⠷⢿⣧⣿⣿⣿⣿⣧⣿⣷⣛⣀⣀⣁⣛⣛⣮⣿⣿⣿⣿⣿ ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿ ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿ ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢏⣾⣿⣿⣿⣿ ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⢻⣿⠏⣼⣿⣿⣿⣿⣿ ⣿⣿⣿⣿⣿⣿⣿⣿⡿⢿⣿⣿⣿⣿⣿⣿⡿⠿⠿⠿⠟⢛⣉⣴⣿⡏⣸⣿⣿⣿⣿⣿⣿ ⣿⣿⣿⣿⣿⣿⣿⣿⣧⣠⣤⣤⣤⣤⣤⣤⣶⣶⣶⣶⣿⣿⣿⣿⣿⠃⣿⣿⣿⣿⣿⣿⣿ ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣾⣿⣿⣿⣿⣿⣿⣿",
            "kpop": "imagine instead of kpop it was rpop and it’s from Russia and you had girls all over twitter being like “Stream Я какала вщтань” and posting pictures going “OMG lvonovativich looks so CUTE” \nimagine if instead of kpop it was dpop and it's from germany and you had girls all over Twitter being like 'stream Donau­dampf­schiffahrts­elektrizitäten­haupt­betriebs­werk­bau­unter­beamten­gesellschaft' and posting pictures like this and being like 'OMG Rudolf looks so CUTE' \nimagine if instead of kpop it was bpop and it's from Brazil and you had girls all over Twitter being like 'stream Comi o cu de quem tá lendo' and posting pictures like this and being like 'OMG Ayrton looks so CUTE'",
            "hentai": "Watashi wa 👅 a 👌 victim of 💦 cyberbullying. Everyday 🗓 someone 👤 online 💻 calls 🗣 me 😭 a 👌 'weeb' desu. 👌 Watashi won't 🚫 stand 💨 for 🍆 this. 👈 26 percent 🔟 of 💦 bullying 😂 victims are 🔢 chosen due to 💦 their 🍆 race 🖕 or 💁 religion 🕋 desu. 👌 I 👁 may 🗓 look 👀 like 💖 a 👌 basic 🚂 white 👱 boy, 👦 but 🍑 deep 😱 down 🔻 I 👁 am 👏 Nihongo desu. 👌 Watashi religion 🕋 is 💦 anime. 😹 Anata wa 👅 bullying 😂 me 😭 because 💁 of 💦 my 👨 race 🖕 and 👏 religion 🕋 desu 👌 ka? Disgusting 😝 desu. 👌 Anata should 💘 be 🐝 ashamed 😳 of 💦 yourself, 🙄 pig. A 👌 baka gaijin like 💖 anata is 💦 probably 😻 jealous 😒 of 💦 my 👨 race 🖕 and 👏 culture, cause 💋 Nippon is 💦 more 🍗 sugoi than 👉 your 👏 shitty 💩 country 🏃 desu. 👌 Watashi pity 😢 anata. You'll 👉 never 🙅 be 🐝 Nihongo like 💖 watashi. I'm 💘 a 👌 weeb? Pfft. I 👁 AM 👏 AN 👹 OTAKU DESU. 👌 Educate yourself 🙄 on 🔛 nani a 👌 'weeb' is 💦 before 😂 anata try 😐 to 💦 insult 😦 watashi desu. 👌 I 👁 WILL 👏 NOT 🚫 BE 🐝 CYBERBULLIED ANYMORE. 🔥 REPORTED. Arigatou 💘 for my first gold💦 and silver🔥 , Stranger sama💋 👅",
        }

        amogus_copypasta = [
            "It’s just a sussy baka and it cannot be that bad. I’m feeling like👹imposter👹I might just be a monster😨😨😨Feeling ☺️kinda crew...😳Got many tasks🔨🔦🔌To do🤨🤨",
            "This game has ruined my fucking life. I'm going to end it and take you all with me because I can't bear to look at anything anymore. Any shape I see is distorted into amogus, any time I hear the word suspicious, sus, task, vent, report, ANYTHING, human pattern recognition turns it into amogus. I close my eyes and i see amogus, i see jerma985 grinning as the gates of my soul are opened by amogus and I can feel the festering sclunge of words and shapes pour in, filling all that I am with the ringing noise of amogus",
            "‼️‼️HOLY FUCKING 🖕👦 SHIT‼️‼️‼️‼️ IS THAT A MOTHERFUCKING 👩💞 AMONG 💰 US 🇺🇸 REFERENCE??????!!!!!!!!!!11!1!1!1!1!1!1 😱! 😱😱😱😱😱😱😱 AMONG 💑👨‍❤️‍👨👩‍❤️‍👩 US 👨 IS THE BEST 👌💯 FUCKING 💦🍆👀 GAME 🎮 🔥🔥🔥🔥💯💯💯💯 RED 🔴 IS SO SUSSSSS 🕵️🕵️🕵️🕵️🕵️🕵️🕵️🟥🟥🟥🟥🟥 COME 💦🏃🏃‍♀️ TO MEDBAY AND WATCH 👀 ME SCAN 👀 🏥🏥🏥🏥🏥🏥🏥🏥 🏥🏥🏥🏥 WHY 😡🤔 IS NO ⚠🚫 ONE 1️⃣ FIXING 👾 O2 🅾 🤬😡🤬😡🤬😡🤬🤬😡🤬🤬😡 OH 🙀 YOUR 👉 CREWMATE? NAME 📛 EVERY 💯 TASK 📋 🔫😠🔫😠🔫😠🔫😠🔫😠 Where Any sus!❓ ❓ Where!❓ ❓ Where! Any sus!❓ Where! ❓ Any sus!❓ ❓ Any sus 🌈🏳️‍🌈! ❓ ❓ ❓ ❓ Where!Where!Where! Any sus!Where!Any sus 🌈🏳️‍🌈 Where!❓ Where! ❓ Where!Any sus❓ ❓ Any sus 💦! ❓ ❓ ❓ ❓ ❓ ❓ Where! ❓ Where! ❓ Any sus!❓ ❓ ❓ ❓ Any sus 🌈🏳️‍🌈! ❓ ❓ Where!❓ Any sus 💦! ❓ ❓ Where!❓ ❓ Where! ❓ Where!Where! ❓ ❓ ❓ ❓ ❓ ❓ ❓ Any sus!❓ ❓ ❓ Any sus!❓ ❓ ❓ ❓ Where! ❓ Where! Where!Any sus!Where! Where! ❓ ❓ ❓ ❓ ❓ ❓ I 👥 think 🤔 it was purple!👀👀👀👀👀👀👀👀👀👀It wasnt me I 👁 was in vents!!!!!!!!!!!!!!😂🤣😂🤣😂🤣😂😂😂🤣🤣🤣😂😂😂",
            "It seems like the more I (13 M) play Amongus, the more my family tries to embaras me. The other day, I overheard my dad (49 M) say that he needed to 'complete tasks' while working at home😯🤬 don't worry it gets worse. Then I hear my Mom (42 F) say that the amount of time I spend on my computer is 'suspiscios.' Ummm ok so (#1) ur too good to say 'sus' 🤔 and (#2) u dont even play amogus??? 😂😂😂. Even my moms work friend (28 M or somthing idk) came over yesterday to 'look at her vents' I'm not even making this up 🙄🙄🙄 But then the worse part😑 every sunday my granpa (69 M) comes over. He reminisces about his 'Crewmates' from his Navy days and apparently a few of them died so u cry about it at dinner? Just start a new game FFS 😆 but he's lying so uhhh we get it bro: u just want attention 😯😅🤣The problem is NONE of them even Play Omungus. How do i tell em that being a poser is a cringe Brie Larson unholesome Black History Month anti-chungus move?",
            "📮📮 📮 📮 📮📮 📮 📮 📮 📮 📮 📮 📮 📮 📮 📮 📮 📮 📮 📮 📮 📮 📮 📮 📮 📮 📮📮 📮📮📮 📮📮 OMG GUYS🤯🤯🤯!!!! THE MAILBOX IS AN IMPOSTER📮😂🤣🤣🤣😳!!! HE IS SO SUS!!!! (THIS IS A REFERENCE TO THE POPULAR MOBIL AND COMPUTER GAMG AMONG US) 🤣🤣😳😳😂😂😂😂😝😝😝📮😳",
            "I am a concerned mother with a 13 year old child and I am here to seek help regarding my son. Last week when we went to the supermarket, my son pointed to a red trash can and started jumping around screaming “THAT’S AMONG US! THAT TRASH CAN IS SUS! RED IS THE IMPOSTOR!” As soon as he did that, the manager told us to leave. I told him that my son is just excited about something, and apologised. But the manager still told us to leave so I picked up the red trash can that my son was going crazy over and threw it on the managers head. Then my son shouted “DEAD BODY REPORTED.” Can someone please tell me what on earth is wrong with him?",
        ]

        if message.author == client.user:
            return

        if re.search(pattern, message.content.lower()):
            await message.channel.send(amogus_copypasta[random.randint(1, len(amogus_copypasta) - 1)])

        for key, value in easter_eggs.items():
            if key in message.content.lower():
                await message.channel.send(value)


susbot = Susbot(pattern, DISCORD_TOKEN)
client.run(DISCORD_TOKEN)
