import time
import sqlite3

class Banco():
    def __init__ (self):
        pass

    def novoBichin(self, nome, fome, tedio, cor):
        try:
            with sqlite3.connect('tamagushis.db') as connection:
                    cursor = connection.cursor()
                    visto = time.time()
                    cursor.execute('INSERT INTO tamagushis(nome,fome, tedio, idade, visto, cor ) VALUES(?, ?, ?, ?, ?, ?)', (nome, fome, tedio, 0, visto, cor))
                    connection.commit()
            return True
        except:
            return False


connection = sqlite3.connect('tamagushis.db')
cursor = connection.cursor()
cursor.execute("""
    CREATE TABLE IF NOT EXISTS tamagushis(
        id INTEGER PRIMARY KEY NOT NULL,
        nome STR NOT NULL,
        fome FLOAT NOT NULL,
        tedio FLOAT NOT NULL,
        idade INTEGER NOT NULL,
        visto DOUBLE FLOAT NOT NULL,
        cor INTEGER NOT NULL
)""")