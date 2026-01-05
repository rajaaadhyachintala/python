import random
import time
def getRandomDate (starDate, endDate):
    print ("printing random date between", starDate,"and", endDate)
    randomGenerator = random.random()
    dateformat = '%m/%d/%Y'
    starttime = time.mktime(time.strptime(starDate, dateformat))
    endtime = time.mktime(time.strptime(endDate, dateformat))
    randomtime = starttime + randomGenerator * (endtime - starttime)
    RandomDate = time.strftime(dateformat, time.localtime(randomtime))
    return RandomDate 
print ("Random date =", getRandomDate("1/1/2020" , "12/12/2024"))