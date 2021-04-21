import subprocess
import sys

def installModule(package):
	subprocess.check_call([sys.executable, "-m", "pip", "install", package])

# Imports
# GUI Interface
import tkinter as tk
import tkinter.ttk as ttk
from tkinter import messagebox # Messagebox
from tkhtmlview import HTMLLabel
from tkinter import filedialog # Filedialog 
from  tkinter import END
from tkinter import scrolledtext


# import ntpaths
try:
	from PIL import ImageTk,Image
except Exception as e:
	res = tk.messagebox.askquestion("Module not found", "Pillow Module not found\nWould you like to install it? Please restart once done")
	print(e)
	if res == 'yes':
		installModule("Pillow")

try:
	from tkhtmlview import HTMLLabel
except Exception as e:
	res = tk.messagebox.askquestion("Module not found", "tkhtmlview Module not found\nWould you like to install it? Please restart once done")
	print(e)
	if res == 'yes':
		installModule("tkhtmlview")

# Database
import sqlite3

# For Sending mail
import smtplib 
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart

# Date Maniplulation
import re
try:
	import pandas as pd
except Exception:
	res = tk.messagebox.askquestion("Module not found", "Pandas Module not found\nWould you like to install it? Please restart once done")
	if res == 'yes':
		installModule("Pandas")

from datetime import datetime

# Login Credentials
import config

# import time as t
import os

# Data

keybinds = "Keybinds are  \n\nEscape	    --> To Exit the application\nCtrl + /	--> Will switch to Light Mode\nCtrl + \\	--> Will switch to Dark Mode"

frame_bg = "#9590A8"
frame_fg = "#000000"
main_label_fg = "#000000"
main_label_bg = "#9590A8"
button_fg = "#000000"
button_bg = "#E5FFDE"
listbox_bg = "#E5FFDE"
listbox_fg = "#000000"

temp_list = []
database_list = []
database_list1 = []
temp_present_list = []
temp_absent_list = []
present_list = []
absent_list = []
df_m = "Hello Student\n\nThis is reminder that you have missed one of your lectures\nDon't miss out on lectures\nThank You."

github_logo ='''<a href="https://github.com/pvppboolean">
		<img src="img/github2.png" width=30 height=20>
		</img>
		</a>
	'''

gmail_logo ='''<a href="https://mail.google.com/mail/?view=cm&fs=1&to=pvppgrpboolean@gmail.com&
		su=Query or Feedback regarding Attendance Manager&body=BODY">
		<img src="img/gmail.png" width=30 height=20>
		</img>
		</a>
	'''

# Functions
def ctrl_backslash(event):
	dark_mode(1)
	mode.set(1)

def ctrl_slash(event):
	dark_mode(0)
	mode.set(0)


def shortcuts(event):
	keyPressed = event.char
	if keyPressed == '\x1b':
		close_button.config(text = "Quitting...")
		MsgBox = tk.messagebox.askquestion ('Exit Application','Are you sure you want to exit the application',icon = 'warning')
		if MsgBox == 'yes':
			present_list.clear()
			absent_list.clear()
			database_list.clear()
			database_list1.clear()
			root.destroy()
		elif MsgBox == 'no':
			close_button.config(text = "Quit")


# def path_leaf(path):
# 	try:
# 		head, tail = ntpath.split(path)
# 		return tail or ntpath.basename(head)
# 	except:
# 		print("Error during finding path of file!")

