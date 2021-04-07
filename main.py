from sendmail import SendMail

send = SendMail()

to = ''
sub = ''
text = ''
html = ''
#mail controller xxx@gmail.com
def mail_isvalid(self,mail_to):
    regex = '^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$'
    if(re.search(regex, mail)):
        return True
    else:
        print('wrong char mail')
        return False

send.sendmail(to,sub,text,html)