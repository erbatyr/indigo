import pandas as pd
import sqlite3

a = pd.read_json('data.json')

con = sqlite3.connect("C:\\Users\erbatyr\\Desktop\\indigo\\indigo\\db.sqlite3")


a.to_sql('table_company',con=con, index=False, if_exists='append')


