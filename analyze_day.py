def get_project_number(filepath):
    # 打开文件
    f = open(filepath)
    # 全部读取文件
    lines = f.readlines()
    index = str(len(lines)//2)
    print("今天共有" + index + "次活动记录")

    log_list = []
    pro_name_list = []
    flag_list = []
    time_list = []
    # 逐行读取文件
    for line in lines:
        log_list.append(line[:-1])
        line_list = line[:-1].split()
        pro_name_list.append(line_list[0])
        flag_list.append(line_list[1])
        temp = line_list[2] + " " + line_list[3]
        time_list.append(temp)

    pro_name_set = set(pro_name_list)
    pro_num = str(len(pro_name_set))
    print("今天共进行了" + pro_num + "项活动")


    time = []
    log_list_temp = log_list

    # 本次程序暂时只实现，单线程，即顺序执行的顺序
    for i in range(len(log_list_temp)):
        pro_list = log_list_temp[i].split()
        if pro_list[1] == '1':
            continue
        if i+1 < len(log_list_temp):
            pro_list_next = log_list_temp[i+1].split()
            # 当当前值和下一个值的时间差
            if pro_list[0] == pro_list_next[0]:
                h1 = pro_list[3].split(':')[0]
                m1 = pro_list[3].split(':')[1]
                s1 = pro_list[3].split(':')[2].split('.')[0]

                # 结束时间
                # 如果在一天
                if pro_list[2].split('-')[-1] == pro_list_next[2].split('-')[-1]:
                    h2 = pro_list_next[3].split(':')[0]
                    m2 = pro_list_next[3].split(':')[1]
                    s2 = pro_list_next[3].split(':')[2].split('.')[0]
                # 如果不在一天
                else:
                    h2 = str(int(pro_list_next[3].split(':')[0]) + 24)
                    m2 = pro_list_next[3].split(':')[1]
                    s2 = pro_list_next[3].split(':')[2].split('.')[0]

                time1 = int(s1) + int(m1)*60 + int(h1)*60*60
                time2 = int(s2) + int(m2)*60 + int(h2)*60*60
                seconds = time2-time1
                # divmod是吧余数除数结合起来
                m, s = divmod(seconds, 60)
                h, m = divmod(m, 60)

                res = pro_list[0] + " " + str(h) + ':' + str(m) + ':' + str(s) + " " + str(seconds)
                time.append(res)

    return time


def unique_day_time(time):
    name = set([t.split()[0] for t in time])
    print(name)
    res_list = []
    for n in name:
        during_time = 0
        for t in time:
            if n == t.split()[0]:
                # 获得最终的秒数
                during_time += int(t.split()[2])
        m, s = divmod(during_time, 60)
        h, m = divmod(m, 60)
        res = n + " " + str(h) + ':' + str(m) + ':' + str(s) + ' ' + str(during_time)
        res_list.append(res)
    return res_list


def generate_graph(res_list):
    import matplotlib.pyplot as plt
    import os

    # 设置matplotlib正常显示中文和负号
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.rcParams['axes.unicode_minus'] = False

    plt.figure()
    x = range(len(res_list))
    y = [int(res.split()[2]) for res in res_list]
    xname = [res.split()[0] for res in res_list]
    label = [res.split()[1] for res in res_list]

    a = len(x) *0.0375
    for i in range(len(x)):
        plt.text(x[i]-a, y[i] + 40, "%s" % label[i])

    f = open('today.txt')
    line = f.readline()
    title = line + '时间总结'
    plt.title(title)
    plt.bar(x, y, width=0.5)
    plt.xticks(x, xname, rotation=15)
    plt.yticks([])

    path = 'summary_figure'
    isExists = os.path.exists(path)
    if not isExists:
        os.makedirs(path)

    plt.savefig('summary_figure/' + title)
    plt.show()


# if __name__ == '__main__':
#     time = get_project_number("time2020-04-02.txt")
#     # time = get_project_number('today.txt')
#     # print(len(time))
#     # for i in time:
#     # print(time[0])
#     res_list = unique_day_time(time)
#     generate_graph(res_list)






# for project in log_list_temp:
    #     if flag != 0:
    #         log_list.re
    #
    #
    #     pro_list = project.split()
    #     # 如果这条记录是开始则匹配最近的1
    #     if pro_list[1] == '0':
    #         # 去除当前条信息
    #         name = pro_list[0]
    #         log_list_temp.remove(project)
    #         log_list_temp2 = log_list_temp
    #         for project2 in log_list_temp2:
    #             pro_list2 = project2.split()
    #             if pro_list2[0] == name and pro_list2[1] == '1':
    #                 # 计算持续时间
    #                 # 先转化成秒，再做减法
    #                 # 开始时间
    #                 h1 = pro_list[3].split(':')[0]
    #                 m1 = pro_list[3].split(':')[1]
    #                 s1 = pro_list[3].split(':')[2].split('.')[0]
    #
    #                 # 结束时间
    #                 h2 = pro_list2[3].split(':')[0]
    #                 m2 = pro_list2[3].split(':')[1]
    #                 s2 = pro_list2[3].split(':')[2].split('.')[0]
    #
    #                 time1 = int(s1) + int(m1)*60 + int(h1)*60*60
    #                 time2 = int(s2) + int(m2)*60 + int(h2)*60*60
    #
    #                 # print(h2 + " " + m2 + " " + s2)
    #                 seconds = time2-time1
    #                 # print(seconds)
    #                 # divmod是吧余数除数结合起来
    #                 m, s = divmod(seconds, 60)
    #                 h, m = divmod(m, 60)
    #
    #                 res = name + " " + str(h) + ':' + str(m) + ':' + str(s)
    #                 # res = name + str(seconds)
    #                 # 将持续时间段加入list中
    #                 time.append(res)
    #                 # 删除当前记录
    #                 # log_list_temp.remove(project2)
    #                 break