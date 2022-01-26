'''
    Timer2.0
    日期：2020-04-04
    增加：
    1、每日结算功能
    修改：
    1、更改文件路径名，进行归类
    2、缩短结束语"继续加油"持续时间
'''
import datetime
import time
import analyze_day as andy


def record():
    while True:
        today = get_today()
        file_name = 'daily_log/time' + today + '.txt'

        project = input("the project you are doing(exit==>e; day end==>end):")
        if project == 'e':
            print("继续加油!!")
            time.sleep(1)
            break

        # 划分当前时间戳
        if project == 'end':
            flag = input("are you sure to end today?(0:back 1:sure):")
            if flag == '1':
                analyze_day(file_name)
                end_day()
                tempf = input("exit(e):")
                if tempf == 'e':
                    # 对今天进行分析
                    print('今天辛苦了，但是离考研又近了一天，明天也要加油！')
                    time.sleep(1)
                    print('晚安！')
                    time.sleep(2)
                    break
            else:
                continue

        # 开始部分的记录
        flag = input("start==>0, end==>1:")
        if flag == '0':
            time_now = datetime.datetime.now()
            with open(file_name, 'a') as file:
                file.writelines(str(project) + " " + flag + " " + str(time_now) + '\n')
            print(str(project) + " start...")
        # 结束的部分记录
        if flag == '1':
            time_now = datetime.datetime.now()
            with open(file_name, 'a') as file:
                file.writelines(str(project) + " " + flag + " " + str(time_now) + '\n')
            print(str(project) + " end...")


def end_day():
    now = str(datetime.datetime.now())
    date = now.split()[0]
    now = now.split()[1]
    now = now.split('.')[0]
    now = now.split(':')

    # 如果end时间点在五点之前，就算当天
    if int(now[0]) < 5:
        with open("today.txt", 'w') as file:
            file.writelines(str(date))
    # 如果在前一天24点或者23点end，则当天+1
    else:
        date_temp = date.split('-')
        date_str = date_temp[2]
        if date_str[0] != '0':
            date_str = str(int(date_str) + 1)
        else:
            date_str = '0' + str(int(date_str[1]) + 1)
        date_tody = date_temp[0] + '-' + date_temp[1] + '-' + date_str
        with open("today.txt", 'w') as file:
            file.writelines(date_tody)


def get_today():
    f = open('today.txt')
    line = f.readline()
    return str(line)


def analyze_day(file_name):
    '''
    1、统计每天一共进行多少项
    2、每一项多少时间
    3、画柱状图
    4、生成完整图像，并保存
    :return:
    '''
    time = andy.get_project_number(file_name)
    res_list = andy.unique_day_time(time)
    andy.generate_graph(res_list)


if __name__ == '__main__':
    record()
