import time
import random

code = random.randint(1, 100)
exp_inp = ""
for cnt, i in enumerate(str(code)):
    if cnt == len(str(code))-1:
        exp_inp = exp_inp + i
    else:
        exp_inp = exp_inp + i + " "
if input(f"{code}\nInput the above code with the space in between: ") != exp_inp:
    exit(1)

backup_cnt, prac_date, prac_code, class_code, uid_2, uid = {}, {}, {}, {}, {}, {}

with open("enc/c_dat", "r") as file:
    raw_dat = file.read()
    file.close()

exec(raw_dat)
print("Initial Values:\nuid_2:", uid_2, "\nprac_code:", prac_code, "\nclass_code:", class_code, "\nuid:", uid,
      "\nprac_date", prac_date, "----------")

print("Hard Resetting the structure in 10 sec")

for i in range(10, 0, -1):
    print(Warning(f"Hard Resetting in {i}"))
    time.sleep(2)

backup_cnt, prac_date, prac_code, class_code, uid_2, uid = {}, {}, {}, {}, {}, {}


def lst_reset():
    global backup_cnt, prac_date, prac_code, class_code, uid, uid_2
    print(backup_cnt, prac_date, prac_code, class_code, uid, uid_2)
    print(f"structure hard reset completed.")
    with open("enc/c_dat", "w") as b_file:
        b_file.write("uid_2:dict=" + str(uid_2) + "\nprac_code:dict=" + str(prac_code) +
                     "\nclass_code:dict=" + str(class_code) + "\nuid:dict=" + str(uid) +
                     "\nprac_date:dict=" + str(prac_date))


lst_reset()
