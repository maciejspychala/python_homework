import matplotlib.pyplot as plt
import matplotlib.ticker as tkr
import csv


def kilo(x, _):
    return '%.0f' % (x / 1000)


f = 'cel.csv'
with open(f, 'r') as data:
    r = csv.reader(data)
    my_list = list(r)
    l = len(my_list[1])
    l2 = len(my_list) - 1
    print(l2)
    a = []
    x = []
    for row in my_list[1::]:
        my_sum = 0
        x.append(row[1])
        for i in range(2, l):
            my_sum += float(row[i])
        a.append(my_sum / (l - 2))
print(a)

fig = plt.figure()
ax1 = fig.add_subplot(111)
ax2 = ax1.twiny()
ax1.plot(x, a)
formatter = tkr.FuncFormatter(kilo)
ax1.xaxis.set_major_formatter(formatter)
ax2.set_xlim(0, l2)
ax2.set_xticks(range(l2 + 1)[0::(l2 / 5)])
plt.show()
