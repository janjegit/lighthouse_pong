import sys
import os.path

def getText(st):
    res = ""
    inPar = False
    i = 0
    while i<len(st):
        if not inPar and st[i] == '\"':
            inPar = True
        elif inPar and st[i] == '\"':
            inPar = False
        elif inPar:
            res = res + st[i]
        i = i+1
    return res

# Get login credentials from 'cred.txt' file
def loginCreds(path = ""):
    if path == "":
        pass
    else:
        if not os.path.exists(path):
            print("ERROR. Credentials file '{}' not found.".format(path))
            exit()
        else:
            f = open(path).read().split('\n')
            username= getText(f[0])
            token= getText(f[1])

    return (username, token)

username, token = loginCreds("cred.txt")
