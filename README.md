## Overview

A centralised attendance management web application, where teaching faculty can take attendance and student can view their attendance in real-time.

Every user has its own pair of userId and password with access controls associated with it.

HOD controls includes the full access to the data, with the rights to create, update and delete the attendance data.
Faculty controls include the rights to access and take attendance of the group which it belongs to.
Student controls include the rights to view respective attendance and percentage of presence and absence to lectures and practicals.

## Quick look

You can visit the following website to see the webapplication running.

*https://attendancewebapp.pythonanywhere.com/*




Required credentials: 

    1. HOD: 
          attID: 0, Password: 1234

    2. Faculty:
          attId: 1, Password: 12345
    
    3. Student: 
          attId: 2, Password: 123456
## Glimpse of UI


![Untitled design](https://github.com/anodicpassion/attendance_webapp/assets/117884284/d59cd48a-0311-4d66-acf8-7f1443987d6e)
![Untitled design1](https://github.com/anodicpassion/attendance_webapp/assets/117884284/811c67be-1f47-4fef-aaca-e638d103fc46)

## Installation

1. Install python3
2. Use the following commands to install all the dependencies:

   ```pip install requirements.txt``` 
## Usage 

1. Get into your project directory:
   ```cd to/your/project/dir```
2. Run the *main.py* python script:
   ```python3 main.py```
3. Open the link in browser:
   ```http://127.0.0.1:5500```
