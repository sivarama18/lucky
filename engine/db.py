import sqlite3

con = sqlite3.connect("lucky.db")
cursor = con.cursor()

#query = "CREATE TABLE IF NOT EXISTS sys_command(id integer primary key,name VARCHAR(100), path VARCHAR(1000))"
#cursor.execute(query)


#query = "INSERT INTO sys_command VALUES (null,'', '')"
#cursor.execute(query)
#con.commit()

#query = "CREATE TABLE IF NOT EXISTS web_command(id integer primary key,name VARCHAR(100), url VARCHAR(1000))"
#cursor.execute(query)

#query = "INSERT INTO web_command VALUES (null,'chatgpt', 'https://chatgpt.com/')"
#cursor.execute(query)
#con.commit()

#testing module
#app_name = "one note"
#cursor.execute('SELECT path FROM sys_command WHERE name IN (?)', (app_name,))
#results = cursor.fetchall()
#print(results[0][0])