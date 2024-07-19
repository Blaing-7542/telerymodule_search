import wikipediaapi
from pyrogram import Client, filters


wiki_wiki = wikipediaapi.Wikipedia(
    language='ru',
    extract_format=wikipediaapi.ExtractFormat.WIKI,
    user_agent='TeleryUserBot/1.0'
)

with open("userbot.info", "r") as file:
    lines = file.readlines()
    prefix_userbot = lines[2].strip()

cinfo = f"🔎`{prefix_userbot}search`"
ccomand = " Ищет информацию в википедии."


def command_search(app):
    @app.on_message(filters.command(["search"], prefixes=prefix_userbot))
    def search_command(_, message):
        query = message.text.split(' ', 1)[1]
        page_py = wiki_wiki.page(query)
        if page_py.exists():
            response = "**🧠Нашёл ответ:**\n\n" + page_py.text[:1024]
            message.edit_text(response)
        else:
            message.edit_text("❌Статья не найдена на Википедии.")

print("Модуль search загружен!")
