
from imap_tools import MailBox
import os
import re

student_id = ""
email_auth = ""

def remove_char(name: str):
    return re.sub(r"[，。（）/: ！]", "_", name)

with MailBox('imap.mail.nankai.edu.cn').login(f'{student_id}@mail.nankai.edu.cn', f'{email_auth}', 'INBOX') as mailbox:
    for message in mailbox.fetch(charset="utf-8"):
        print(message.subject)
        for att in message.attachments:  # list: [Attachment objects]
            if bool(att.filename):
                if not os.path.exists("data"):
                    os.mkdir("data")
                # 注意不能有特殊字符(如:, !, ?之类)
                with open(f"data/{remove_char(att.filename)}", "wb") as fp:
                    fp.write(att.payload)