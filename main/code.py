import pyshorteners


print()
print("                                                Welcome to URL Shortner ")
url = input("Enter Your URL >> ")

def shortner(url):
    s = pyshorteners.Shortener()
    print(s.tinyurl.short(url))

ch = 'yes'
while ch == 'yes':
    print()
    shortner(url)

    ch = input("Do you want to shorten more URL (YES/NO) : ")
    if ch.lower() != 'yes':
        break