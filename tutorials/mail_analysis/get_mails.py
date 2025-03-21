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


def main():
    load_creds()
    print('Loaded creds: ', CREDS)
    print('^'*100)
    mailbox = poplib.POP3_SSL(CREDS.get('server', ''), CREDS.get('port', ''))
    mailbox.user(CREDS.get('user', ''))
    mailbox.pass_(CREDS.get('password', ''))
    for i in range(10):
        print('Message number: ', i+1)
        for msg in mailbox.retr(i+1)[1]:
            print(msg)
            print('='*100)

        print('End of messages\n', '*'*100)
    
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


if __name__=='__main__':
    main()