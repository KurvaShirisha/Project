# IMPORT LIBRARIES
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import pymysql
import mysql.connector

#CONNECTION BETWEEN PYTHON AND MYSQL
connection = mysql.connector.connect(
host="127.0.0.1",
user="root",
password="Shirisha@7569",
database="crimedata"
)
cursor = connection.cursor()

#Victim Demographics:
#What is the distribution of victim ages in reported crimes?
query = "SELECT `Vict_Age` FROM crime_data WHERE `Vict_Age` IS NOT NULL"
cursor.execute(query)
result = cursor.fetchall()

# Extract victim ages
Vict_Age = [row[0] for row in result]

# Close the connection
connection.close()

# Plot a histogram of victim ages
plt.hist(Vict_Age, bins=20, edgecolor='black')
plt.xlabel('Victim Age')
plt.ylabel('Number of Crimes')
plt.title('Distribution of Victim Ages in Reported Crimes')
plt.show()