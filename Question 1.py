# IMPORT LIBRARIES
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import pymysql
import mysql.connector

# CONNECTION BETWEEN PYTHON ANS MYSQL
connection = mysql.connector.connect(
host="127.0.0.1",
user="root",
password="Shirisha@7569",
database="crimedata"
)
cursor = connection.cursor()

#Spatial Analysis:
#Where are the geographical hotspots for reported crimes?

query = "SELECT LAT, LON, COUNT(*) as CrimeCount FROM crime_data GROUP BY LAT, LON ORDER BY CrimeCount DESC "
cursor.execute(query)
result = cursor.fetchall()

# Extract latitude, longitude, and crime count
#LIST COMPRAHENSION
LAT= [row[0] for row in result]
LON = [row[1] for row in result]
crime_counts = [row[2] for row in result]

# Close the connection
connection.close()

# Visualize the hotspots on a scatter plot
plt.scatter(LON, LAT, c=crime_counts, cmap='viridis', s=crime_counts, alpha=0.7)
plt.colorbar(label='Number of Crimes')
plt.xlabel('LON')
plt.ylabel('LAT')
plt.title('Geographical Hotspots for Reported Crimes')
plt.show()
