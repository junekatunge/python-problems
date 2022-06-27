#Create a Time class and initialize it with hours and minutes.
#Make a method addTime which should take two time object and add them. E.g.- (2 hour and 50 min)+(1 hr and 20 min) is (4 hr and 10 min)
#Make a method DisplayMinute which should display the total minutes in the Time. E.g.- (1 hr 2 min) should display 62 minute.



from time import time


class Time(object):
    def __init__(self,hours,minutes):
        self.hours = hours
        self.minutes = minutes
        
    def addTime(timea,timeb):
        timec = Time(0,0)#to create a new object
        timec.hours = timea.hours + timeb.hours
        timec.minutes = timea.minutes + timeb.minutes
        while timec.minutes >= 60:
           timec.hours += 1
           timec.minutes -= 60
        return timec
   
    def displayTime(self):
        print(self.hours,"hrs", self.minutes,"min")
        
    def DisplayMinute(self):
        print((self.hours * 60) + self.minutes,"minutes")
        
a = Time(7, 30)
b = Time(1, 30)
c = Time.addTime(a,b)

c.displayTime()
c.DisplayMinute()

           


        