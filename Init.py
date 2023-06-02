
# Build on Python 3.9.10

from discord.ext import commands as DiscCommands
from discord import Intents
import pomice as Pomice
import sqlite3 as Mysql

Db = Mysql.connect('Database.db')
Cursor = Db.cursor()

Cursor.execute('''
CREATE TABLE IF NOT EXISTS General_Preferences(
Server_Identifier INTEGER PRIMARY KEY,
Prefix TEXT,
Language TEXT
)
''')
Db.commit()

def getPrefix(Bot, Context : DiscCommands.Context):

    intIdentifier = Context.guild.id

    getIdentifierCursor = Cursor.execute('SELECT Prefix FROM General_Preferences WHERE Server_Identifier = ?', (intIdentifier,) )
    varIdentifierResult = getIdentifierCursor.fetchone()
    
    if varIdentifierResult is None:

        Cursor.execute('INSERT INTO General_Preferences (Server_Identifier, Prefix, Language) VALUES (?, ?, ?)', (intIdentifier, '!', 'English') )
        Db.commit()

        varIdentifierResult = '!'

    else: varIdentifierResult = varIdentifierResult[0]

    return varIdentifierResult
        
Bot = DiscCommands.Bot(command_prefix = ".", intents = Intents.all())

async def ConnectNode():

    await Bot.wait_until_ready()

    await Pomice.NodePool.create_node(bot = Bot, host = '', port = , password = '', identifier = 'Main', secure = False, 
                                      spotify_client_id="", 
                                      spotify_client_secret="",
                                      apple_music=)

@Bot.event

async def on_ready():

    await Bot.load_extension(f'MusicPlayer')

    Bot.loop.create_task(ConnectNode())

Bot.run('')

