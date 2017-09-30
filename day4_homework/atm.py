import os , json, time , decimal

def info_print(id):
    filename = 'accounts/' + str(id)
    with open(filename,'r',encoding='utf-8') as read_f:
        data = json.loads(read_f.read())
        print("用户id:",data['id'])
        print("用户信用额度:",data['credit'])
        print("用户余额:",data['balance'])
        print("用户状态:",data['status'])


def with_draw(id,money):
    filename = 'accounts/' + str(id)
    with open(filename, 'r', encoding='utf-8') as read_f ,open('.swap','w') as write_f:
        data = json.loads(read_f.read())
        if money > data['balance']:
            print("余额不足，无法完成提现！")
        else:
            data['balance'] = data['balance'] - money*1.05
            print("提现:",money,"手续费为",money*0.05,"余额:",data['balance'])
            write_f.write(json.dumps(data))

    os.remove(filename)
    os.rename('.swap',filename)

def top_up(id,money):



if __name__ == '__main__':
    #info_print(20170930152752)
    # with_draw(20170930152752,500)

