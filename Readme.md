# Attendance Manager
##### Attendance Manager is a simple Python-powered application which helps teachers in managing online lecture attendance in a easier way.

##### This Software works for this [ Chrome Extension](https://chrome.google.com/webstore/detail/google-meet-attendance-co/hjjeaaibilndjeabckakaknlcbblcmbc)

## Features

- Generate Present and Absent list
- Easy to use GUI
- Send mail to absent students with one click
- Easy to maintain Attendance Register
- Dark mode for nerds
- Easy Keybinds


## Tech

Attendance Manager uses a number of Python Modules to work properly:

- [Python](https://www.python.org/) - For Backend
- [Tkinter](https://docs.python.org/3/library/tkinter.html) - For GUI
- [smtplib](https://docs.python.org/3/library/smtplib.html) - For Email
- [Sqlite3](https://docs.python.org/3/library/sqlite3.html) - For Database Management
- [Pandas](https://pypi.org/project/pandas/) - For Data Management

Attendance Manager is a open source project with a [Public Repository](https://github.com/PVPPBoolean/Attendance-Manager)
 on GitHub.
 
 ## Installation
 
 Attendance Manager requires [Python](https://www.python.org/) 3.9+ to run
 
#### Clone the Repository from github.
 ```sh
git clone https://github.com/PVPPBoolean/Attendance-Manager.git
```

#### Install all the requirements.
 ```sh
pip install -r requirements.txt
```

#### Fill your details in config.py file as shown below
 ```sh
EMAIL_ADDRESS = "Example@gmail.com" 
PASSWORD = "Example_Password"
```

#### Edit Register.csv file for maintaining records
> Note: File name and format should be strictly same
> Add Student's names under the Name column

##### Example

| Name |
| ----- |
| Example_Name1 |
| Example_Name2 |
| Example_Name3 |

#### Create a *.xls file to crate database as per your need
> Note: Format should be strictly same

##### Example

| name | email | ID_num |
| ----- | ----- | ---- |
| Example_Name1 | Example_email1 | Example_id_num1 |
| Example_Name2 | Example_email2 | Example_id_num2 |
| Example_Name3 | Example_email3 | Example_id_num3 |

#### Now run ATTM.pyw

- Click on settings menu and click Edit Database
- File dialog will open and upload the *.xls file

```diff 
 Now you can start using Attendance Manager
```
