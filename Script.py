class script(object):
    START_TXT = """**ഞാൻ ഒരു 𝐀𝐔𝐓𝐎 𝐅𝐈𝐋𝐓𝐄𝐑 𝐁𝐎𝐓 ആണ്, എന്റെ ഉടമസ്ഥർ  <a href='https://t.me/+8TAZr0iTGgQ1MmI1'>CINEMA-HUB</a> ആണ്, നിങ്ങൾക്കും നിങ്ങളുടെ ഗ്രൂപ്പുകളിൽ ഇപ്പോൾ എന്നെ ഉപയോഗിക്കാവുന്നതാണ്**"""
    HELP_TXT = """𝙷𝙴𝚈 {}
𝙷𝙴𝚁𝙴 𝙸𝚂 𝚃𝙷𝙴 𝙷𝙴𝙻𝙿 𝙵𝙾𝚁 𝙼𝚈 𝙲𝙾𝙼𝙼𝙰𝙽𝙳𝚂."""
    ABOUT_TXT = """✯ 𝙼𝚈 𝙽𝙰𝙼𝙴: {}
✯ Cʀᴇᴀᴛᴏʀ: <a href='https://t.me/BATMAN_CINEMAHUB'>Tʜɪs ᴘᴇʀsᴏɴ</a>
✯ Lɪʙʀᴀʀʏ: <a href='https://docs.pyrogram.org/'>Pʏʀᴏɢʀᴀᴍ</a>
✯ Lᴀɴɢᴜᴀɢᴇ: <a href='https://www.python.org/download/releases/3.0/'>Pʏᴛʜᴏɴ 3</a>
✯ DᴀᴛᴀBᴀsᴇ: <a href='https://www.mongodb.com/'>MᴏɴɢᴏDB</a>
✯ Bᴏᴛ Sᴇʀᴠᴇʀ: <a href='https://t.me/MYFASTSERVERR'>Qᴜɪᴄᴋ Fᴀsᴛ</a>
✯ Bᴜɪʟᴅ Sᴛᴀᴛᴜs: v2.0.3 [ Sᴛᴀʙʟᴇ ]</b>"""
    SOURCE_TXT = """<b>NOTE:</b>
- Jerry is a private project. 

<b>DEVS:</b>
- <a href=https://t.me/BATMAN_CINEMAHUB>BÀTMAN™</a>"""
            
    BUTTON_TXT = """Help: <b>Buttons</b>

- Bot Supports both url and alert inline buttons.

<b>NOTE:</b>
1. Telegram will not allows you to send buttons without any content, so content is mandatory.
2. Jerry supports buttons with any telegram media type.
3. Buttons should be properly parsed as markdown format

<b>URL buttons:</b>
<code>[Button Text](buttonurl:https://t.me/EvaMariaBot)</code>

<b>Alert buttons:</b>
<code>[Button Text](buttonalert:This is an alert message)</code>"""
    AUTOFILTER_TXT = """Help: <b>Auto Filter</b>

<b>NOTE:</b>
1. Make me the admin of your channel if it's private.
2. make sure that your channel does not contains camrips, porn and fake files.
3. Forward the last message to me with quotes.
 I'll add all the files in that channel to my db."""
    CONNECTION_TXT = """Help: <b>Connections</b>

- Used to connect bot to PM for managing filters 
- it helps to avoid spamming in groups.

<b>NOTE:</b>
1. Only admins can add a connection.
2. Send <code>/connect</code> for connecting me to ur PM

<b>Commands and Usage:</b>
• /connect  - <code>connect a particular chat to your PM</code>
• /disconnect  - <code>disconnect from a chat</code>
• /connections - <code>list all your connections</code>"""    
    EXTRAMOD_TXT = """Help: <b>Extra Modules</b>

<b>NOTE:</b>
these are the extra features of Eva Maria

<b>Commands and Usage:</b>
• /id - <code>get id of a specified user.</code>
• /info  - <code>get information about a user.</code>
• /imdb  - <code>get the film information from IMDb source.</code>
• /search  - <code>get the film information from various sources.</code>"""
    ADMIN_TXT = """Help: <b>Admin mods</b>

<b>NOTE:</b>
This module only works for my admins

<b>Commands and Usage:</b>
• /logs - <code>to get the rescent errors</code>
• /stats - <code>to get status of files in db.</code>
• /delete - <code>to delete a specific file from db.</code>
• /users - <code>to get list of my users and ids.</code>
• /chats - <code>to get list of the my chats and ids </code>
• /leave  - <code>to leave from a chat.</code>
• /disable  -  <code>do disable a chat.</code>
• /ban  - <code>to ban a user.</code>
• /unban  - <code>to unban a user.</code>
• /channel - <code>to get list of total connected channels</code>
• /broadcast - <code>to broadcast a message to all users</code>"""
   
    CUSTOM_FILE_CAPTION = """<b>📂Fɪʟᴇɴᴀᴍᴇ : {file_name}</b>
╔════ ᴊᴏɪɴ ᴡɪᴛʜ ᴜs ═════╗
Main Channel ➧ https://t.me/+_CIGB5Zb3k4zZTg1
🎗️ʝσιи 🎗️ ѕнαяє🎗️ ѕυρρσят🎗️
╚════ ᴊᴏɪɴ ᴡɪᴛʜ ᴜs ═════╝>"""
    
    STATUS_TXT = """📂 𝖳𝗈𝗍𝖺𝗅 𝖥𝗂𝗅𝖾𝗌     - <code>{}</code>

𒆜  𝗗𝗕 1️⃣
╭ ▸ 𝖴𝗌𝖾𝗋𝗌 : <code>{}</code>
├ ▸ 𝖢𝗁𝖺𝗍𝗌  : <code>{}</code>
╰ ▸ 𝖴𝗌𝖾𝖽 𝖲𝗍𝗈𝗋𝖺𝗀𝖾: <code>{}</code>MB

 𒆜 𝗗𝗕 2️⃣
╭ ▸ 𝖳𝗈𝗍𝖺𝗅 𝖥𝗂𝗅𝖾𝗌 : <code>{}</code>
╰ ▸ 𝖴𝗌𝖾𝖽 𝖲𝗍𝗈𝗋𝖺𝗀𝖾: <code>{}</code>MB

 𒆜 𝗗𝗕 3️⃣ 
╭ ▸ 𝖳𝗈𝗍𝖺𝗅 𝖥𝗂𝗅𝖾𝗌 : <code>{}</code>
╰ ▸ 𝖴𝗌𝖾𝖽 𝖲𝗍𝗈𝗋𝖺𝗀𝖾: <code>{}</code>MB

𒆜  𝗗𝗕 4️⃣
╭ ▸ 𝖳𝗈𝗍𝖺𝗅 𝖥𝗂𝗅𝖾𝗌 : <code>{}</code>
╰ ▸ 𝖴𝗌𝖾𝖽 𝖲𝗍𝗈𝗋𝖺𝗀𝖾: <code>{}</code>MB

𒆜 𝗗𝗕 5️⃣
╭ ▸ 𝖳𝗈𝗍𝖺𝗅 𝖥𝗂𝗅𝖾𝗌 : <code>{}</code>
╰ ▸ 𝖴𝗌𝖾𝖽 𝖲𝗍𝗈𝗋𝖺𝗀𝖾: <code>{}</code>MB"""
    
    LOG_TEXT_G = """#NewGroup
Group = {}(<code>{}</code>)
Total Members = <code>{}</code>
Added By - {}
@JERRYCINEMABOT
"""
    LOG_TEXT_P = """#NewUser
ID - <code>{}</code>
Name - {}
@JERRYCINEMABOT
"""
