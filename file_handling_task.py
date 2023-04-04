# Reading file

# f = open("Pythonlife_works/sample.txt",mode = "r")
# content = f.read()   # read = total data
# content = f.read(15)
# print(content)
# f.close()

# f = open("Pythonlife_works/sample.txt",mode = "r")
# # content = f.readline()  # readline = Only one line data
# content = f.readlines() # readlines = data in List form
# print(content)
# f.close()

# f = open("Pythonlife_works/demo.txt",mode = "w")
# f.write("This is write function")
# f.close()

# f = open("Pythonlife_works/demo.txt",mode = "a")
# f.write("This is append function")
# f.close()

## Reading file in r+ mode
# with open("Pythonlife_works/demo.txt",'r+') as fd:
#     print(fd.read())
#     print(fd.tell())

## Reading file in w+ mode  ## w+ ==> write and read (data replace)
# with open("Pythonlife_works/demo.txt",'w+') as fd:
#     print(fd.tell())
#     c = fd.write("This is w+")
#     print(fd.read())
#     print(fd.tell())

## Write file in 'r+' mode ## r+ ==> read and write starts from 0 index
# with open("Pythonlife_works/demo.txt",'r+') as fd:
#     fd.write("This is New text")

## Write file in ‘w+’ mode
# with open("Pythonlife_works/demo.txt",'w+') as fd:
#     fd.write("New text.")

'''
tell() method can be used to get the position of File Handle
tell() method returns current position of file object.
This method takes no parameters and returns integer values.

'''

# # Python program to demonstrate tell() method

# fp = open("Pythonlife_works/demo.txt",'r')
# # print(fp.tell())
# fp.read(8)
# print(fp.tell())
# fp.close()


'''
seek() function is used to change the position of the File Handle 
to a given specific position. 
File handle is like a cursor, 
which defines from where the data has to be read or written in the file. 

'''

'''
f.seek(0)	
Move file pointer to the beginning of a File
'''

# fp = open("Pythonlife_works/demo.txt",'r')
# print(fp.tell())  # 0
# fp.read(2)

# print(fp.tell())  # 2
# fp.seek(0)
# print(fp.tell())  # 0
# fp.close()


# file = open("Pythonlife_works/demo.txt",'r+') # open
# content=file.read() # operation
# v=str(content)
# print(v)
# f=v.split()
# print(f)
# f.insert(2,'  chetan')
# print(file.tell())
# file.close()
# file=open('Pythonlife_works/demo.txt',mode='w')
# print(f)
# for i in f:
#     file.writelines([i])