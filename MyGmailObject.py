import gmail
class MyGmailObject():

    def __init__(self, gmail_username, gmail_password , gmail_access_token):
        #authenticate and login
        gmail.authenticate(gmail_username, gmail_access_token)
        self.mailObject = gmail.login(gmail_username,gmail_password)


    def get_latest_email(self):
        allMessages = self.mailObject.inbox().mail()
        allMessages[len(allMessages)-1].fetch()
        return allMessages[len(allMessages)-1]

    def get_latest_sender(self):
        latestMessage = self.get_latest_email()
        return latestMessage.fr

    def get_latest_subject(self):
        latestMessage = self.get_latest_email()
        return latestMessage.subject

    def get_latest_body(self):
        latestMessage = self.get_latest_email()
        return latestMessage.body

    def get_num_unread_messages(self):
        allMessages = self.mailObject.inbox().mail(unread = True)
        return len(allMessages)

    def close_my_mail(self):
        self.mailObject.logout()

