from fsub import Bot

from hydrogram import filters
from hydrogram.types import CallbackQuery, InlineKeyboardMarkup, Message
from hydrogram.types import InlineKeyboardButton


class Data:
    HELP = """<b>
<u> This the command of this bot </u>

/start: Start the bot
/help: Help and about bots
/ping: Check bot latency
/uptime: Check bot uptime
/users: Bot user statistics (Admin)
/batch: Multi posts in one link (Admin)
/broadcast: Broadcast message to bot users (Admin)‌‌ </b>
"""

    close = [
        [InlineKeyboardButton("Close", callback_data="close")]
    ]

    mbuttons = [
        [
            InlineKeyboardButton("Help", callback_data="help"),
            InlineKeyboardButton("Close", callback_data="close")
        ],
    ]

    buttons = [
        [
            InlineKeyboardButton("About", callback_data="about"),
            InlineKeyboardButton("close", callback_data="close")
        ],
    ]

    ABOUT = """<b>
┏━━━━━•◦●◉✿ ❟❛❟ ✿◉●◦•━━━━━━┓
┃ Developer : <a href='tg://user?id=1895952308'>Stupidboi69</a>
┃ Owner: <a href='tg://user?id=5997896353'>This Person</a>
┃ Language : Python3
┃ Library : <a href='https://docs.hydrogram.org/'>Hydrogram</a>
┗━━━━━•◦●◉✿ ❟❛❟ ✿◉●◦•━━━━━━┛</b>"""
         

@Bot.on_message(filters.private & filters.incoming & filters.command("help"))
async def help(client: Bot, message: Message):
    await client.send_message(
        message.chat.id, 
        Data.HELP,
        disable_web_page_preview=True,
        reply_markup=InlineKeyboardMarkup(Data.buttons),
    )


@Bot.on_callback_query()
async def handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        try:
            await query.message.edit_text(
                text=Data.ABOUT.format(client.username),
                disable_web_page_preview=True,
                reply_markup=InlineKeyboardMarkup(Data.mbuttons),
            )
        except Exception:
            pass
    elif data == "help":
        try:
            await query.message.edit_text(
                text=Data.HELP,
                disable_web_page_preview=True,
                reply_markup=InlineKeyboardMarkup(Data.buttons),
            )
        except Exception:
            pass
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except Exception:
            pass
