regn_no = input("Enter Register Number: ")
studentID = input("Enter Student ID: ")
emailID = input("Enter email ID : ")
password = input("Enter password : ")
referral_code = input("Enter referral code : ")

last_three_digits = int(regn_no[len(regn_no) - 3:])

if last_three_digits % 2 == 0:

    if len(password) >= 8 and password[0] >= 'A' and password[0] <= 'Z' and (password.count('0') + password.count('1') + password.count('2') +password.count('3') + password.count('4') + password.count('5') +password.count('6') + password.count('7') + password.count('8') +password.count('9')) >= 1:

        if len(studentID) == 7 and studentID[0:3] == "CSE" and studentID[3] == '-' and studentID[4].isdigit() and studentID[5].isdigit() and studentID[6].isdigit():

            if emailID.count('@') == 1 and emailID.count('.') >= 1 and emailID[0] != '@' and emailID[len(emailID) - 1] != '@' and emailID[len(emailID) - 4:len(emailID)] == ".edu":

                if len(referral_code) == 6 and referral_code[0:3] == "REF" and referral_code[3].isdigit() and referral_code[4].isdigit() and referral_code[5] == '@':

                    print("APPROVED")

                else:
                    print("REJECTED")

            else:
                print("REJECTED")

        else:
            print("REJECTED")

    else:
        print("REJECTED")

else:

    if len(studentID) == 7 and studentID[0:3] == "CSE" and studentID[3] == '-' and studentID[4].isdigit() and studentID[5].isdigit() and studentID[6].isdigit():

        if emailID.count('@') == 1 and emailID.count('.') >= 1 and emailID[0] != '@' and emailID[len(emailID) - 1] != '@' and emailID[len(emailID) - 4:len(emailID)] == ".edu":

            if len(password) >= 8 and password[0] >= 'A' and password[0] <= 'Z' and (password.count('0') + password.count('1') + password.count('2') + password.count('3') + password.count('4') + password.count('5') + password.count('6') + password.count('7') + password.count('8') +password.count('9')) >= 1:

                if len(referral_code) == 6 and referral_code[0:3] == "REF" and referral_code[3].isdigit() and referral_code[4].isdigit() and referral_code[5] == '@':

                    print("APPROVED")

                else:
                    print("REJECTED")
            else:
                print("REJECTED")
        else:
            print("REJECTED")
    else:
        print("REJECTED")
