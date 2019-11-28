import smtplib, ssl, random

def lottery():
    
    x = 0
    emails = ('email1@gmail.com', 'email2@gmail.com')
    personal_data = {
        'email1@gmail.com': ('Ariel', 'Semik'), 
        'email2@gmail.com': ('Patrick', 'Harrison')
        }

    ###### Lottery of couple
    while x == 0:
        x = 1
        lotter = list(emails)
        random.shuffle(lotter)
        couple = {}
        for y in range(len(lotter)):
            l = lotter[y]
            n = emails[y]
            if l == n:
                x = 0
                break
            couple[l] = n
            

    ###### Connect to Gmaila
    port = 465  # For SSL
    smtp_server = "smtp.gmail.com"
    sender_email = "email@gmail.com"  # Enter your address
    password = "****"  # Enter your password
    

    ###### Send enmail to each person
    for x in couple:
        
        ##### Chose person
        receiver_email = couple.get(x)
        who = couple[receiver_email]
        name = personal_data[who][0]
        surname = personal_data[who][1]
        print(receiver_email)
        subj = "Bedziesz Mikolajem dla {}".format(who)
        text = "Gratulacje. Losowanie przebieglo pomyslnie. W te Swieta bedziesz Mikolajem dla {} - {} {}. \nWesolych Swiat i przyjemnych zakupow".format(who, name, surname)
        message = "Subject: {}\n\n{}".format(subj, text)
        print(message)

        ##### Send email        
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, message)
        

    
    print("Emails sent")

lottery()
