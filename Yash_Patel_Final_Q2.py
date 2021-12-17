import datetime
now = datetime.datetime.now()
print("\ntodays date: ,todays time: ")
print(now.strftime("%m-%d-%Y"), now.strftime("%H-%M-%S"))

fileread = open('PROG1783File2.txt', "rt")
data = fileread.read()
data = data.replace('Yash Patel','********')
fileread.close()
fileread = open("PROG1783File2.txt", "wt")
fileread.write(data)
fileread.close()


