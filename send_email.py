import smtplib


email_list = []


email_id = input('Enter your email id: ')
password_log = input("Enter your password: ")
subject = input('Enter the subject of mail: ')
email_body = input('Enter the email body: ')


n = int(input('Enter no. of recipients: '))
for x in range(n):
    email_str = input('Recpient email %d : '%(x+1))
    email_list.append(email_str)


smtpObj = smtplib.SMTP_SSL('smtp.gmail.com',465)
smtpObj.ehlo()
smtpObj.login(email_id,password_log)
message_body = 'Subject:' +  subject + '\n' + email_body
smtpObj.sendmail(email_id ,email_list, message_body)