def dark_mode(mode):
	if mode:
		frame_bg = "#121212"
		frame_fg = "#E5FFDE"
		main_label_fg = "#E5FFDE"
		main_label_bg = "#121212"
		button_fg = "#000000"
		button_bg = "#bbcbcb"
		listbox_bg = "#121212"
		listbox_fg = "#E5FFDE"

		for frame in (keybind_frame, social_frame, home_frame, present_frame, register_frame, absent_frame, email_frame, default_frame):
			frame.config(bg=frame_bg, fg=frame_fg)

		for frames in (absent_students_frame, present_students_frame):
			frames.config(bg = frame_bg)

		for menu in (settings_menu, social_menu, home_menu, main_menu):
			menu.config(bg=frame_bg, fg=frame_fg)

		for label in (binds_label, social_html_label2, social_html_label1, social_label1, social_label3, social_label5, social_label6, Default_label, email_label, Register_label, Absent_label, Present_label, welcome_label):
			label.config(bg=main_label_bg, fg=main_label_fg)

		for button in (send_button, save_button, update_button, register_button, home_button_k, home_button_p, home_button_so, home_button_a, home_button_d, home_button_r, home_button_e, close_button, mail_button, absent_button, present_button, upload_file_button):
			button.config(bg=button_bg, fg=button_fg)

		for listbox in (Present_student_listbox, Absent_student_listbox):
			listbox.config(bg=listbox_bg, fg=listbox_fg)

		for radio in (email_radio1, email_radio2):
			radio.config(bg=button_bg, fg=button_fg)


	elif mode == 0:
		frame_bg = "#9590A8"
		frame_fg = "#000000"
		main_label_fg = "#18020C"
		main_label_bg = "#9590A8"
		button_fg = "#000000"
		button_bg = "#E5FFDE"
		listbox_bg = "#9590A8"
		listbox_fg = "#000000"

		for frame in (keybind_frame, social_frame, home_frame, present_frame, register_frame, absent_frame, email_frame, default_frame):
			frame.config(bg=frame_bg, fg=frame_fg)

		for frames in (absent_students_frame, present_students_frame):
			frames.config(bg = frame_bg)

		for menu in (settings_menu, social_menu, home_menu, main_menu):
			menu.config(bg=frame_bg, fg=frame_fg)

		for label in (binds_label, social_label1, social_label6, social_label3, social_html_label1, social_html_label2, social_label5, Default_label, email_label, Register_label, Absent_label, Present_label, welcome_label):
			label.config(bg=main_label_bg, fg=main_label_fg)

		for button in (send_button, save_button, update_button, register_button, home_button_k, home_button_p, home_button_so, home_button_a, home_button_d, home_button_r, home_button_e, close_button, mail_button, absent_button, present_button, upload_file_button):
			button.config(bg=button_bg, fg=button_fg)

		for listbox in (Present_student_listbox, Absent_student_listbox):
			listbox.config(bg=listbox_bg, fg=listbox_fg)

		for radio in (email_radio1, email_radio2):
			radio.config(bg=button_bg, fg=button_fg)

def sel():
	if var.get() == 1:
		text_widget.delete("1.0", END)
		text_widget.insert(END, df_m)
		text_widget.config(state="disabled", fg="grey")
		# print("Default Message Selected")
	
	if var.get() == 2:
		text_widget.config(state="normal", fg="black")
		# print("Custom Message Selected")

	return

def raise_frame(frame):
	frame.tkraise()
	return

def intersection(lst1, lst2):
	lst3 = [value for value in lst1 if value in lst2]
	return lst3


def Diff(li1, li2):
	return list(set(li1) - set(li2))


def present_students():

	# connection to database
	conn = sqlite3.connect(os.path.abspath("Students.db"))
	c = conn.cursor()
	c.execute("SELECT * FROM Students")
	conn.commit()

	items = c.fetchall()

	for item in items:
		database_list.append(item[0])

	# present list genration
	global present_list
	present_list = Diff(database_list, Diff(database_list, temp_present_list))
	# print("\t\t\tPresent Students are: ")
	Present_student_listbox.delete(0,END)
	if len(present_list) == 0:
		Present_label = tk.Label(present_frame)
		Present_label.config(text="No Student was Present!", font=50)
		# Present_label.place(relx=0.044, rely=0.064, relwidth=0.913, relheight=0.06)
		Present_student_listbox.insert(END,"MassBunk")
		# print("No Student was Present!")
	else:
		Present_label = tk.Label(present_frame)
		Present_label.config(text ="Present Students are:", font=100)
		# Present_label.place(relx=0.044, rely=0.064, relwidth=0.913, relheight=0.06)
		i = 1
		for name in present_list:
			Present_student_listbox.insert(END,str(i)+" . "+name)
			# print(name)
			i+=1
		Present_student_listbox.insert(END, "Total number of present students: "+str(len(present_list)))
		# print("\n")
	return


