"""
This is a simple script to retrieve emails with POP3 and use streamlit to display a report of 
retrieved messages/senders/date_received. To connect we need to have a file called 'creds.txt'
in the same directory populated for the example with the following lines:
pop_server=<server>
pop_port=<port>
username=<user@mail>
password=<user_password>

Usage:
streamlit run get_mails.py
python3 get_mails.py
"""

import poplib
import streamlit as st

CREDS = {}
MAX_MSG_ATTRIBUTES_COUNT = 4

def save_email(msg):
    print('Saving message ', msg.get('subject', 'Empty subject'))


def main():
    load_creds()
    print('Loaded creds: ', CREDS)
    print('^'*100)
    mailbox = poplib.POP3_SSL(CREDS.get('server', ''), CREDS.get('port', ''))
    mailbox.user(CREDS.get('user', ''))
    mailbox.pass_(CREDS.get('password', ''))
    messages = []
    for i in range(10):
        print('Message number: ', i+1)
        message_attributes = {}
        attributes_found = 0
        for msg in mailbox.retr(i+1)[1]:
            if b'Date: ' in msg:
                message_attributes['date'] = msg.decode('utf-8')
                attributes_found += 1
            elif b'To: ' in msg:
                message_attributes['receivers'] = msg.decode('utf-8')
                attributes_found += 1
            elif b'Subject: ' in msg:
                message_attributes['subject'] = msg.decode('utf-8')
                attributes_found += 1
            elif b'From: ' in msg:
                message_attributes['sender'] = msg.decode('utf-8')
                attributes_found += 1

            # print(msg)
            # print('='*100)
            if attributes_found == MAX_MSG_ATTRIBUTES_COUNT:
                break

        messages.append(message_attributes)

    count = 0
    for msg in messages:
        print('='*100)
        count += 1
        print(f"Message {count}: ", msg)
        st.write(msg)
        btn = st.button('Save email', key=count, on_click=save_email(msg))
    
    mailbox.quit()

def load_creds(filepath='creds.txt'):
    with open(filepath, 'r') as f:
        creds = f.readlines()

    # print(creds)
    for item in creds:
        if 'pop_server' in item:
            CREDS['server'] = item.split('=')[1].replace('\n', '')
        elif 'pop_port' in item:
            CREDS['port'] = item.split('=')[1].replace('\n', '')
        elif 'username' in item:
            CREDS['user'] = item.split('=')[1].replace('\n', '')
        elif 'password' in item:
            CREDS['password'] = item.split('=')[1].replace('\n', '')


main()