import datetime
uid_2 = {}
prac_code = {}
class_code = {}
uid = {}
prac_date = {}

with open("enc/c_dat", "r") as file:
    raw_dat = file.read()
    file.close()

exec(raw_dat)
# print("uid_2:", uid_2, "\nuid_0_1:", prac_code, "\nclass_code:", class_code, "\nuid:", uid)

print(uid)