def absent_students():

	# connection to database
	conn = sqlite3.connect(os.path.abspath("Students.db"))
	c = conn.cursor()
	c.execute("SELECT * FROM Students")
	conn.commit()

	items = c.fetchall()

	for item in items:
		database_list.append(item[0])

	# absent list generation
	global absent_list
	absent_list = Diff(database_list, temp_present_list)
	# print("\t\t\tAbsent Students are: ")
	Absent_student_listbox.delete(0,END)
	if len(absent_list) == 0:
		Absent_label = tk.Label(absent_frame)
		Absent_label.config(text ="All students are Present!", font=30)
		# Absent_label.place(relx=0.044, rely=0.064, relwidth=0.913, relheight=0.06)
		Absent_student_listbox.insert(END,"0 student absent")
		# print("No Student was Absent!")
	else:
		Absent_label = tk.Label(absent_frame)
		Absent_label.config(text ="Absent Students are:", font=30)
		# Absent_label.place(relx=0.044, rely=0.064, relwidth=0.913, relheight=0.06)
		i = 1
		for name in absent_list:
			Absent_student_listbox.insert(END,str(i)+" . "+name)
			# print(name)
			i+=1
		Absent_student_listbox.insert(END, "Total number of absent students: "+str(len(absent_list)))
		# print("\n")
	return

def send_feed():
	pass


def send_mail():
	try:
		send_button.config(text = "Mail Sent")
		# connection to mail server
		server = smtplib.SMTP('smtp.gmail.com:587')
		server.ehlo()
		server.starttls()
		server.login(config.EMAIL_ADDRESS, config.PASSWORD)

		# connection to Database
		conn = sqlite3.connect(os.path.abspath("Students.db"))
		c = conn.cursor()
		c.execute("SELECT * FROM Students")
		conn.commit()
		items = c.fetchall()

		for item in items:
			database_list.append(item[0])
		for item in items:
			database_list1.append((item[0], item[1]))

		absent_list = Diff(database_list, temp_present_list)

		for item in database_list1:
			if item[0] in absent_list:
				temp_absent_list.append(item)
		for item in temp_absent_list:
			
			# create msg
			msg = MIMEMultipart()
			msg['From'] = 'PVPPGRPBOOLEAN'
			msg['To'] = item[1]
			msg['subject'] = 'Attendance Report'
			# Message = message.create_msg(item[0], config.LECTURE_NAME, config.TEACHER_NAME)

			# Message = txtmessage()

			if var.get() == 1:
				Message = "Hello Student\n\nThis is reminder that you have missed one of your lectures\nDon't miss out on lectures\nThank You."
				# print("Selected")
			elif var.get() == 2:
				Message = text_widget.get("1.0", "end-1c")
			else: 
				# print("error in var get")
				Message = "ERROR wrong MAIL"
				continue

			msg.attach(MIMEText(Message, 'plain'))
			text = msg.as_string()
			# Sending Email
			server.sendmail(config.EMAIL_ADDRESS, item[1], text)
		
		tk.messagebox.showinfo ('Thank You','Mail has been sent',icon = 'info')

		# print('Mails Sent!!')

		text_widget.config(state="normal")
		text_widget.delete("1.0", END)

		# print("Thank You!")
		present_list.clear()
		absent_list.clear()
		database_list.clear()
		database_list1.clear()

		send_button.config(text = "Send")

		return
	except Exception as e:
		print(e)
		# print("Error during sending Email!! Please try again")
		send_button.config(text = "Send")
		tk.messagebox.showinfo ('Mailing Error','Error during Mailing! Try Again',icon = 'info')


