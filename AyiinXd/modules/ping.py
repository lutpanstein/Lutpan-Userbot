# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.d (the "License");
# you may not use this file except in compliance with the License.
#
# ReCode by @mrismanaziz
# FROM Man-Userbot <https://github.com/mrismanaziz/Man-Userbot>
# t.me/SharingUserbot & t.me/Lunatic0de


import time
from datetime import datetime

from speedtest import Speedtest

from AyiinXd import CMD_HANDLER as cmd
from AyiinXd import CMD_HELP, StartTime
from AyiinXd.ayiin import edit_or_reply, humanbytes, ayiin_cmd
from time import sleep


async def get_readable_time(seconds: int) -> str:
    count = 0
    up_time = ""
    time_list = []
    time_suffix_list = ["s", "m", "Jam", "Hari"]

    while count < 4:
        count += 1
        remainder, result = divmod(
            seconds, 60) if count < 3 else divmod(
            seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)

    for x in range(len(time_list)):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        up_time += f"{time_list.pop()}, "

    time_list.reverse()
    up_time += ":".join(time_list)

    return up_time


@ayiin_cmd(pattern="ping$")
async def _(ping):
    uptime = await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    Ayiin = await edit_or_reply(ping, "**Bentar bang**")
    await Ayiin.edit("**lagi ngeping**")
    await Ayiin.edit("**kek deres aja gikesanlu**")
    await Ayiin.edit("**kata Lutpan klo deresยฒ ntar kelimit**")
    await Ayiin.edit("**eh ini ping lu segini bejirrr**")
    end = datetime.now()
    duration = (end - start).microseconds / 1000
    user = await ping.client.get_me()
    await Ayiin.edit("๐ต")
    sleep(3)
    await Ayiin.edit(
        f"**โ ๐ป๐๐๐ฟ๐ฐ๐ฝ ๐๐๐ด๐๐ฑ๐พ๐ โ**\n\n"
        f"โ **๐ฟ๐ธ๐ฝ๐ถ๐ด๐ โ** `%sms`\n"
        f"โ **๐๐ฟ๐๐ธ๐ผ๐ด โ** `{uptime}` \n"
        f"โ **๐พ๐๐ฝ๐ด๐ โ** [{user.first_name}](tg://user?id={user.id})" % (duration)
    )


@ayiin_cmd(pattern="xping$")
async def _(ping):
    uptime = await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    xping = await edit_or_reply(ping, "`Pinging....`")
    end = datetime.now()
    duration = (end - start).microseconds / 1000
    await xping.edit(
        f"**PONG!! ๐ญ**\n**Pinger** : %sms\nLutpanUbot nyala ya bejirrr\n**Bot Uptime** : {uptime}๐" % (duration)
    )


@ayiin_cmd(pattern="lping$")
async def _(ping):
    uptime = await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    lping = await edit_or_reply(ping, "**โ PING โ**")
    await lping.edit("**โโ PING โโ**")
    await lping.edit("**โโโ PING โโโ**")
    await lping.edit("**โโโโ PING โโโโ**")
    await lping.edit("**โฆาออโณ PONG!**")
    end = datetime.now()
    duration = (end - start).microseconds / 1000
    user = await ping.client.get_me()
    await lping.edit(
        f"โ **Ping !!** "
        f"`%sms` \n"
        f"โ **Uptime -** "
        f"`{uptime}` \n"
        f"**โฆาออโณ Master :** [{user.first_name}](tg://user?id={user.id})" % (duration)
    )


@ayiin_cmd(pattern="keping$")
async def _(pong):
    await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    kopong = await edit_or_reply(pong, "**ใโ๐๐๐๐๐๐ใ**")
    await kopong.edit("**โโ๐๐๐๐๐๐๐โโ**")
    await kopong.edit("**๐๐๐๐๐๐๐๐ ๐๐๐๐ ๐๐๐ ๐๐๐**")
    await kopong.edit("**โฌ๐๐๐๐ ๐๐๐๐๐๐๐ ๐๐๐๐๐๐๐๐ ๐๐๐โฌ**")
    end = datetime.now()
    duration = (end - start).microseconds / 1000
    user = await pong.client.get_me()
    await kopong.edit(
        f"**โฒ ๐บ๐พ๐ฝ๐๐พ๐ป ๐ผ๐ด๐ป๐ด๐ณ๐๐ถ** "
        f"\n โซธ ๐บ๐พ๐ฝ๐๐พ๐ป `%sms` \n"
        f"**โฒ ๐ฑ๐ธ๐น๐ธ ๐ฟ๐ด๐ป๐ด๐** "
        f"\n โซธ ๐บ๐ฐ๐ผ๐ฟ๐ฐ๐ฝ๐ถใ[{user.first_name}](tg://user?id={user.id})ใ \n" % (duration)
    )


