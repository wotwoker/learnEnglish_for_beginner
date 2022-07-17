import random as r


def judge_book(word):  # 用以判断英文字符串的类型
    name = '单词'  # 定义一字符串变量，初值为‘单词’
    count = 0  # 空格计数器，判断词汇类型
    for tra in word:  # 如果tra等于空格 count就加1,count的值用于判断词汇类型
        if tra == ' ':
            count += 1
    if count == 0:
        name = '单词'
    elif count == 1:
        name = '词组'
    elif count >= 2:
        name = '短句'
    return name  # 返回词汇本名字（单词、词组、短句）


def add_new(e, z):  # 添加新的单词、词组、短句到对应的文件中
    eng_and_zh = e.strip() + '-' + z + '\n'  # 将英文和中文组合并换行（英-中\n)
    flag = True  # 标记，单词已存在时不进行添加操作
    book_name = judge_book(e)  # 判断字符串类型，在不同的词汇本查找
    with open(book_name+'.txt', 'r', encoding='utf-8') as f:  # 先只读查看单词是否已存在
        line = f.readlines()  # 读取所有文件行
        for index in line:  # 遍历查找
            h = index.split('-')[0]  # 以 “-” 为标志取出英文字符
            if e == h:
                print("该单词已经在单词本")
                flag = False
        if flag:  # flag 为 True 时做添加操作
            with open(book_name+'.txt', 'a+', encoding='utf-8') as file:  # a+: 附加读写方式打开
                file.writelines(eng_and_zh)  # 写入英中组合行


def del_new(e):  # 删除,从单词、词组、短句分块查找
    flag = False
    book_name = judge_book(e)  # 判断字符串类型
    with open(book_name+'.txt', 'r', encoding='utf-8') as f1:
        lines = f1.readlines()
        with open(book_name+'.txt', 'w+', encoding='utf-8') as f2:  # 新建读写，重新写入
            for line in lines:
                k = line.split('-')[0]
                if e == k:
                    flag = True
                    continue
                f2.write(line)  # 未被查找的重新写入
    if flag:
        print('删除成功！')
    else:
        print("未有该单词")


def show_new():  # 查看所有单词、词组、短句
    print("以下为单词：\n")
    with open('单词.txt', 'r', encoding='utf-8') as f:
        lines = f.readlines()
        for line in lines:
            line = line.strip('\n')  # 去掉行尾的换行符，以免影响观感
            print(line)
    print("以下为词组：\n")
    with open('词组.txt', 'r', encoding='utf-8') as f:
        lines = f.readlines()
        for line in lines:
            line = line.strip('\n')  # 去掉行尾的换行符，以免影响观感
            print(line)
    print("以下为短句：\n")
    with open('短句.txt', 'r', encoding='utf-8') as f:
        lines = f.readlines()
        for line in lines:
            line = line.strip('\n')  # 去掉行尾的换行符，以免影响观感
            print(line)
    print("查询成功！")


def search_zh(eng):  # 查询英文的汉语意思，分块查找
    flag = False
    book_name = judge_book(eng)  # 判断字符串类型
    with open(book_name+'.txt', 'r', encoding='utf-8') as files:
        line = files.readlines()
        for index in line:
            h = index.split('-')[0]
            if eng == h:
                print(index)
                flag = True
    if not flag:
        print("单词本里未有该单词")


def search_eng(zh):  # 查询汉语的英文，逐级查找匹配汉语
    flag = False
    with open('单词.txt', 'r', encoding='utf-8') as files:
        line = files.readlines()
        for index in line:
            o = index.split('-')[1]  # 拆分字符串，获取第二个
            if zh + '\n' == o:
                print(index)
                flag = True
    with open('词组.txt', 'r', encoding='utf-8') as files:
        line = files.readlines()
        for index in line:
            o = index.split('-')[1]  # 拆分字符串，获取第二个
            if zh + '\n' == o:
                print(index)
                flag = True
    with open('短句.txt', 'r', encoding='utf-8') as files:
        line = files.readlines()
        for index in line:
            o = index.split('-')[1]  # 拆分字符串，获取第二个
            if zh + '\n' == o:
                print(index)
                flag = True
    if not flag:
        print("单词本里未有该单词")