def upload_file():
	try:
		upload_file_button.config(text = "Loading...")
		file_name = filedialog.askopenfilename(filetypes=[("Excel Files", "*.csv"), ("All Files", "*.*")])
		# name_type = path_leaf(file_name)
		file = open(file_name)
		file_data = file.read()

		temp_present_list.clear()
		temp_list.append(file_data.split("\n"))

		for items in temp_list:
			for item in items:
				temp_present_list.append(item)

		temp_list.clear()

		global date
		raw_date = (temp_present_list[0:4])[0]
		match = re.search(r'\d{4}-\d{2}-\d{2}', raw_date)
		date = (datetime.strptime(match.group(), '%Y-%m-%d').date()).strftime("%d-%b")
		
		# print(date)

		if temp_present_list[-1] == '':
			del temp_present_list[-1]

		file.close()
		upload_file_button.config(text = "Upload file")
		return
	except Exception as e:
		tk.messagebox.showinfo ('Upload Error','Error during file uploading file! Try Again',icon = 'info')
		upload_file_button.config(text = "Upload file")
		# print(e)

def save():
	df.to_csv('Register.csv', index = False)
	tk.messagebox.showinfo("OK", "OK")
	return

def update():
	present_students()
	global df
	try:
		df = pd.read_csv('Register.csv')
		df[date] = ["Absent" for _ in range(df.shape[0])]
	except NameError:
		tk.messagebox.showinfo("File not found", "Hence, showing the previous records", icon = "info")

	for student in present_list:
		df.loc[df["Name"] == student, date] = "Present"
	clear_treeview()
	Register_treeview["column"] = list(df.columns)
	Register_treeview["show"] = "headings"
	for column in Register_treeview["columns"]:
		Register_treeview.heading(column, text=column)
	df_rows = df.to_numpy().tolist()
	for row in df_rows:
		Register_treeview.insert("", "end", values=row)

def clear_treeview():
	Register_treeview.delete(*Register_treeview.get_children())

def quit_app():
	close_button.config(text = "Quitting...")
	MsgBox = tk.messagebox.askquestion ('Exit Application','Are you sure you want to exit the application',icon = 'warning')
	if MsgBox == 'yes':
		present_list.clear()
		absent_list.clear()
		database_list.clear()
		database_list1.clear()
		root.destroy()
	if MsgBox == 'no':
		close_button.config(text = "Quit")

#GUI Interface

# Root
root = tk.Tk()
root.geometry("480x550+500+100")
root.title("Attendance Manager")

photo = tk.PhotoImage(file = "img/Logo.png")
root.iconphoto(True, photo)
root.bind("<Escape>", shortcuts)
root.bind("<Control-slash>", shortcuts)
root.bind('<Control-slash>', ctrl_slash)      # forward-slash
root.bind('<Control-backslash>', ctrl_backslash)  # backslash

var=tk.IntVar()
mode=tk.IntVar()
var.set(1)
mode.set(0)

#Style
# style = ttk.Style(root).configure("Treeview", foreground="White", background="Black", fieldbackground="Black")
# style.theme_use('vista')

#style.map("C.TButton",
#    foreground=[('pressed', 'red'), ('active', 'blue')],
#    background=[('pressed', '!disabled', 'black'), ('active', 'white')]
#    )

# Canvas and Frames
Height= 560
Width= 448

canvas1 = tk.Canvas(root, height=Height, width=Width)
canvas1.pack()

home_frame = tk.LabelFrame(root, text="Home", bg=frame_bg, fg=frame_fg, bd=5)
home_frame.place(relx=0, rely=0, relwidth=1, relheight=1)

present_frame = tk.LabelFrame(root, text="Present Students", bg=frame_bg, fg=frame_fg, bd=5)
present_frame.place(relx=0, rely=0, relwidth=1, relheight=1)

absent_frame = tk.LabelFrame(root, text="Absent Students", bg=frame_bg, fg=frame_fg, bd=5)
absent_frame.place(relx=0, rely=0, relwidth=1, relheight=1)

email_frame = tk.LabelFrame(root, text="Email", bg=frame_bg, fg=frame_fg, bd=5)
email_frame.place(relx=0, rely=0, relwidth=1, relheight=1)

register_frame = tk.LabelFrame(root, text="Register_frame", bg=frame_bg, fg=frame_fg, bd=5)
register_frame.place(relx=0, rely=0, relwidth=1, relheight=1)

default_frame = tk.LabelFrame(root, text="Developers", bg=frame_bg, fg=frame_fg, bd=5)
default_frame.place(relx=0, rely=0, relwidth=1, relheight=1)

