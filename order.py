import csv
# the algorithm works simply by finding the maximum value, removing it, then find the max of the new
# list. after that, get the name of that number.
f = csv.DictReader(open("/home/islam/PycharmProjects/Algorithm/yob1995.csv"), ['name', 'sex', 'num'])
num_lst = [int(row['num']) for row in f if row['sex'] == 'F']
omitted_num = max(num_lst)
num_lst.remove(omitted_num)
second_num = str(max(num_lst))
# for some reason, f no longer have the csv file. so, i read it again.
f = csv.DictReader(open("/home/islam/PycharmProjects/Algorithm/yob1995.csv"), ['name', 'sex', 'num'])
for line in f:
    if (line['sex'] == 'F') and (line['num'] == second_num):
        print(line['name'])
# An interesting method is done by the professor
new_file = open("/home/islam/PycharmProjects/Algorithm/yob1995.txt")
max_name = 'None'
max_val = 0
sec_max_name = 'None'
sec_max_val = 0
for line in new_file:
    # print(type(line))
    (name, sex, val) = line.split(sep=',')
    val = int(val)
    if sex == "F":
        if val > max_val:
            sec_max_val = max_val
            sec_max_name = max_name
            max_val = val
            max_name = name
        elif val > sec_max_val:
            sec_max_val = val
            sec_max_name = name
print(sec_max_name)
