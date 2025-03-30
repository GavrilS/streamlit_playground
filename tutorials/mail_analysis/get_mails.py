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
LOADED_MAILS = []

def stateful_button(*args, key=None, **kwargs):
    if key is None:
        raise ValueError('Must pass key')
    
    if key not in st.session_state:
        st.session_state[key] = False
    
    if st.button(*args, **kwargs):
        st.session_state[key] = not st.session_state[key]

    return st.session_state[key]


def get_mails(mail_count=10):
    mailbox = poplib.POP3_SSL(CREDS.get('server', ''), CREDS.get('port', ''))
    mailbox.user(CREDS.get('user', ''))
    mailbox.pass_(CREDS.get('password', ''))
    for i in range(len(LOADED_MAILS), mail_count):
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

        LOADED_MAILS.append(message_attributes)

    mailbox.quit()


def main():
    load_creds()
    get_mails()

    count = 0
    for msg in LOADED_MAILS:
        print('='*100)
        count += 1
        print(f"Message {count}: ", msg)
        st.write(msg)


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