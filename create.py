import requests
# with open("/Users/anodic_passion/Downloads/111111111111111111111111111111111111111111111111.xlsx - Sheet1.csv") as csv:
#     file = csv.read()
#
# print(file.split("\n"))
# for rec in file.split("\n"):
#     # print(rec)
#     _, roll, name = rec.split(",")
#     password = name.split(" ")[0] + "123"
#     print(roll, name)
#     js_1 = requests.post(json={"name": str(name), "roll": str(roll), "password": password}, url="http://127.0.0.1:5500/signup")
#     n_id = js_1.json()["n_id"]
#     print(n_id)
#     print(roll, name, password)
#     with open("/Users/anodic_passion/Downloads/SE_AIDS_Att_Id.csv", "a") as f:
#         f.write(str(roll) + "," + name + "," + str(n_id) + "," + password + "\n")
#     print("adding to lect")
#     js_2 = requests.post(json={"subject": "DGHQ"}, url="http://127.0.0.1:5500/add_subject", cookies={"user_id": str(n_id)})
#     print(js_2.status_code)
#     js_2 = requests.post(json={"subject": "FZFW"}, url="http://127.0.0.1:5500/add_subject", cookies={"user_id": str(n_id)})
#     print(js_2.status_code)
#     js_2 = requests.post(json={"subject": "KPVB"}, url="http://127.0.0.1:5500/add_subject", cookies={"user_id": str(n_id)})
#     print(js_2.status_code)
#     js_2 = requests.post(json={"subject": "NHWR"}, url="http://127.0.0.1:5500/add_subject", cookies={"user_id": str(n_id)})
#     print(js_2.status_code)
#
#     if 1 <= int(roll) < 26:
#         bat = "A"
#     elif 26 <= int(roll) <= 50:
#         bat = "B"
#     else:
#         bat = "C"
#
#
#     js_2 = requests.post(json={"subject": "XXTI" + bat}, url="http://127.0.0.1:5500/add_batch",
#                          cookies={"user_id": str(n_id)})
#     print(js_2.status_code)
#     js_2 = requests.post(json={"subject": "NKLJ" + bat}, url="http://127.0.0.1:5500/add_batch",
#                          cookies={"user_id": str(n_id)})
#     print(js_2.status_code)
#     js_2 = requests.post(json={"subject": "CTLX" + bat}, url="http://127.0.0.1:5500/add_batch",
#                          cookies={"user_id": str(n_id)})
#     print(js_2.status_code)

# print(file.split("\n")[0].split(",")[1:])
# Class code for year "SE AIDS" subject "DSA" is DGHQ
# Class code for year "SE AIDS" subject "MIS" is FZFW
# Class code for year "SE AIDS" subject "IOT" is KPVB
# Class code for year "SE AIDS" subject "SE" is NHWR


# Class code for year "SE AIDS" subject "IOT (Lab)" is XXTI
# Class code for year "SE AIDS" subject "DSA (Lab)" is NKLJ
# Class code for year "SE AIDS" subject "PBL (Lab)" is CTLX


js_2 = requests.post(json={"subject": "CTLXA"}, url="http://127.0.0.1:5500/add_batch",
                         cookies={"user_id": "300"})
print(js_2.status_code)
