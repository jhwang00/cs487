from tkinter import *
from tkcalendar import *
import psycopg2
import datetime
import calendar

connection = {
  "dbname": "postgres",
  "user": "postgres",
  "password": "postgres",
  "port": 5432
}

try:
  conn = psycopg2.connect(**connection)
except:
  print(f"I am unable to connect to the database with connection parameters:\n{connection}")
  exit(1)

cur = conn.cursor()

def calendar(): #아
  today_time = datetime.date.today()

  root = Tk()
  root.title("Calendar")
  root.geometry("600x400")

  cal = Calendar(root, selectmode="day", year=today_time.year, month=today_time.month, day=today_time.day)
  cal.pack(fill = "both", expand = True)

  root.mainloop()

def main():
  tk = Tk() # create root window
  label1 = Label(tk, text='e-mail').grid(row=0, column = 0) #text
  label2 = Label(tk, text='password').grid(row=1, column = 0) #text

  #if in db
  button = Button(tk, text='Login', command=calendar).grid(row=2, column = 0)
  #else

  #button.pack(padx=10, pady=10)#(padx=720, pady=360)
  id = Entry(tk)
  pw = Entry(tk)
  id.grid(row=0, column=1)
  pw.grid(row=1, column=1)

  

  tk.mainloop()

main()

cur.close()
conn.close()

#r = tk.Tk()
#r.title('Task flow')
#button = tk.Button(r, text='Stop', width=25, height = 5, command=r.destroy)
#button.pack()
#r.mainloop()