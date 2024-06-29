uid_2 = {}
prac_code = {}
class_code = {}
uid = {}

with open("enc/c_dat", "r") as file:
    raw_dat = file.read()
    file.close()

exec(raw_dat)

# --------------------------
cc="KAGX"
header = ["Roll Number", "Name"]
std_lst = class_code[cc][3]
for k in std_lst:
    for i in uid_2[k][cc]:
        if i not in header:
            header.append(i)
with open("dat/report.xls", "w") as x:
    x.write("")
csv_file = open("dat/report.xls", "a")
csv_file.write(str(header)[1:-1])
temp_lst = []
for z in std_lst:
    temp_lst = []
    for _ in range(len(header) - 1):
        temp_lst.append("")
    temp_lst.insert(0, uid[z][1])
    temp_lst.insert(1, uid[z][0])
    for d in uid_2[z][cc]:
        temp_lst.insert(header.index(d), 1)
    csv_file.write("\n" + str(temp_lst)[1:-1])
csv_file.close()
print(header)
print(temp_lst)
# --------------------------
#     b_file.write("uid_2:dict=" + str(uid_2) + "\nuid_0_1:dict=" + str(uid_0_1) +
#                  "\nclass_code:dict=" + str(class_code) + "\nuid:dict=" + str(uid))
