# Credits:
# 1. Aditya Bhattacharya (github: /AdityaBhattacharya1)
# 2. Garv Sachdev (github: /gavkujo)
# =====================================================
# Indent system: 4 spaces (= 1 tab). Peace is among us.

import os
from os.path import dirname, join
import random
import re
from typing import Match, List, Dict

import discord
from dotenv import load_dotenv

from copypastas import *

client = discord.Client()

dotenv_path = join(dirname(__file__), ".env")
load_dotenv(dotenv_path)
DISCORD_TOKEN = os.environ.get("DISCORD_TOKEN")


pattern: str = (
    "(electrical)(?! (engineering|engg))|sus|amogus|gus(?! (fring|fing|johnson))|imposter|vent|us$|bay|crewmate|baka"
)


class Susbot:
    def __init__(self, pattern: str, token: str) -> None:
        self.pattern = pattern
        self.token = token

    @client.event
    async def on_ready() -> None:
        print(f"We have logged in as {client.user}")

    @client.event
    async def on_message(message: str) -> None:
        def generate_regex(dict: Dict[str, str], list: List[str]) -> None:
            for key in dict.keys():
                list.append(key)

        def regex_matcher(pattern: str) -> Match:
            return re.search(pattern, message.content.lower()).group(0)

        easter_egg_detections_list: List[str] = []
        image_detection_list: List[str] = []
        separator = "|"

        # programmatically create a regex with all the keys in the following manner: "key1|key2|key3..."
        generate_regex(easter_eggs, easter_egg_detections_list)
        generate_regex(image_easter_eggs, image_detection_list)

        pattern2 = separator.join(easter_egg_detections_list)
        pattern3 = separator.join(image_detection_list)

        if message.author == client.user:
            return

        # if re.search returns None (there is no match), there will be an attrib error. These try-excepts are to prevent that.
        try:
            regex_matcher(pattern)
            await message.channel.send(amogus_copypasta[random.randint(1, len(amogus_copypasta) - 1)])

        except AttributeError:
            try:
                await message.channel.send(easter_eggs[regex_matcher(pattern2)])

            except AttributeError:
                try:
                    await message.channel.send(image_easter_eggs[regex_matcher(pattern3)])

                except AttributeError:
                    return

        # Not a fan of nested try-except blocks? Comment that out and use the following code instead.
        # try:
        #     regex_matcher(pattern)
        #     await message.channel.send(amogus_copypasta[random.randint(1, len(amogus_copypasta) - 1)])

        # except AttributeError:
        #     pass

        # try:
        #     await message.channel.send(easter_eggs[regex_matcher(pattern2)])

        # except AttributeError:
        #     pass

        # try:
        #     await message.channel.send(image_easter_eggs[regex_matcher(pattern3)])

        # except AttributeError:
        #     return


susbot = Susbot(pattern, DISCORD_TOKEN)
client.run(DISCORD_TOKEN)