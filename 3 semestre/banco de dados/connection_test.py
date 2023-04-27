# Importing module
import mysql.connector

# Creating connection object
test2 = mysql.connector.connect(
	host = "localhost",
	user = "leao",
	password = "************"
)

# Printing the connection object
print(test2)
