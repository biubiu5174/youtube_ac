f = open("buy_gmail","r")
f_res = open("gmail_list","a+")
for line in f.readlines():
    # print(type(line))
    email = line.split("----")[0].strip()
    password = line.split("----")[1].split(",")[0].strip()
    aux_email = line.split("----")[1].split(",")[1].strip()
    aux_email_password = line.split("----")[1].split(",")[2].strip()
    item = {"email":email,"password":password,"aux_email":aux_email,"aux_email_password":aux_email_password}
    # print(email,password,aux_email,aux_email_password)

    f_res.write(str(item)+"\n")




# {'lastName': 'he', 'firstName': 'tom', 'username': 'tomhe5174', 'email': 'tomhe5174@gmail.com', 'password': 'XLjwOWok'}