# .keping & kping Coded by Koala


@ayiin_cmd(pattern=r"kazu$")
async def _(pong):
    uptime = await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    kping = await edit_or_reply(pong, "8โ===D")
    await kping.edit("8=โ==D")
    await kping.edit("8==โ=D")
    await kping.edit("8===โD")
    await kping.edit("8==โ=D")
    await kping.edit("8=โ==D")
    await kping.edit("8โ===D")
    await kping.edit("8=โ==D")
    await kping.edit("8==โ=D")
    await kping.edit("8===โD")
    await kping.edit("8==โ=D")
    await kping.edit("8=โ==D")
    await kping.edit("8โ===D")
    await kping.edit("8=โ==D")
    await kping.edit("8==โ=D")
    await kping.edit("8===โD")
    await kping.edit("8===โD๐ฆ")
    await kping.edit("8====D๐ฆ๐ฆ")
    await kping.edit("**Lutpan**")
    await kping.edit("**DISINI Lutpan ya ajgggg.....**")
    end = datetime.now()
    duration = (end - start).microseconds / 1000
    await kping.edit("๐ต")
    sleep(3)
    await kping.edit(
        f"**LUTPAN DISINIII**\n**๐ฟ๐ธ๐ฝ๐ถ๐ด๐** : %sms\n**๐ฑ๐พ๐ ๐๐ฟ๐๐ธ๐ผ๐ด** : {uptime}๐" % (duration)
    )


@ayiin_cmd(pattern="speedtest$")
async def _(speed):
    xxnx = await edit_or_reply(speed, "`Running speed test...`")
    test = Speedtest()
    test.get_best_server()
    test.download()
    test.upload()
    test.results.share()
    result = test.results.dict()
    msg = (
        f"**Started at {result['timestamp']}**\n\n"
        "**Client**\n"
        f"**ISP :** `{result['client']['isp']}`\n"
        f"**Country :** `{result['client']['country']}`\n\n"
        "**Server**\n"
        f"**Name :** `{result['server']['name']}`\n"
        f"**Country :** `{result['server']['country']}`\n"
        f"**Sponsor :** `{result['server']['sponsor']}`\n\n"
        f"**Ping :** `{result['ping']}`\n"
        f"**Upload :** `{humanbytes(result['upload'])}/s`\n"
        f"**Download :** `{humanbytes(result['download'])}/s`"
    )
    await xxnx.delete()
    await speed.client.send_file(
        speed.chat_id,
        result["share"],
        caption=msg,
        force_document=False,
    )


@ayiin_cmd(pattern="pong$")
async def _(pong):
    start = datetime.now()
    xx = await edit_or_reply(pong, "`Sepong`")
    await xx.edit("Sepong Sayang.....")
    end = datetime.now()
    duration = (end - start).microseconds / 9000
    await xx.edit("๐ต")
    sleep(3)
    await xx.edit("**๐ฟ๐ธ๐ฝ๐ถ!**\n`%sms`" % (duration))


CMD_HELP.update(
    {
        "ping": f"**Plugin : **`ping`\
        \n\n  ยป  **Perintah :** `{cmd}ping` ; `{cmd}lping` ; `{cmd}xping` ; `{cmd}kazu`\
        \n  ยป  **Kegunaan : **Untuk menunjukkan ping userbot.\
        \n\n  ยป  **Perintah :** `{cmd}pong`\
        \n  ยป  **Kegunaan : **Sama seperti perintah ping\
    "
    }
)


CMD_HELP.update(
    {
        "speedtest": f"**Plugin : **`speedtest`\
        \n\n  ยป  **Perintah :** `{cmd}speedtest`\
        \n  ยป  **Kegunaan : **Untuk Mengetes kecepatan server userbot.\
    "
    }
)
