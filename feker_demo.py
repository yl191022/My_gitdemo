from faker  import Faker

faker = Faker()

with open("register.txt","a+",encoding="utf-8") as f:
    for i in range(1,100000):
        str1 = f"{faker.user_name()},{faker.password(length=8,special_chars=False)},{str(faker.random_int(1000000,9999999999))+'@qq.com'}"
        f.write(str1+"\n")

# with open("file.txt","a+") as f:
#     for i in range(1,100000):
#         str1=f"{faker.sentence()},{faker.paragraph()}"
#         f.write(str1+"\n")

# print(faker.password(length=8,special_chars=False))
