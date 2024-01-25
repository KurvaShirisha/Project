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

# Is there a significant difference in crime rates between male and female victims?


query = "SELECT `Vict_Sex`, COUNT(*) as CrimeCount FROM crime_data WHERE `Vict_Sex` IS NOT NULL GROUP BY Vict_Sex"
cursor.execute(query)
result = cursor.fetchall()

# Extract crime counts for each gender
gender_labels = [row[0] for row in result]
crime_counts = [row[1] for row in result]

# Close the connection
connection.close()

# Plot a bar chart to compare crime rates between genders
plt.bar(gender_labels, crime_counts)
plt.xlabel('Victim Sex')
plt.ylabel('Number of Crimes')
plt.title('Crime Rates Between Male and Female Victims')
plt.show()

