
# Build on Python 3.9.10

from discord.ext import commands as DiscCommands
from discord import Intents
from configparser import ConfigParser
import sqlite3 as Mysql

class Init(DiscCommands.Bot):

    def __init__(Self):

        Self.Intetns = Intents.all()

        Self.Db = Mysql.connect('Database.db')

        Self.Cursor = Self.Db.cursor()

        # Create table if not exists.

        Self.Cursor.execute(f'''
        
        CREATE TABLE IF NOT EXISTS Users (
            User_Identifier Int,
            Server_Identifier Int,
            Prefix Char(1) Default {Ini['Init']['DefaultPrefix']},
            Language Varchar(12) Default {Ini['Init']['DefaultLangauge']},
            Primary Key (User_Identifier)
        )

        ''')
        Self.Db.commit()

        super().__init__(command_prefix = Self.RequestPrefix, intents = Self.Intetns)

    def RequestPrefix(Self, Bot, Context : DiscCommands.Context):

        Author, Server = Context.author.id, Context.guild.id

        varPrefix = Self.Cursor.execute('SELECT Prefix FROM Users WHERE User_Identifier = ? AND Server_Identifier = ?', (Author, Server) ).fetchone()

        if varPrefix is None:

            Self.Cursor.execute('INSERT INTO Users (User_Identifier, Server_Identifier) VALUES (?, ?)', (Author, Server) )
            Self.Db.commit()

            varPrefix = Ini['Init']['DefaultPrefix']

        else: varPrefix = varPrefix[0]

        return varPrefix
    
    async def on_ready():

        await super().load_extension(f'Music Player')

Ini = ConfigParser()
Ini.read(f'Configuration.ini')

Bot = Init()
Bot.run(Ini['Init']['Token'])
