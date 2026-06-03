import json
import random
import string
from pathlib import Path


class Bank:
    database='database.json'
    data=[]

    if Path(database).exists():
        with open(database) as fs:
            data=json.loads(fs.read())

    @classmethod
    def __update(cls):
        with open(cls.database,'w') as fs:
            fs.write(json.dumps(cls.data))

    
    @classmethod
    def __accountgenerate(cls):
        alpha=random.choices(string.ascii_letters,k=4)
        num=random.choices(string.digits,k=4)
        acc =alpha+num
        random.shuffle(acc)
        return ''.join(acc)

    def create_user(self):
        info={
            "name":(input('enter users name : ')),
            'age':int(input('enter users age : ')),
            'email':input('enter users email : '),
            'AccountNo.':Bank.__accountgenerate(),
            'pin' : int(input('generate your pin : ')),
            'Balance': 0 
        }
        if info['age'] < 12 or len(str(info['pin'])) !=4 :
            print('cannot create account')
        else:
            Bank.data.append(info)
            Bank.__update()

    def deposit_money(self):
        accno=input('enter your acc number : ')
        pin = int(input('enter your pin : '))
        
        userdata= [i for i in Bank.data if
                    i['AccountNo.']==accno  and 
                    i['pin']==pin]
        if userdata == False:
            print('wrong account number and you do not exist')
        else:
            amount = int(input('enter your ammount for depositing  : '))
            userdata[0]['Balance']+=amount   # isme data automatically chnge ho jyga due to deep copy 
            bank.__update()
            print(f'balance added successfully ')

            
    def withdraw_money(self):
        accno=input('enter your acc number : ')
        pin = int(input('enter your pin : '))
        
        userdata= [i for i in Bank.data if
                    i['AccountNo.']==accno  and 
                    i['pin']==pin]
        if userdata == False:
            print('wrong account number and you do not exist')
        else:
            amount = int(input('enter your ammount for withdrawing  : '))
            if amount > userdata[0]['Balance']:
                print('insufficient ')
            else:
                userdata[0]['Balance']-=amount   # isme data automatically chnge ho jyga due to deep copy 
                bank.__update()
                print(f'balance updated successfully ')


    def show_details(self):
            accno=input('enter your acc number : ')
            pin = int(input('enter your pin : '))
            
            userdata= [i for i in Bank.data if
                    i['AccountNo.']==accno  and 
                    i['pin']==pin]
            if not userdata:
                print("no data found")
            else:
                for i in userdata[0]:
                    print(f"{i} : {userdata[0][i]}")

    def updating_details(self):
        accno=input('enter your acc number : ')
        pin = int(input('enter your pin : '))
            
        userdata= [i for i in Bank.data if
                    i['AccountNo.']==accno  and 
                    i['pin']==pin]
        
        if not userdata:
            print("no user found")
        else:
            print("you cannot chnage the bank balance , account number and age !!!!!!")
            newdata={'name'  : input('enter your name or press enter to skip  '),
                 'email' : input('enter your email or press enter to skip '),
                 'pin': input('enter your pin or press enter to skip ')
                 }
            if newdata['name']=="":
                newdata['name']=userdata[0]['name']
            if newdata['email']=="":
                newdata['email']=userdata[0]['email']
            if newdata['pin']=="":
                newdata['pin']=str(userdata[0]['pin'])
        
            for i in userdata[0]:
                if i in newdata and i != 'pin':
                    userdata[0][i]=newdata[i]
                if i =='pin':
                    userdata[0][i]=int(newdata[i])
            
            Bank.__update()
            
    
    def delete_account(self):
        accno=input('enter your acc number : ')
        pin = int(input('enter your pin : '))
            
        userdata= [i for i in Bank.data if
                    i['AccountNo.']==accno  and 
                    i['pin']==pin]
        if userdata==False:
            print('no such data')
        else:
            print('Are you sure you want to delete')
            check  =input('press y (yes) or n(no)')
            if check == 'y':
                index=Bank.data.index(userdata[0])
                Bank.data.pop(index)
        Bank.__update()
bank=Bank()

while True:
    print('press 1 for Creating an account ')
    print('press 2 for Depositing money')
    print('press 3 for Withdraw Money ')
    print('press 4 for Details of an user')
    print('press 5 for updating users details')
    print('press 6 for deleting user')
    print('press 0 for exit')

    res = int(input('Please enter your response : '))
    if res== 1:
        bank.create_user()
    if res==2:
        bank.deposit_money()
    if res==3:
        bank.withdraw_money()
    if res==4:
        bank.show_details()
    if res==5:
        bank.updating_details()
    if res==6:
        bank.delete_account()
    if res==0:
        break
    else:
        print('khtm h bhai bhg ja abh')