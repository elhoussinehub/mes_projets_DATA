import csv
import sqlite3
from io import StringIO

def sql_to_csv(database, table_name):
    conn = sqlite3.connect(database)
    cur = conn.cursor()
    cur.execute(f"SELECT * FROM {table_name}")
    rows = cur.fetchall()
    rows = list(map(lambda t: list(map(str, t)), rows))
    rows = list(map(lambda t: ",".join(t), rows))
    rows = "\n".join(rows)
    header = ",".join([discription[0] for discription in cur.description]) + "\n"
    final = header + rows

    with open('list_fault_lines.csv', 'w', encoding="utf-8") as f:
        f.write(final)

    return  final

# print(sql_to_csv('all_fault_line.db','fault_lines'))

def csv_to_sql(csv_content, database, table_name):

    conn = sqlite3.connect(database)
    cur = conn.cursor()

    reader = csv.reader(csv_content)
    rows = list(reader)

    header = rows[0]
    data_rows = rows[1:]

    columns = ", ".join([f'"{col}" TEXT' for col in header])
    cur.execute(f"CREATE TABLE IF NOT EXISTS {table_name}({columns})")
    placeholders = ", ".join(["?"] * len(header))
    insert_q = f"INSERT INTO {table_name} VALUES ({placeholders})"

    for row in data_rows:
        cur.execute(insert_q, row)
        
    conn.commit()
    conn.close()

#csv_content = open("list_volcano.csv")
#csv_to_sql(csv_content, 'list_volcanos.db','volcanos')
