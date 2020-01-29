#imports sqlite
import sqlite3

#connects it to the books-collection database
conn = sqlite3.connect('game-records.db')

#creates the cursor
c = conn.cursor()

#executes the query which inserts values in the table
c.execute("INSERT INTO game VALUES( 1, '[dinner, time, machine, learning, experience, required, reading, material, world, peace]', '', '[0, 9]', '[1, 8]', 0, 0, 0, 1, 0, 0, 0)")
c.execute("INSERT INTO turn VALUES( 1, 1, 1, 1, '[0,0]', 0, '', 1, 0, '', '', 1, '', 0, 0 )")
#commits the executions
conn.commit()

#closes the connection
conn.close()