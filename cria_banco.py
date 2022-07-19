import sqlite3

# creates connection
connection = sqlite3.connect('hotel.db')
# creates cursor into connection to execute queries
cursor = connection.cursor()

# sql script to generate table
cria_tabela = "CREATE TABLE IF NOT EXISTS hoteis (hotel_id text PRIMARY KEY,\
   nome text, estrelas real, diaria real, cidade text)"

cria_hotel = "INSERT INTO hoteis VALUES ('alpha', 'Alpha Hotel', 4.3, 345.30, 'Sao Paulo')"

# executes script into sgbd
cursor.execute(cria_tabela)
cursor.execute(cria_hotel)

# commits script commands
connection.commit()

# closes connection
connection.close()
