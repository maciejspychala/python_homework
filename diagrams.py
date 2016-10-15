import matplotlib.pyplot as plt
import matplotlib.ticker as tkr
import csv

markers_list = ['o', 'v', 's', 'D', 'd']
files_list = ['cel.csv', '2cel.csv', 'cel-rs.csv', '2cel-rs.csv', 'rsel.csv']


def calc_length():
    with open(files_list[0], 'r') as data:
        r = csv.reader(data)
        my_list = list(r)
        l = len(my_list[1])
        l2 = len(my_list) - 1
        return l, l2


def kilo(x, _):
    return '%.0f' % (x / 1000)


def load_data(f):
    with open(f, 'r') as data:
        r = csv.reader(data)
        my_list = list(r)
        a = []
        x = []
        for row in my_list[1::]:
            my_sum = 0
            x.append(row[1])
            for i in range(2, l):
                my_sum += float(row[i])
            a.append(my_sum / (l - 2))
    return a, x


x = []
a = []
l, l2 = calc_length()
for i in range(5):
    a1, x1 = load_data(files_list[i])
    x.append(x1)
    a.append(a1)

fig = plt.figure()
ax1 = fig.add_subplot(111)
ax2 = ax1.twiny()
ax1.grid(True)
ax1.set_xlim(0, 500000)
for i in range(5):
    ax1.plot(x[i], a[i], marker=markers_list[i], markevery=l2 / 8)
formatter = tkr.FuncFormatter(kilo)
ax1.xaxis.set_major_formatter(formatter)
ax2.set_xlim(0, l2)
ax2.set_xticks(range(l2 + 1)[0::(l2 / 5)])
plt.show()
