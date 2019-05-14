'''
This is a function that masks all but the last four characters of a string with "#".
'''
def mask():
    cc = list(str(input("Enter a password: ")))
    if len(cc) == 0:
        print("''")
    elif len(cc) <= 4:
        print(''.join(cc))
    else:
        new_cc = ''
        for elem in cc[0:-4]:
            elem = "#"
            new_cc += elem
        print(new_cc + "".join(cc[-4:]))

mask()