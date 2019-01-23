def show_magicians(names):
    #打印每个魔术师的名字
    for name in names:
        msg = "Hello, " + name.title() + "!"
        print(msg)

username = ['cyril','david stone','Richard Mo','Eric']
show_magicians(username)