print('Program Validasi Email')
inputuser = input('masukan email: ')
def validitasemail(inputuser):
    inputuser = inputuser.replace('@', ' ')
    inputuser = inputuser.replace('.', ' ')
    inputuser_split = inputuser.split(' ')

    if len(inputuser_split) != 3: 
        print('EMAIL INVALID') 
    else:
        user = inputuser_split[0]; hosting = inputuser_split[1]; ekstensi = inputuser_split[2]
        if user.isalnum() == True or '-' in user or '_' in user:
            if hosting.isalnum() == True:  
                if ekstensi.isalpha() == True and len(ekstensi) <= 5:
                     print('EMAIL VALID')
                else:
                    print('EMAIL INVALID')
            else:
                print('EMAIL INVALID')
        else:
            print('EMAIL INVALID')

validitasemail(inputuser)