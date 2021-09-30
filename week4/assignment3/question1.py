import sqlite3
import configparser
from sqlalchemy import MetaData
from sqlalchemy_schemadisplay import create_schema_graph

con = sqlite3.connect("database.sqlite")
cursor = con.cursor()
# b) Print the names of both the Home Teams and Away Teams in each match played in 2015 and
#                                                                                   Full time Home Goals (FTHG) = 5
cursor.execute("SELECT HomeTeam, AwayTeam FROM Matches WHERE Season = 2015 AND FTHG = 5")
results = cursor.fetchall()
print("The HomeTeam and AwayTeam are:")
for row in results:
    print(row)

# c) Print the details of the matches where Arsenal is the Home Team and  Full Time Result (FTR) is “A” (Away Win)
cursor.execute("SELECT * FROM Matches WHERE HomeTeam = 'Arsenal' AND FTR = 'A'")
results = cursor.fetchall()
print("The Details are :")
for row in results:
    print(row[0])

# d) Print all the matches from the 2012 season till the 2015 season where Away Team is Bayern Munich
#                                                                               and Full time Away Goals (FTHG) > 2
cursor.execute("SELECT * FROM Matches WHERE Season BETWEEN 2012 AND 2015 AND "
               "AwayTeam = 'Bayern Munich' AND FTHG > 2")
results = cursor.fetchall()
print("The matches from 2012 - 2015 ,Away Team is Bayern Munich and Full time Away Goals (FTHG) > 2 are:")
for row in results:
    print(row[0])

# e) Print all the matches where the Home Team name begins with “A” and Away Team name begins with “M”
cursor.execute("SELECT Match_ID,HomeTeam,AwayTeam FROM Matches WHERE HomeTeam LIKE 'A%' AND AwayTeam LIKE 'M%'")
results = cursor.fetchall()
print("Matches where the Home Team name begins with “A” and Away Team name begins with “M:”")
for row in results:
    print(row)
con.commit()
con.close()
