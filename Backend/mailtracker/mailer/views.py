from __future__ import print_function

import pickle
import os.path
import base64

from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.utils import timezone

from .models import *

from email import encoders
from email.message import Message
from email.mime.audio import MIMEAudio
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://mail.google.com/']

@login_required(login_url='/accounts/login/')
def login_for_gmail(request):
    """Shows basic usage of the Gmail API.
    Lists the user's Gmail labels.
    """
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=8081)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    return render(request, 'mailer/index.html', {"user" : request.user})


def create_message(sender, to, subject, message_text):
    message = MIMEText(message_text)
    message['to'] = to
    message['from'] = sender
    message['subject'] = subject
    raw_message = base64.urlsafe_b64encode(message.as_string().encode("utf-8"))
    return {
        'raw': raw_message.decode("utf-8")
    }

def create_message_with_attachment(
    sender, to, subject, message_text, file):
    """Create a message for an email.

    Args:
    sender: Email address of the sender.
    to: Email address of the receiver.
    subject: The subject of the email message.
    message_text: The text of the email message.
    file: The path to the file to be attached.

    Returns:
    An object containing a base64url encoded email object.
    """
    message = MIMEMultipart()
    message['to'] = to
    message['from'] = sender
    message['subject'] = subject

    msg = MIMEText(message_text)
    message.attach(msg)

    content_type, encoding = mimetypes.guess_type(file)

    if content_type is None or encoding is not None:
        content_type = 'application/octet-stream'
    main_type, sub_type = content_type.split('/', 1)
    if main_type == 'text':
        fp = open(file, 'rb')
        msg = MIMEText(fp.read(), _subtype=sub_type)
        fp.close()
    elif main_type == 'image':
        fp = open(file, 'rb')
        msg = MIMEImage(fp.read(), _subtype=sub_type)
        fp.close()
    elif main_type == 'audio':
        fp = open(file, 'rb')
        msg = MIMEAudio(fp.read(), _subtype=sub_type)
        fp.close()
    else:
        fp = open(file, 'rb')
        msg = MIMEBase(main_type, sub_type)
        msg.set_payload(fp.read())
        fp.close()
    filename = os.path.basename(file)
    msg.add_header('Content-Disposition', 'attachment', filename=filename)
    message.attach(msg)

    return {'raw': base64.urlsafe_b64encode(message.as_string())}


def send_message(service, user_id, message):
    try:
        message = (service.users().messages().send(userId=user_id, body=message)
               .execute())
        print('Message Id: %s' % message['id'])
        return message
    except Exception as e:
        print('An error occurred: %s' % e)
        return None

@login_required(login_url='/accounts/login/')
def profile(request):
    return render(request, 'mailer/index.html', {"user" : request.user})


@login_required(login_url='/accounts/login/')
def database(request):
    all_profs = ProfessorModel.objects.all().order_by("name")
    context = { 'professor_list' : all_profs, "user" : request.user }
    return render(request, 'mailer/pages/database/database.html', context)

@login_required(login_url='/accounts/login/')
def sendmail(service, recv_email, subject, mes):
    verified_gmail_data = service.users().getProfile(userId="me")
    m = create_message(verified_gmail_data["emailAddress"], recv_email, subject, message)
    ### Take Email of receiver as input !
    send_m = send_message(service, "me", m)
    return send_m


@login_required(login_url='/accounts/login/')
def addprof(request):
    data = dict(request.GET)
    if request.method == 'GET':
        newprof = ProfessorModel(name=data["name"],
            emailid=data["email"],
            country=data["country"],
            interests=data["interests"],
            university=data["university"],
            userperson=request.user,
            email_body=data["email_body"],
            reminder_mail = data["reminder_mail"])
        newprof.save()
    context = { 'professor_list' : data }
    return render(request, 'pages/forms/first_email.html', context)


@login_required(login_url='/accounts/login/')
def deleteprof(request, prof_id):
    ProfessorModel.objects.filter(pk=prof_id).delete()


@login_required(login_url='/accounts/login/')
def get_profs(request):
    all_profs = ProfessorModel.objects.all().order_by("name")
    context = { 'professor_list' : all_profs}
    return render(request, 'pages/database/database.html', context)


@login_required(login_url='/accounts/login/')
def update_seen_reply_status(request):
    pass


@login_required(login_url='/accounts/login/')
def update_send_mail(request):
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=8081)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('gmail', 'v1', credentials=creds)
    verified_gmail_data = service.users().getProfile(userId="me")
    all_profs = ProfessorModel.objects.all()
    for prof in all_profs:
        latest_email = prof.emailmodel_set.latest('date_created')
        if latest_email is None:
            sendmail(service, prof.emailid, prof.email_subject, prof.email_body)
            continue
        if latest_email.seen == True:
            continue #Seen zoned lol
        else:
            if latest_email.since() > 3: ## more than 3 days then mail
                sendmail(service, prof.emailid, prof.reminder_subject, prof.reminder_mail)

