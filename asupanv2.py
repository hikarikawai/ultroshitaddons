# By https://t.me/JustRex 
# Dont delete my name!
# Appreciate my work!
# Asupan v2

"""
Plugin ini dibuat oleh @JustRex

👨‍💻 Commands Tersedia :

🎥 VIDEO :
	
• `{i}asp`
     untuk mendapatkan video asupan secara random
• `{i}prn`
    untuk mendapatkan video bokep secara random
• `{i}asv`
    untuk mendapatkan anime short video secara random
• `{i}vl`
    untuk mendapatkan video lucu secara random
• `{i}sv`
    untuk mendapatkan Sad video secara random

📷 PHOTOS :
	
• `{i}aw`
    untuk mendapatkan wallpaper anime secara random
• `{i}ppcp`
    untuk mendapatkan Mentahan foto couple secara random
• `{i}dpanime`
    untuk mendapatkan pp anime secara random
• `{i}mci`
    untuk mendapatkan meme dari meme comic indonesia
• `{i}np`
    untuk mendapatkan foto bugil secara random
•`{i}ayang`
    untuk mendapatkan ayang mu secara random (HALU)

🔈 VOICE : 
	
• `{i}desah`
    untuk mendapatkan desahan secara random
• `{i}alqu`
    untuk mendapatkan lantunan ayat dari surat alquran secara random
•`{i}ms`
    untuk mendapatkan musik metal/alternatif rock /rock secara random
•`{i}poppunk`
    untuk mendapatkan Musik Poppunk secara random
•`{i}sadsong`
    untuk mendapatkan musik galau secara random

© @JustRex 
"""

import asyncio
import random
from telethon.tl.types import InputMessagesFilterVideo
from telethon.tl.types import InputMessagesFilterPhotos
from telethon.tl.types import InputMessagesFilterVoice
from telethon.tl.types import InputMessagesFilterMusic
from telethon import events
from . import *

@ultroid_cmd(pattern=r"prn")
async def _(event):
    try:
        asupannya = [
            asupan
            async for asupan in event.client.iter_messages(
                "@notygirl", filter=InputMessagesFilterVideo
            )
        ]
        await event.client.send_file(
            event.chat_id,
            file=random.choice(asupannya),
            caption=f"Nih bokep nya! plugin by @JustRex",                   
        )
        await event.delete()
    except Exception:
        await event.edit("Tidak bisa menemukan video.")

# ANIME SHORT 
        
@ultroid_cmd(pattern=r"asv")
async def _(event):
    try:
        asupannya = [
            asupan
            async for asupan in event.client.iter_messages(
                "@jawahrshteleme", filter=InputMessagesFilterVideo
            )
        ]
        await event.client.send_file(
            event.chat_id,
            file=random.choice(asupannya),
            caption=f"This plugin made by @JustRex",                   
        )
        await event.delete()
    except Exception:
        await event.edit("Tidak bisa menemukan video.")
        
# VIDEO LUCU        

@ultroid_cmd(pattern=r"vl")
async def _(event):
    try:
        asupannya = [
            asupan
            async for asupan in event.client.iter_messages(
                "@memetelegram", filter=InputMessagesFilterVideo
            )
        ]
        await event.client.send_file(
            event.chat_id,
            file=random.choice(asupannya),
            caption=f"🤣",                   
        )
        await event.delete()
    except Exception:
        await event.edit("Tidak bisa menemukan video.")
 
# SAD VIDEO
       
@ultroid_cmd(pattern=r"sv")
async def _(event):
    try:
        asupannya = [
            asupan
            async for asupan in event.client.iter_messages(
                "@videorandom_sad", filter=InputMessagesFilterVideo
            )
        ]
        await event.client.send_file(
            event.chat_id,
            file=random.choice(asupannya),
            caption=f"dont be too sad 🥀",                   
        )
        await event.delete()
    except Exception:
        await event.edit("Tidak bisa menemukan video.")
        
# ASUPAN
        
@ultroid_cmd(pattern=r"asp")
async def _(event):
    try:
        asupannya = [
            asupan
            async for asupan in event.client.iter_messages(
                "@FYPTIKTOK2022", filter=InputMessagesFilterVideo
            )
        ]
        await event.client.send_file(
            event.chat_id,
            file=random.choice(asupannya),
            caption=f"This plugin made by @JustRex🥀",                   
        )
        await event.delete()
    except Exception:
        await event.edit("Tidak bisa menemukan video.")
        
# GAMBAR GAMBAR BUKAN VIDEO BY REXA

# ANIME WALLPAPER

@ultroid_cmd(pattern=r"aw")
async def _(event):
    try:
        asupannya = [
            asupan
            async for asupan in event.client.iter_messages(
                "@Anime_WallpapersHD", filter=InputMessagesFilterPhotos
            )
        ]
        await event.client.send_file(
            event.chat_id,
            file=random.choice(asupannya),
            caption=f"This plugin made by @JustRex",                   
        )
        await event.delete()
    except Exception:
        await event.edit("Tidak bisa menemukan video.")

# COUPLE FOTO

