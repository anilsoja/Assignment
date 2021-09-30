import sqlite3
con = sqlite3.connect("database.sqlite")
cursor = con.cursor()

# a) Write a query that returns the HomeTeam, FTHG (number of home goals scored in a game) and FTAG (number of away
# goals scored in a game) from the Matches table. Only include data from the 2010 season and where ‘Aachen’ is the
# name of the home team. Return the results by the number of home goals scored in a game in descending order.
print("HomeTeam, FTHG, FTAG are:")
cursor.execute("SELECT HomeTeam,FTHG,FTAG FROM Matches WHERE Season = 2010 AND HomeTeam='Aachen' ORDER BY FTHG DESC")
results = cursor.fetchall()
for row in results:
    print(row)

# b)Print the total number of home games each team won during the 2016 season in descending order
# of number of home games from the Matches table.
cursor.execute("SELECT HomeTeam, COUNT(FTR) FROM Matches WHERE Season = 2016 AND FTR ='H' GROUP BY HomeTeam ORDER BY "
               "COUNT(FTR) DESC")
results = cursor.fetchall()
print("Total no:of home games during 2016:")
for row in results:
    print(row)

# c)PWrite a query that returns the first ten rows from the Unique_Teams table
cursor.execute("SELECT * FROM Unique_Teams LIMIT 10")
results = cursor.fetchall()
print("The First 10 rows from Unique_Teams Table are:")
for row in results:
    print(row)

# d) Print the Match_ID and Unique_Team_ID with the corresponding Team_Name from the
# Unique_Teams and Teams_in_Matches tables. Use the WHERE statement first and
# then use the JOIN statement to get the same result.
cursor.execute("SELECT * FROM Teams_in_Matches T,Unique_Teams U WHERE  T.Unique_Team_ID = U.Unique_Team_ID")
results = cursor.fetchall()
print("Match_ID and Unique_Team_ID of Team_Name :")
for row in results:
    print(row)

# e) Write a query that joins together the Unique_Teams data table and the Teams table, and returns the first 10 rows.
cursor.execute("SELECT * FROM Unique_Teams U JOIN Teams T  ON U.TeamName = T.TeamName LIMIT 10")
results = cursor.fetchall()
print("First 10 rows are:")
for row in results:
    print(row)
# f)Write a query that shows the Unique_Team_ID and TeamName from the Unique_Teams table and A
# vgAgeHome, Season and ForeignPlayersHome from the Teams table. Only return the first five rows
cursor.execute("SELECT U.Unique_Team_ID,U.TeamName,T.AvgAgeHome,T.Season, T.ForeignPlayersHome FROM Unique_Teams U JOIN"
               " Teams T  ON U.TeamName = T.TeamName LIMIT 5")
results = cursor.fetchall()
print("The First 5 rows:")
for row in results:
    print(row)
# g) Write a query that shows the highest Match_ID for each team that ends in a “y” or a “r”.
# Along with the maximum Match_ID, display the Unique_Team_ID from the Teams_in_Matches table
# and the TeamName from the Unique_Teams table.
cursor.execute("SELECT MAX(Match_ID),T.Unique_Team_ID,TeamName FROM Teams_in_Matches T JOIN Unique_Teams U "
               "ON T.Unique_Team_ID =U.Unique_TEAM_ID WHERE (TeamName lIKE '%y')OR"
               "(TeamName LIKE '%r')GROUP BY T.Unique_Team_ID,TeamName")
results = cursor.fetchall()
print("Highest Match_ID ends with y or r :")
for row in results:
    print(row)
con.commit()
con.close()
