# IMPORT LIBRARIES
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import pymysql
import mysql.connector
# CONNECTION BETWEEN PYTHON AND MYSQL
connection = mysql.connector.connect(
host="127.0.0.1",
user="root",
password="Shirisha@7569",
database="crimedata"
)
cursor = connection.cursor()

#Location Analysis:
#Where do most crimes occur based on the "Location" column?

query = "SELECT `Location`, COUNT(*) as CrimeCount FROM crime_data WHERE `Location` IS NOT NULL GROUP BY `Location` ORDER BY CrimeCount DESC LIMIT 10"
cursor.execute(query)
result = cursor.fetchall()

# Extract locations and crime counts
locations = [row[0] for row in result]
crime_counts = [row[1] for row in result]

# Close the connection
connection.close()

# Plot a bar chart to show top crime locations
plt.bar(locations, crime_counts)
plt.xlabel('Location')
plt.ylabel('Number of Crimes')
plt.title('Top Crime Locations')
plt.show()