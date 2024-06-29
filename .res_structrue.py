import time

backup_cnt, prac_date, prac_code, class_code, uid_2 = {}, {}, {}, {}, {}

with open("enc/c_dat", "r") as file:
    raw_dat = file.read()
    file.close()

exec(raw_dat)
print("Initial Values:\nuid_2:", uid_2, "\nprac_code:", prac_code, "\nclass_code:", class_code, "\nuid:", uid,
      "\nprac_date", prac_date, "----------")

print("Resetting the structure in 10 sec")

for i in range(10, 0, -1):
    print(Warning(f"Resetting in {i}"))
    time.sleep(1)

backup_cnt, prac_date, prac_code, class_code, uid_2 = {}, {}, {}, {}, {}


def lst_reset():
    global backup_cnt, prac_date, prac_code, class_code, uid, uid_2
    print(backup_cnt, prac_date, prac_code, class_code, uid, uid_2)
    print(f"structure backed up while exiting.")
    with open("enc/c_dat", "w") as b_file:
        b_file.write("uid_2:dict=" + str(uid_2) + "\nprac_code:dict=" + str(prac_code) +
                     "\nclass_code:dict=" + str(class_code) + "\nuid:dict=" + str(uid) +
                     "\nprac_date:dict=" + str(prac_date))


lst_reset()
