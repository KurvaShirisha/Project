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

#Crime Code Analysis:
#What is the distribution of reported crimes based on Crime Code?

query = "SELECT `Crm_Cd`, COUNT(*) as CrimeCount FROM crime_data WHERE `Crm_Cd` IS NOT NULL GROUP BY `Crm_Cd` ORDER BY CrimeCount DESC LIMIT 10"
cursor.execute(query)
result = cursor.fetchall()

# Extract crime codes and crime counts
Crm_Cd = [row[0] for row in result]
crime_counts = [row[1] for row in result]

# Close the connection
connection.close()

# Plot a bar chart to show the distribution of reported crimes based on Crime Code
plt.bar(Crm_Cd, crime_counts)
plt.xlabel('Crime Code')
plt.ylabel('Number of Crimes')
plt.title('Distribution of Reported Crimes Based on Crime Code')
plt.show()