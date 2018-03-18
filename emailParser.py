# =C3=A8 e grave
# =C3-A9 e accute
# =C3=B4 o circumflex

# signatories spreadsheet
# name;role;country;email;country;mailing list;comment;time;ip;(contact form); time processed by program

# email format
# name;email;country;role;I sign; mailing list;comment;time;ip;)contact form); time processed by program

# mailchimp format
# email, firstname, lastname, role, country, ...

import csv
import os
import datetime
import codecs

stringEnd = ">"

nameVar = "*Name:* "
roleVar = "*Role/Title as Mental Health Worker:* "
countryVar = "> *Country:* "
emailVar = "> *Email:* "
#no space at the end
isignVar = "> *I sign the Mental Health Workers' Pledge:*"
#No space at the end
mailinglistVar = "> *Please add me to the USA/UK PalMHN mailing list :*"
mailinglistVar2 = "> *Please add me to the UKPalMHN mailing list :*"
#no space at end
commentVar = "> *Comment:*"
timeVar = "> Time: "
ipVar = "> IP Address: "

nameVarFR = "*Nom (exig=C3=A9) ::* "
roleVarFR = "*R=C3=B4le/qualit=C3=A9 en tant que professionnel de la sant=C3=A9 mental=e (exig=C3=A9) ::*> "
countryVarFR = "> *Pays (exig=C3=A9) ::* "
emailVarFR = "> *E-mail (exig=C3=A9) ::* "
#No space at the end
isignVarFR = "> sant=C3=A9/Palestine/Royaume-Uni):*"
#No space at the end
mailinglistVarFR = "> *Merci de m=E2=80=99ajouter =C3=A0 la liste de diffusion UKPalMHN (Profes=sionnels de la> sant=C3=A9/Palestine/Royaume-Uni):*"
#No space at the end
commentVarFR = "> *Commentaire::*"
timeVarFR = "> Time: "
ipVarFR = "> IP Address: "

path = '/Users/graham/PycharmProjects/emailParser/inputfiles/'
files = os.listdir(path)

for file in files:
    name = " "
    role = " "
    country = " "
    email = " "
    isign = " "
    mailinglist = " "
    comment = " "
    time = " "
    ip = " "
    processed = " "

    fh = open(os.path.join(path, file),errors='replace').read()
    fh = fh.replace("\n", "")
    mycsv = csv.writer(open('SignatoriesOutpup.csv', 'a'))
    if fh.rfind(nameVarFR) > 1:
        name = ((fh.split(nameVarFR))[1].split(stringEnd)[0])
        print(name)
        role = ((fh.split(roleVarFR))[1].split(stringEnd)[0])
        print(role)
        country = ((fh.split(countryVarFR))[1].split(stringEnd)[0])
        print(country)
        email = ((fh.split(emailVarFR))[1].split(stringEnd)[0])
        print(email)
        isign = ((fh.split(isignVarFR))[1].split(stringEnd)[0])
        print(isign)
        mailinglist = ((fh.split(mailinglistVarFR))[1].split(stringEnd)[0])
        print(mailinglist)
        comment = ((fh.split(commentVarFR))[1].split(stringEnd)[0])
        print(comment)
        time = ((fh.split(timeVarFR))[1].split(stringEnd)[0])
        print(time)
        ip = ((fh.split(ipVarFR))[1].split(stringEnd)[0])
        print(ip)
        processed = datetime.date.today()
        mycsv.writerow([name, role, country, email, country, isign, mailinglist, comment, time, ip, processed])
    elif fh.rfind(nameVar) > 1:
        name = ((fh.split(nameVar))[1].split(stringEnd)[0])
        print(name)
        role = ((fh.split(roleVar))[1].split(stringEnd)[0])
        print(role)
        country = ((fh.split(countryVar))[1].split(stringEnd)[0])
        print(country)
        email = ((fh.split(emailVar))[1].split(stringEnd)[0])
        print(email)
        isign = ((fh.split(isignVar))[1].split(stringEnd)[0])
        print(isign)
        if fh.rfind(mailinglistVar) > 1:
            mailinglist = ((fh.split(mailinglistVar))[1].split(stringEnd)[0])
        elif fh.rfind(mailinglistVar2) > 1:
            mailinglist = ((fh.split(mailinglistVar2))[1].split(stringEnd)[0])
        print(mailinglist)
        comment = ((fh.split(commentVar))[1].split(stringEnd)[0])
        print(comment)
        time = ((fh.split(timeVar))[1].split(stringEnd)[0])
        print(time)
        ip = ((fh.split(ipVar))[1].split(stringEnd)[0])
        print(ip)
        processed = datetime.date.today()
        mycsv.writerow([name, role, country, email, country, isign, mailinglist, comment, time, ip, processed])