def recite_word():  # 背单词
    n = 0  # 答错题数
    m = 0  # 答对题数
    book_name = '单词'
    is_continue = "y"
    while is_continue == "y" or is_continue == "Y" or is_continue == "\n":
        with open(book_name+'.txt', 'r', encoding='utf-8') as wordFile:
            world_list = wordFile.readlines()
            for index in r.sample(world_list, 1):  # 随机选取一行
                bu = r.randint(0, 1)  # 记录布尔值0或1
                x = index.split("-")[bu].strip('\n')  # 随机选取英文或汉语
                y = index.split("-")[(bu + 1) % 2].replace('\n', '').replace('\r', '')  # 选取x的反
                # split分的汉语最后有个换行符，淦，用 .replace('\n', '').replace('\r', '') 或 .strip('\n') 可以去掉换行符
                print("\n随机英语或汉语:")
                print(">------>   " + x)

                if bu:
                    guess = input("输入英语: ").strip()  # 防止用户误操作录入空白
                else:
                    guess = input("输入汉语: ").strip()  # 防止用户误操作录入空白

                flag = 1  # 标记，防止同一个题多次出错，影响总体正确率
                while guess != y:
                    print("对不起，不正确。")
                    if flag == 1:  # 多次出错 n 只增加一次，不重复计数
                        n = n + 1
                    flag = 0
                    rate = m / (n + m)
                    print('——>正确率：%.1f' % (rate*100), '%')
                    guess = input("继续输入：").strip()
                if guess == y:
                    print("真棒！答对了！！")
                    m = m + 1
                    rate = m / (n + m)
                    print('——>正确率：%.1f' % (rate*100), '%')
                is_continue = input("是否继续（Y/N）：")
                # 判断晋级（条件：答了至少5道题，且正确率大于或等于0.9）
                if n+m >= 5 and rate >= 0.9 and book_name == '单词':
                    book_name = '词组'
                    n = m = 0  # 晋级重新计数
                    print('——恭喜晋级！——')
                elif n+m >= 5 and rate >= 0.9 and book_name == '词组':  # 判断晋级
                    book_name = '短句'
                    n = m = 0  # 晋级重新计数
                    print('——恭喜晋级！——')
                elif n+m >= 5 and rate < 0.9 and book_name == '词组':  # 判断降级
                    book_name = '单词'
                    print('——降一等级！——')
                elif n+m >= 5 and rate < 0.9 and book_name == '短句':  # 判断降级
                    book_name = '词组'
                    print('——降一等级！——')
    print("太棒了！你又完成了一次学习！下次再来哦！")


def main():  # 主菜单
    print("""
                     欢迎来到单词学习系统O(∩_∩)O
                  妈妈再也不用担心我的学习了(～￣▽￣)～　
            -------------------------------------------
                1.添加生词     2.删除生词      3.查看所有
                4.查询生词     5.背 生 词      6.退 出
                      --------------------
    """)
    while True:
        i = int(input("输入您要选择的功能：1.添加  2.删除  3.查看  4.查询  5.背  6.退出\n"))
        if i == 1:
            e = input("输入生词的英文：")
            z = input("输入生词的中文：")
            add_new(e, z)
        if i == 2:
            e = input("输入生词的英文：")
            del_new(e)
        if i == 3:
            show_new()
        if i == 4:
            a = input("查询中文or查询英文：（e表示英文，z表示中文）")
            if a == "z":
                e = input("请输入英文单词")
                search_zh(e)
            if a == "e":
                z = input("请输入该单词中文意思")
                search_eng(z)
        if i == 5:
            recite_word()
        if i == 6:
            print("确定要退出该程序吗？")
            u = input("yes or no:")
            if u == "yes" or u == "y" or u == 'Y':
                break


main()
