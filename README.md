# VARS - Modern Day Email Tracking

## Introduction
VARS is a webapp that automates the process of sending emails and subsequent follow ups, untill a reply is received, for you. It does so by tracking the email sent, and updates you on the status of your email (not seen/seen/replied). You have the option of customizing your first email sent, and the rest of the process is taken care of by VARS :)

## Screenshots and Examples
You can find below a few attached screenshots of the working of the webapp. You can see the layouts of the various screens  

Dashboard  
![Image of Dashboard](https://github.com/0sidharth/mail-tracker/blob/master/dashboard_full.png)

Dashboard Condensed  
![Image of Dashboard_2](https://github.com/0sidharth/mail-tracker/blob/master/dashboard_condensed.png)

Form to fill up details of Professors  
![Image of login](https://github.com/0sidharth/mail-tracker/blob/master/login.jpg)

Database with details of Professors  
![Image of Database](https://github.com/0sidharth/mail-tracker/blob/master/db.jpg)

Form to fill up details of Professors  
![Image of Form](https://github.com/0sidharth/mail-tracker/blob/master/first_email.png)

## How to use?
Firstly, clone the repository.  
` $ git clone git@github.com:0sidharth/mail-tracker.git `  

Currently we haven't hosted it on a server, so you will have to run the webapp on your localhost. You can do this by  
` $ python Backend/mailtracker/manage.py runserver 8000 `  

Now the server will be up and running on your localhost `127.0.0.1:8000/mailer/index`  

Using the webapp itself is really simple. Firstly you can see the dashboard which will show you stats related to the mails you have sent and recent notification.  

You can navigate to First Email Details tab to fill up a new entry of a professor you want to email. Once you have entered all the details, just click submit and the professor will be added to the Database, accessible by the Database tab. Here, you can see the current status of all the professors you are tracking. You can remove any professor you want to from here by a simple click of a button.  

The update button on the top of the database tab is what handles the sending of emails for you. It will read from the database when the last email was sent, and if it is over 3 days without a reply, a followup will be sent. Or if it is the first time, the first email will be sent. You only need to press update once a day after the details are added, and it will take care of everything for you.  

The video below demonstrates the usage of the app!  
https://drive.google.com/drive/u/1/folders/1CAs000kVq8OaFA4LVWTJ4xv18z5m1OpJ  

## Motive
Our main inspiration was to make something that we ourselves will be able to use and can also be modified easily to cater to anyone else’s requirements.  
Apping (short for applying to universities externally) is a tedious process of mailing HR managers or professors to secure internships or jobs. It requires a lot of patience and perseverance to mail them everyday, keep track of replies, giving them reminders, etc.  
So the main aim was to automate this task through a webapp which can keep track of everything with just one click.  

## About Us
We are a team of 4 sophomore from IIT Bombay:
* Vikram Atreya - [vikram-atreya](https://github.com/vikram-atreya)
* Aaron Jerry Ninan - [aaroncodebro](https://github.com/aaroncodebro)
* Richeek Das - [sudoRicheek](https://github.com/sudoRicheek)
* Sidharth Mundhra - [0sidharth](https://github.com/0sidharth)