social_frame = tk.LabelFrame(root, text="Socials", bg=frame_bg, fg=frame_fg, bd=5)
social_frame.place(relx=0, rely=0, relwidth=1, relheight=1)

keybind_frame = tk.LabelFrame(root, text="Key Bind", bg=frame_bg, fg=frame_fg, bd=5)
keybind_frame.place(relx=0, rely=0, relwidth=1, relheight=1)

#Menu
main_menu = tk.Menu(root, background = "#202302")
root.config(menu = main_menu)

#homemenu
home_menu = tk.Menu(main_menu, tearoff= False, bg=frame_bg, fg=frame_fg)
main_menu.add_cascade(label='Home', menu = home_menu)
home_menu.add_command(label='Home', command =lambda:[raise_frame(home_frame)])
home_menu.add_command(label='Present Students', command =lambda:[present_students(), raise_frame(present_frame)])
home_menu.add_command(label='Absent Students', command =lambda:[absent_students(), raise_frame(absent_frame)])
home_menu.add_command(label='Register', command =lambda:[raise_frame(register_frame), update()])
home_menu.add_separator()
home_menu.add_command(label='Quit', command =quit_app)

#settings_menu
settings_menu =tk.Menu(main_menu, tearoff=False, bg=frame_bg, fg=frame_fg)
main_menu.add_cascade(label='Settings', menu = settings_menu)
settings_menu.add_radiobutton(label="Dark Mode", command=lambda:[dark_mode(mode.get())], variable=mode, value=1)
settings_menu.add_radiobutton(label="Light Mode", command=lambda:[dark_mode(mode.get())], variable=mode, value=0)

# Social menu
social_menu =tk.Menu(main_menu, tearoff=False, bg=frame_bg, fg=frame_fg)
main_menu.add_cascade(label='Social', menu = social_menu)
social_menu.add_command(label='Social', command = lambda:[raise_frame(social_frame)])
social_menu.add_command(label='Key Binds', command = lambda:[raise_frame(keybind_frame)])


#home_frame
welcome_label = tk.Label(home_frame, text ="Attendance Manager", font=("Helvetica", 20), fg=main_label_fg, bg=main_label_bg)
welcome_label.place(relx=0.2, rely=0.12, relwidth=0.6, relheight=0.3)
upload_file_button = tk.Button(home_frame, text="Upload File", command=upload_file, fg=button_fg, bg=button_bg)
upload_file_button.place(relx=0.275, rely=0.384, relwidth=0.45, relheight=0.05)
present_button = tk.Button(home_frame, text="Show Present Students", borderwidth=1, command=lambda:[present_students(), raise_frame(present_frame)], fg=button_fg, bg=button_bg)
present_button.place(relx=0.275, rely=0.448, relwidth=0.45, relheight=0.05)
absent_button = tk.Button(home_frame, text="Show Absent Students", command=lambda:[absent_students(), raise_frame(absent_frame)], fg=button_fg, bg=button_bg)
absent_button.place(relx=0.275, rely=0.514, relwidth=0.45, relheight=0.05)
mail_button = tk.Button(home_frame, text="E-Mail", command=lambda:[raise_frame(email_frame),var.set(1),sel()], fg=button_fg, bg=button_bg)
mail_button.place(relx=0.275, rely=0.58, relwidth=0.45, relheight=0.05)
register_button = tk.Button(home_frame, text="Register", command=lambda:[update(), raise_frame(register_frame)], fg=button_fg, bg=button_bg)
register_button.place(relx=0.275, rely=0.645, relwidth=0.45, relheight=0.05)
close_button = tk.Button(home_frame, text="Quit", command=quit_app, fg=button_fg, bg=button_bg)
close_button.place(relx=0.58, rely=0.75, relwidth=0.2, relheight=0.04)

