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
Hello, !!
Nice To Meet You 🤗 !!
I guess, that you know me, Uhh you don't, np..
Well I'm Mᴜsɪᴄ Bᴏᴛ.
A Pᴏᴡᴇʀғᴜʟ Mᴜsɪᴄ ᴀssɪᴛᴀɴᴛ ᴏғ [Tʜᴇ Sʜᴀsʜᴀɴᴋ⚡️](t.me/theshashank)
                           Pᴏᴡᴇʀᴇᴅ Bʏ [Wʜɪᴛᴇ Dᴇᴠɪʟ](t.me/Whitedevil_support)
I ᴄᴀɴ sᴛʀᴇᴀᴍ ᴍᴜsɪᴄ ɪɴ ᴠᴏɪᴄᴇ ᴄʜᴀᴛ 😊😊.""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "⚒COMMANDS", url="https://telegra.ph/Music-Bot-04-06"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "My sweet creator ☺️", url="https://t.me/theshashank"
                    ),
                    InlineKeyboardButton(
                        "creator ki jaan🤭", url="https://t.me/cutie1145"
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
