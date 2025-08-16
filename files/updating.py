# with open('files/newfile.txt', 'r+', encoding="utf-8") as file:
#     file.seek(5)
#     file.write('ABCDE')  # Overwrites from position 5
#     file.seek(0)
#     content = file.read()
#     print(content) 

# with open('files/newfile.txt', 'r+', encoding="utf-8") as file:    
#     print(file.read())

# with open('files/newfile.txt', 'a+', encoding="utf-8") as file:
#     file.write('\nNew line added at the end.')
#     file.seek(0)
#     content = file.read()
#     print(content)

# with open('files/newfile.txt', 'r+', encoding="utf-8") as file:
#     content = file.read()
#     content = "Rıdvan Aslan\n" + content
#     file.seek(0)
#     file.write(content)
#     file.seek(0)
#     print(file.read())

with open('files/newfile.txt', 'r+', encoding="utf-8") as file:
    my_list = file.readlines()
    my_list.insert(3, "Rıdvan\n")
    file.seek(0)
    file.writelines(my_list)
    file.seek(0)
    print(file.read())