#present_frame
Present_label = tk.Label(present_frame, text ="Present Students are", bg=main_label_bg, fg=main_label_fg, font=30)
Present_label.place(relx=0.044, rely=0.064, relwidth=0.913, relheight=0.06)
present_students_frame = tk.Frame(present_frame, bg=frame_bg, bd=1)
present_students_frame.place(relx=0.044, rely=0.15, relwidth=0.913, relheight=0.707)
v = tk.Scrollbar(present_students_frame, orient="vertical")
Present_student_listbox = tk.Listbox(present_students_frame, fg=listbox_fg, bg=main_label_bg, highlightcolor="Blue", bd="0", selectmode = "MULTIPLE", yscrollcommand=v.set)
Present_student_listbox.pack(side="left",fill="both", expand="yes", padx=5, pady=5)
v.config(command=Present_student_listbox.yview)
v.pack(side="right", fill="y")
home_button_p = tk.Button(present_frame, text="Home", command=lambda:[raise_frame(home_frame)], fg=button_fg, bg=button_bg)
home_button_p.place(relx=0.275, rely=0.88, relwidth=0.45, relheight=0.05)

#absent_frame
Absent_label = tk.Label(absent_frame, text ="Absent Students are:", fg=main_label_fg, bg=main_label_bg, font=30)
Absent_label.place(relx=0.044, rely=0.064, relwidth=0.913, relheight=0.06)
absent_students_frame = tk.Frame(absent_frame, bg=frame_bg, bd=5)
absent_students_frame.place(relx=0.044, rely=0.15, relwidth=0.913, relheight=0.707)
v = tk.Scrollbar(absent_students_frame, orient="vertical") 
Absent_student_listbox = tk.Listbox(absent_students_frame, fg=listbox_fg, bg=main_label_bg, highlightcolor="Blue", yscrollcommand=v.set)
Absent_student_listbox.pack(side="left",fill="both", expand="yes", padx=5, pady=5)
v.config(command=Absent_student_listbox.yview)
v.pack(side="right", fill="y")
home_button_a = tk.Button(absent_frame, text="Home", command=lambda:[raise_frame(home_frame)], fg=button_fg, bg=button_bg)
home_button_a.place(relx=0.275, rely=0.88, relwidth=0.45, relheight=0.05)

# email_frame
home_button_e = tk.Button(email_frame, text="Home", command=lambda:[raise_frame(home_frame)], fg=button_fg, bg=button_bg)
home_button_e.place(relx=0.275, rely=0.88, relwidth=0.45, relheight=0.05)
email_label = tk.Label(email_frame, text="Type the message below", font=("Helvetica", 16), fg=main_label_fg, bg=main_label_bg)
email_label.place(relx=0.28, rely=0.02)
email_back_frame = tk.Frame(email_frame, bg=frame_bg, bd=5)
email_back_frame.place(relx=0.044, rely=0.09, relheight=0.6, relwidth=0.91)
text_widget = tk.Text(email_back_frame,width=25, height=6, wrap = 'word', font=("Helvetica", 10))
text_widget.pack(side="left",fill="both", expand="yes")
s = tk.Scrollbar(email_back_frame, orient="vertical", command = text_widget.yview)
text_widget['yscroll'] = s.set
s.pack(side="right", fill="y")
email_radio1 = tk.Radiobutton(email_frame, text = "Default Message",variable=var, value=1, cursor="Dot", command=sel, fg=button_fg, bg=button_bg)
email_radio1.place(relx=0.23, rely=0.72)
email_radio2 = tk.Radiobutton(email_frame, text = "Custom Message",variable=var, value=2, cursor="Dot", command=sel, fg=button_fg, bg=button_bg)
email_radio2.place(relx=0.53, rely=0.72)
send_button = tk.Button(email_frame, text="Send", command=send_mail, fg=button_fg, bg=button_bg)
send_button.place(relx=0.275, rely=0.82, relwidth=0.45, relheight=0.05)

