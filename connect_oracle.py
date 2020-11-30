import cx_Oracle
import pandas as pd
"""
Some quick start guides:
* cx_Oracle 8: https://cx-oracle.readthedocs.io/en/latest/user_guide/installation.html
* pandas: https://pandas.pydata.org/pandas-docs/stable/user_guide/10min.html
"""
# TODO change path of Oracle Instant Client to yours
cx_Oracle.init_oracle_client(lib_dir = "./instantclient_19_9")

# TODO change credentials
# Connect as user "user" with password "mypass" to the "CSC423" service
# running on lawtech.law.miami.edu
connection = cx_Oracle.connect(
    "jastcsc423", "jack1ethan", "lawtech.law.miami.edu/CSC_423")
cursor = connection.cursor()
cursor.execute("""
    SELECT * FROM STAFF 
    WHERE SEX = 'M'
    """)

# get column names from cursor
columns = [c[0] for c in cursor.description]
# fetch data
data = cursor.fetchall()
# bring data into a pandas dataframe for easy data transformation
df = pd.DataFrame(data, columns = columns)
print(df) # examine
print(df.columns)

cursor.execute("""
    SELECT * FROM HIRE_AGREEMENT ORDER BY period_start DESC
    """)
# get column names from cursor
columns = [c[0] for c in cursor.description]
# fetch data
data = cursor.fetchall()
# bring data into a pandas dataframe for easy data transformation
df = pd.DataFrame(data, columns = columns)
print(df) # examine
print(df.columns)

cursor.execute("""
    SELECT VEHICLES.registration_number, VEHICLES.current_milage, OUTLETS.address FROM VEHICLES 
    INNER JOIN OUTLETS ON OUTLETS.location_number = VEHICLES.location_number
    """)
# get column names from cursor
columns = [c[0] for c in cursor.description]
# fetch data
data = cursor.fetchall()
# bring data into a pandas dataframe for easy data transformation
df = pd.DataFrame(data, columns = columns)
print(df) # examine
print(df.columns)

cursor.execute("""
    SELECT STAFF.first_name, STAFF.last_name, OUTLETS.location_number 
    FROM STAFF INNER JOIN OUTLETS ON OUTLETS.location_number = STAFF.location_number
    """)
# get column names from cursor
columns = [c[0] for c in cursor.description]
# fetch data
data = cursor.fetchall()
# bring data into a pandas dataframe for easy data transformation
df = pd.DataFrame(data, columns = columns)
print(df) # examine
print(df.columns)


cursor.execute("""
    
SELECT VEHICLES.model, VEHICLES.make FROM VEHICLES WHERE current_milage > 100
    """)
# get column names from cursor
columns = [c[0] for c in cursor.description]
# fetch data
data = cursor.fetchall()
# bring data into a pandas dataframe for easy data transformation
df = pd.DataFrame(data, columns = columns)
print(df) # examine
print(df.columns)
