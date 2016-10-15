import matplotlib.pyplot as plt
import csv

f = 'cel.csv'
with open(f, 'r') as data:
    r = csv.reader(data)
    my_list = list(r)
    l = len(my_list[1])
    a = []
    x = []
    for row in my_list[1::]:
        my_sum = 0
        x.append(row[1])
        for i in range(2, l):
            my_sum += float(row[i])
        a.append(my_sum / (l - 2))
print(a)

plt.plot(x, a)
plt.ylabel('some numbers')
plt.show()
