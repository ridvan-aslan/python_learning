try:
    with open('files/newfile.txt', 'r', encoding='utf-8') as file:
        # for i in file:
        #     print(i.strip())

        # content1 = file.read()
        # print("Content 1:")
        # print(content1)
    
        # content2 = file.read()
        # print("Content 2:")
        # print(content2)

        # content = file.read(6)
        # content = file.read(3)
        # print(content)

        # print(file.readline().strip())
        # print(file.readline())
        # print(file.readline())
        # print(file.readline())
        # print(file.readline())

        my_list = file.readlines()
        print(my_list)
        print(my_list[1])
             
except FileNotFoundError:
    print("File not found. Please check the file path and try again.")
finally:
    print("File operation completed.")