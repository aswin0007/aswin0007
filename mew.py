import mysql.connector

def insert_data(db_config, data):
    try:
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor()

        insert_query = """
            INSERT INTO your_table_name (Name, CurrentDesignation, Location, Experience, Skills)
            VALUES (%s, %s, %s, %s, %s)
        """

        cursor.execute(insert_query, data)
        connection.commit()
        print("Data inserted successfully.")

    except mysql.connector.Error as error:
        print(f"Error: {error}")
        connection.rollback()

    # finally:
    #     cursor.close()
    #     connection.close()