@ultroid_cmd(pattern=r"ppcp")
async def _(event):
    try:
        asupannya = [
            asupan
            async for asupan in event.client.iter_messages(
                "@mentahanppcp", filter=InputMessagesFilterPhotos
            )
        ]
        await event.client.send_file(
            event.chat_id,
            file=random.choice(asupannya),
            caption=f"This plugin made by @JustRex",                   
        )
        await event.delete()
    except Exception:
        await event.edit("Tidak bisa menemukan foto.")
        
# MEME COMIC INDO

@ultroid_cmd(pattern=r"mci")
async def _(event):
    try:
        asupannya = [
            asupan
            async for asupan in event.client.iter_messages(
                "@meme_comic", filter=InputMessagesFilterPhotos
            )
        ]
        await event.client.send_file(
            event.chat_id,
            file=random.choice(asupannya),
            caption=f"This plugin made by @JustRex",                   
        )
        await event.delete()
    except Exception:
        await event.edit("Tidak bisa menemukan Foto.")

# FOTO BUGIL 

@ultroid_cmd(pattern=r"np")
async def _(event):
    try:
        asupannya = [
            asupan
            async for asupan in event.client.iter_messages(
                "@durovbgst", filter=InputMessagesFilterPhotos
            )
        ]
        await event.client.send_file(
            event.chat_id,
            file=random.choice(asupannya),
            caption=f"This plugin made by @JustRex",                   
        )
        await event.delete()
    except Exception:
        await event.edit("Tidak bisa menemukan Foto.")

# PP ANIME 

@ultroid_cmd(pattern=r"dpanime")
async def _(event):
    try:
        asupannya = [
            asupan
            async for asupan in event.client.iter_messages(
                "@animehikarixa", filter=InputMessagesFilterPhotos
            )
        ]
        await event.client.send_file(
            event.chat_id,
            file=random.choice(asupannya),
            caption=f"HALO WIBU! 🇯🇵",                   
        )
        await event.delete()
    except Exception:
        await event.edit("Tidak bisa menemukan Foto.")

# INI AYANG

@ultroid_cmd(pattern=r"ayang")
async def _(event):
    try:
        asupannya = [
            asupan
            async for asupan in event.client.iter_messages(
                "@CeweLogoPack", filter=InputMessagesFilterPhotos
            )
        ]
        await event.client.send_file(
            event.chat_id,
            file=random.choice(asupannya),
            caption=f"ini ayangmu ♥️",                   
        )
        await event.delete()
    except Exception:
        await event.edit("Tidak bisa menemukan Foto.")

  

# SUARA DESAH DLL

# DESAH

@ultroid_cmd(pattern=r"desah")
async def _(event):
    try:
        asupannya = [
            asupan
            async for asupan in event.client.iter_messages(
                "@deshanhiroshi", filter=InputMessagesFilterVoice
            )
        ]
        await event.client.send_file(
            event.chat_id,
            file=random.choice(asupannya),
            caption=f"This plugin made by @JustRex",                   
        )
        await event.delete()
    except Exception:
        await event.edit("Tidak bisa menemukan suara.")

# METAL

@ultroid_cmd(pattern=r"ms")
async def _(event):
    try:
        asupannya = [
            asupan
            async for asupan in event.client.iter_messages(
                "@alternative_music_rock", filter=InputMessagesFilterMusic
            )
        ]
        await event.client.send_file(
            event.chat_id,
            file=random.choice(asupannya),
            caption=f"👨‍🎤👨‍🎤👨‍🎤",                   
        )
        await event.delete()
    except Exception:
        await event.edit("Tidak bisa menemukan suara.")
        
# POP PUNK

@ultroid_cmd(pattern=r"poppunk")
async def _(event):
    try:
        asupannya = [
            asupan
            async for asupan in event.client.iter_messages(
                "@Poppunk90", filter=InputMessagesFilterMusic
            )
        ]
        await event.client.send_file(
            event.chat_id,
            file=random.choice(asupannya),
            caption=f"🎸",                   
        )
        await event.delete()
    except Exception:
        await event.edit("Tidak bisa menemukan suara.")        

#ALQU

@ultroid_cmd(pattern=r"alqu")
async def _(event):
    try:
        asupannya = [
            asupan
            async for asupan in event.client.iter_messages(
                "@lantunan_quran", filter=InputMessagesFilterMusic
            )
        ]
        await event.client.send_file(
            event.chat_id,
            file=random.choice(asupannya),
            caption=f"🕋",                   
        )
        await event.delete()
    except Exception:
        await event.edit("Tidak bisa menemukan suara.")
  
# SAD SONG
      
@ultroid_cmd(pattern=r"sadsong")
async def _(event):
    try:
        asupannya = [
            asupan
            async for asupan in event.client.iter_messages(
                "@lagugallauu", filter=InputMessagesFilterMusic
            )
        ]
        await event.client.send_file(
            event.chat_id,
            file=random.choice(asupannya),
            caption=f"🥀",                   
        )
        await event.delete()
    except Exception:
        await event.edit("Tidak bisa menemukan suara.")    


@ultroid_cmd(pattern=r"cogan")
async def _(event):
    try:
        asupannya = [
            asupan
            async for asupan in event.client.iter_messages(
                "@galeriCogann", filter=InputMessagesFilterPhotos
            )
        ]
        await event.client.send_file(
            event.chat_id,
            file=random.choice(asupannya),
            caption=f"♥️",                   
        )
        await event.delete()
    except Exception:
        await event.edit("Tidak bisa menemukan Foto .")    

     


   
