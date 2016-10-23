import matplotlib.pyplot as plt
import matplotlib.ticker as tkr
import csv

markers_list = ['o', 'v', 's', 'D', 'd']
files_list = ['rsel.csv', 'cel-rs.csv', '2cel-rs.csv', 'cel.csv', '2cel.csv']
names_list = ['1-Evol-RS', '1-Coev-RS', '2-Coev-RS', '1-Coev', '2-Coev']


def calc_length():
    with open(files_list[0], 'r') as data:
        r = csv.reader(data)
        my_list = list(r)
        l = len(my_list[1])
        l2 = len(my_list) - 1
        return l, l2


def kilo(x, _):
    return '%.0f' % (x / 1000)


def percent(x, _):
    return '%.0f' % (x * 100)


def load_data(f, l):
    with open(f, 'r') as data:
        r = csv.reader(data)
        my_list = list(r)
        a = []
        x = []
        last = []
        for row in my_list[1::]:
            my_sum = 0
            x.append(row[1])
            for i in range(2, l):
                my_sum += float(row[i])
            a.append(my_sum / (l - 2))
        row = my_list[-1]
        row = row[2:]
        for i in row:
            last.append(float(i))
    return a, x, last


def main():
    x = []
    a = []
    last = []
    l, l2 = calc_length()
    for i in range(5):
        a1, x1, last1 = load_data(files_list[i], l)
        x.append(x1)
        a.append(a1)
        last.append(last1)
    plt.rcParams["figure.figsize"] = [13.4, 10]
    fig = plt.figure()
    line_graph = fig.add_subplot(121)
    line_graph_up = line_graph.twiny()
    for i in range(5):
        line_graph.plot(x[i], a[i], marker=markers_list[i], markevery=l2 / 8, label=names_list[i])
    line_graph.legend(loc='best')
    line_graph.grid(True)
    line_graph.set_xlim(0, 500000)
    line_graph.set_ylim(0.6, 1)
    line_graph_up.set_xticks(range(l2 + 1)[0::40])
    line_graph.xaxis.set_major_formatter(tkr.FuncFormatter(kilo))
    line_graph.yaxis.set_major_formatter(tkr.FuncFormatter(percent))
    line_graph.set_xlabel('Rozegranych gier ( x 1000)')
    line_graph.set_ylabel('Odsetek wygranych gier [%]')
    line_graph_up.set_xlabel('Pokolenie')
    box_graph = fig.add_subplot(122)
    meanpointprops = dict(marker='o', markerfacecolor='blue')
    box_graph.boxplot(last, labels=names_list, showmeans=True, notch=True, meanprops=meanpointprops)
    box_graph.grid(True)
    box_graph.yaxis.set_major_formatter(tkr.FuncFormatter(percent))
    box_graph.set_ylim(0.60, 1)
    plt.xticks(rotation=20)
    plt.savefig('plot.pdf')
    plt.show()


if __name__ == '__main__':
    main()
