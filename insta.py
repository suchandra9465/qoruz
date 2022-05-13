import re

text1 = """The tiny one, with not so tiny dreams.
For shows: info@qoruz-influencers.com.
For brand / films: support@qoruz.com.
instagram.com/qoruz. Cheers!!""".lower()

text2 = """The tiny one, with not so tiny dreams.Follow me on instagram 
@qoruz_global. For shows: info@qoruz-influencers.com"""

regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')

def isValid(email):
    if re.fullmatch(regex, email):
        return True
    else:
        return False
    
def extract_emails_and_usernames(text):
    tokens = text.split()
    emails = []
    usernames = []
    for index,token in enumerate(tokens):
        # remove full-stop char at the end if exists
        if token[-1]==".":
            token = token[:-1]
        if isValid(token):
            emails.append(token)

        if token=="instagram":
            
            if tokens[index+1][0]=="@":
                usernames.append(tokens[index+1])
            elif tokens[index+2][0]=="@":
                usernames.append(tokens[index+2])
        if "instagram.com" in token:
            usernames.append(token)
    
    return {"instagram":usernames,"emails":emails}

print(extract_emails_and_usernames(text1))