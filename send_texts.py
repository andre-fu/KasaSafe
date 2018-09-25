from twilio.rest import Client
class send_texts:
    
    def __init__(self, destNumber, emergContact = None):
        self.accountSID = 'ACf33e1ad1e9fef28b8bfb8d138b3c481c'
        self.accounTOKEN = 'fff365c67321a41d9b15a3f5dcf3468f'

        self.tw = Client(self.accountSID, self.accounTOKEN)
        self.twNumber = '+12898143339'
        self.destNumber = str(destNumber)
        self.emergContact = str(emergContact)


    def send_text(self):
        message = self.tw.messages.create(
            body = 'Hey! You seem a bit drowsy, Please wake up!', 
            from_ = self.twNumber, 
            to = self.destNumber
        )
        message = self.tw.messages.create(
            body = 'You are the emergery contact of ' + self.destNumber + ' Please make sure they drive safe !', 
            from_ = self.twNumber, 
            to = self.emergContact
        )

        