# Register_frame
Register_label = tk.Label(register_frame, text ="Attendance Register", fg=main_label_fg, bg=main_label_bg, font=30)
Register_label.place(relx=0.044, rely=0.064, relwidth=0.913, relheight=0.06)
register_box_frame = tk.Frame(register_frame, bg="white", bd=5)
register_box_frame.place(relx=0.044, rely=0.15, relheight=0.65, relwidth=0.91)
update_button = tk.Button(register_frame, text="Update", command=update, fg=button_fg, bg=button_bg)
update_button.place(relx=0.15, rely=0.83, relwidth=0.3, relheight=0.05)
save_button = tk.Button(register_frame, text="Save", command=save, fg=button_fg, bg=button_bg)
save_button.place(relx=0.55, rely=0.83, relwidth=0.3, relheight=0.05)
home_button_r = tk.Button(register_frame, text="Home", command=lambda:[raise_frame(home_frame)], fg=button_fg, bg=button_bg)
home_button_r.place(relx=0.275, rely=0.9, relwidth=0.45, relheight=0.05)
Register_treeview = ttk.Treeview(register_box_frame)
Register_treeview.place(relheight=1, relwidth=1)
treescrolly = tk.Scrollbar(register_box_frame, orient="vertical", command=Register_treeview.yview)
treescrollx = tk.Scrollbar(register_box_frame, orient="horizontal", command=Register_treeview.xview)
Register_treeview.config(xscrollcommand=treescrollx.set, yscrollcommand=treescrolly.set)
treescrollx.pack(side='bottom', fill="x")
treescrolly.pack(side='right', fill="y")

# Social Frame
social_label1 = tk.Label(social_frame, font=("Segoe UI", 16),
		fg=main_label_fg, bg=main_label_bg,
		text="For any queries\nor suggestions\n\nYou can connect with us at:"
	)
social_html_label1 = HTMLLabel(social_frame, html = github_logo, bg=main_label_bg, fg = main_label_fg)
social_html_label2 = HTMLLabel(social_frame, html = gmail_logo, bg=main_label_bg, fg = main_label_fg)
social_label3 = tk.Label(social_frame,font=("Segoe UI light", 12, 'underline'), fg=main_label_fg, bg=main_label_bg, text="Gmail")
social_label6 = tk.Label(social_frame,font=("Segoe UI light", 12, 'underline'), fg=main_label_fg, bg=main_label_bg, text="Github")
social_label5 = tk.Label(social_frame, font=("Segoe UI", 14),
		fg=main_label_fg, bg=main_label_bg,
		text="Your feedback is always welcome\n\nThank you for using our app"
	)
social_label1.place(relx=0.165, rely=0.05, relheight=0.35, relwidth=0.7)
social_label3.place(relx=0.34, rely=0.4, relheight=0.05, relwidth=0.1)
social_label6.place(relx=0.53, rely=0.4, relheight=0.05, relwidth=0.11)
social_html_label1.place(relx=0.55, rely=0.35, relheight=0.055, relwidth=0.08)
social_html_label2.place(relx=0.35, rely=0.35, relheight=0.055, relwidth=0.08)
social_label5.place(relx=0.05, rely=0.58, relheight=0.15, relwidth=0.88)
home_button_so = tk.Button(social_frame, text="Home", command=lambda:[raise_frame(home_frame)], fg=button_fg, bg=button_bg)
home_button_so.place(relx=0.275, rely=0.88, relwidth=0.45, relheight=0.05)

# Keybind Frame
binds_label = tk.Label(keybind_frame, font=("Segoe UI", 16),
		fg=main_label_fg, bg=main_label_bg,
		text=keybinds
	)
binds_label.place(relx=0.05, rely=0.1, relheight=0.35, relwidth=0.9)
home_button_k = tk.Button(keybind_frame, text="Home", command=lambda:[raise_frame(home_frame)], fg=button_fg, bg=button_bg)
home_button_k.place(relx=0.275, rely=0.88, relwidth=0.45, relheight=0.05)

#default_frame
Default_label = tk.Label(default_frame, text ="Work in Progress!!", fg=main_label_fg, bg=main_label_bg)
Default_label.place(relx=0.044, rely=0.064, relwidth=0.913, relheight=0.06)
home_button_d = tk.Button(default_frame, text="Home", command=lambda:[raise_frame(home_frame)], fg=button_fg, bg=button_bg)
home_button_d.place(relx=0.275, rely=0.88, relwidth=0.45, relheight=0.05)

# Mainloop
root.protocol("WM_DELETE_WINDOW", quit_app)

raise_frame(home_frame)
root.mainloop()
