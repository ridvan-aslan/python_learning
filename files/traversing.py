with open('files/newfile.txt', 'r', encoding="utf-8") as file:
    content1 = file.read(10)
    print(content1)
    file.seek(0)  
    print(file.tell())
    content2 = file.read(10)
    print(content2)