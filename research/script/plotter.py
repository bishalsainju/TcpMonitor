import csv
import matplotlib.pyplot as plt
from os.path import expanduser
import os
from inputSetter import get_input

file_list = get_input()['file_list']
home = expanduser('~')
path = home + '/Desktop/research'

def create_new_dir(path):
    if not os.path.exists(os.path.dirname(path)):
        try:
            os.makedirs(os.path.dirname(path))
        except OSError as exc:
            if exc.errno != errno.EExist:
                raise
    return True

def plot_data(filename):
    image_url = path +'/graphs2/'+filename+'.png'
    create_new_dir(image_url)

    fig = plt.figure( )
    fig.set_size_inches(18.5, 10.5)

    with open(path + '/data/'+filename+'.csv', "r") as fp:
        reader = csv.reader(fp)
        dat_read = [row for row in reader]

    y = [[],[],[],[],[], [], [], [], []]

    for row in dat_read[1:]:
        for i in [1, 4, 6, 8]:
            y[i].append(float(row[3+i]))


    x = list(range(0,len(y[1])))
    # print len(y[1])
    # x2 = []
    # for x1 in x:
    #     x2.append(x1*100/100)
    # x = x2
    # print x

    # plt.subplot(3, 3, 1)
    # plt.plot(x, y[0], label = "rto")
    # plt.title('rto')
    #
    plt.subplot(2, 2, 1)
    plt.plot(x, y[1], label = "rtt")
    plt.title('rtt')
    plt.ylabel('rtt(ms)')

    # plt.subplot(3, 3, 3)
    # plt.plot(x, y[2], label = "ato")
    # plt.title('ato')

    # plt.subplot(3, 3, 4)
    # plt.plot(x, y[3], label = "mss")
    # plt.title('mss')

    plt.subplot(2, 2, 2)
    plt.plot(x, y[4], label = "cwnd")
    plt.title('cwnd')

    # plt.subplot(3, 3, 6)
    # plt.plot(x, y[5], label = "ssthresh")
    # plt.title('ssthresh')

    plt.subplot(2, 2, 3)
    plt.plot(x, y[6], label = "send")
    plt.title('Throughput')
    # plt.xlabel()
    plt.ylabel('Throughput(MB/s)')

    # plt.subplot(3, 3, 8)
    # plt.plot(x, y[7], label = "pace")
    # plt.title('pace')

    plt.subplot(2, 2, 4)
    plt.plot(x, y[8], label = "unacked")
    plt.title('unacked')

    manager = plt.get_current_fig_manager()
    manager.resize(*manager.window.maxsize())

    plt.savefig(image_url)
    plt.show()
    plt.gcf().clear()

for i in file_list:
    filename = str(i)
    plot_data(filename)
