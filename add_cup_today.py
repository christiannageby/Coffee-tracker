import time

data = [d.split(":") for d in open('C:\CoffeeTracker\stats.data')]

for array in data:
    array[0] = int(array[0])
    array[1] = array[1].rsplit()

w = open("C:\CoffeeTracker\stats.data", 'w')
if str(data[len(data) - 1][1])[2:12] == str(str(time.strftime("%Y-%m-%d"))):
    data[len(data) - 1][0] += 1
    index = 0
    for d in data:
        index += 1
        w.write(str(d[0])+':'+str(d[1])[2:12] + ("\n" if index != len(data) else '' ) )

else:
    for d in data:
        w.write(str(d[0]) + ':' + str(d[1])[2:12]+"\n")
    w.write("1:"+str(time.strftime("%Y-%m-%d")))
w.close()