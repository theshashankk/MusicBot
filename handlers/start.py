from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton


@Client.on_message(
    filters.command("start")
    & filters.private
    & ~ filters.edited
)
async def start_(client: Client, message: Message):
    await message.reply_text(
        f"""<b>👋🏻 Hi {message.from_user.first_name}!</b>

Hᴇʏ Nᴜʙ ɪ'ᴍ Nᴜʙ Isʜɪᴋᴀ Mᴜsɪᴄ ᴘʟᴀʏᴇʀ, Aɴ ᴏᴘᴇɴ-sᴏᴜʀᴄᴇ ʙᴏᴛ ᴛʜᴀᴛ ʟᴇᴛs ʏᴏᴜ ᴘʟᴀʏ ᴍᴜsɪᴄ ɪɴ ʏᴏᴜʀ ᴛᴇʟᴇɢʀᴀᴍ ɢʀᴏᴜᴘ.

Use the buttons below to know more about me.""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "⚒COMMANDS", url="https://telegra.ph/MusicBot-Robot-MusicBot-Robo-03-14"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "💬 Group", url="https://t.me/Marshmellosupport"
                    ),
                    InlineKeyboardButton(
                        "Channel 🔈", url="https://t.me/CheemsUerbot"
                    )
                ]
            ]
        )
    )


@Client.on_message(
    filters.command("start")
    & filters.group
    & ~ filters.edited
)
async def start(client: Client, message: Message):
    await message.reply_text(
        "💁🏻‍♂️ Do you want to search for a YouTube video?",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "✅ Yes", switch_inline_query_current_chat=""
                    ),
                    InlineKeyboardButton(
                        "No ❌", callback_data="close"
                    )
                ]
            ]
        )
    )
