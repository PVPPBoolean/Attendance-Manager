import sqlite3
import pandas as pd
from tkinter import filedialog


def xls_to_sql():
        filename=filedialog.askopenfilename(filetypes=[('Excel Files', '*.xls'),('All Files', '*.*')])
        con=sqlite3.connect('Students'+".db") 
        wb=pd.ExcelFile(filename)
        for sheet in wb.sheet_names:
                df=pd.read_excel(filename)
                df.to_sql('Students',con, index=False,if_exists="replace")
        con.commit()
        con.close()

if __name__ == '__main__':
        xls_to_sql()