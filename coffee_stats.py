import time
import sys

def median(matrix):
    result = 0
    for i in matrix:
        result += float(i)
    return result/float(len(matrix))

def total(matrix):
    result = 0
    for i in matrix:
        result += int(i)
    return result

if __name__ == '__main__':
    data = [d.split(":") for d in open('C:\CoffeeTracker\stats.data')]

    for array in data:
        array[1] = array[1].rsplit()

    print "cups today ", data[len(data)-1][0] if str(data[len(data) - 1][1])[2:12] == str(str(time.strftime("%Y-%m-%d"))) else 0
    print "cups last week: ", total([row[0] for row in data[-7:]])
    print "cups last 30 days: ", total([row[0] for row in data[-30:]])
    print "cups since installation: ", total([row[0] for row in data])
    print "\n"
    print "average last week: ", median([row[0] for row in data[-7:]]), "cups"
    print "avarage last month: ", median([row[0] for row in data[-30:]]), " cups"
    print "avarage since installation: ", median([row[0] for row in data]), " cups"