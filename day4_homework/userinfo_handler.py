import json ,time,os,decimal


def AutoFirst():
    '''
    初始化用户信息，默认信用额度15000,
    将用户信息以id为名，存成一个文件，放在accounts下，
    并将username和id变成键值对，存在info表的字典里
    '''
    user = {"balance": 15000, "expire_date": "2021-01-01", "enroll_date": None, "credit": 15000, "id": None,"status": 0, "pay_day": 22, "password": None}

    while True:
        with open('accounts/info', 'r', encoding='utf-8') as check:
            checkout = json.loads(check.read())
            username = input("输入您的用户名：").strip()
            if username in checkout:
                print("用户名已存在，请重新输入！")
                continue
            else:
                break

    password = input("请输入您的密码：").strip()

    user['id'] = int(time.strftime('%Y%m%d%H%M%S',time.localtime()))
    user['enroll_date'] = time.strftime('%Y-%m-%d',time.localtime())

    user['password'] = password
    filename = 'accounts/' + str(user['id'])
    with open(filename,'w') as newfile:
        newfile.write(json.dumps(user))

    with open('accounts/info','r',encoding='utf-8') as read_f , open('accounts/.info','w') as write_f:
         if not read_f.read() == '':
            read_f.seek(0,0)
            ss = json.loads(read_f.read())
            ss[username] = user['id']
            write_f.write(json.dumps(ss))
         else:
             ss = {username:user['id']}
             write_f.write(json.dumps(ss))
    os.remove('accounts/info')
    os.rename('accounts/.info','accounts/info')



def  modify(id,**kwargs):
    '''
     用户传入status，修改用户的status，0是正常，1是冻结
     用户传入credit，修改用户的信用额度，自动同步余额
    '''
    files = os.listdir('accounts')
    filename = 'accounts/' + str(id)
    if str(id) in files:
        with open(filename, 'r', encoding='utf-8') as read_f, open('.swap', 'w') as write_f:
            read_f.seek(0, 0)
            ss = json.loads(read_f.read())
            for k in kwargs:
                ss[k] = float(kwargs[k])
                if k == 'credit':
                    ss['balance'] = float(kwargs[k])
            write_f.write(json.dumps(ss))
        os.remove(filename)
        os.rename('.swap', filename)
        print("操作成功")
    else:
        print("用户id已存在！！")



if __name__ == '__main__':
    # AutoFirst()
     modify(20170930152752,status=0)
