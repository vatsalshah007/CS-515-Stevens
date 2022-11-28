# Vatsal Shah
# 10474245 

class Time:
    def __init__(self, hours, minutes):
        try:
            assert (00 <= hours <= 24)

            assert (00 <= minutes <= 60)

            self.hours = hours
            self.minutes = minutes
        
        except AssertionError:
            print("Invalid time")
        
    def __str__(self):
        if self.hours < 10 and self.minutes < 10:
            return '0' + str(self.hours) + ':' + '0' + str(self.minutes)
        elif self.hours < 10:
            return '0' + str(self.hours)+":"+str(self.minutes)
        elif self.minutes < 10:
            return str(self.hours)+":"+ '0' + str(self.minutes)

        return str(self.hours)+":"+str(self.minutes)

    def __eq__(self, __o):
        return self.hours == __o.hours and self.minutes == __o.minutes

    def isAfterNoon(self):
        if (17 > self.hours >= 12):
            return True
        return False

    def isBefore(self, t2):
        if self.hours < t2.hours:
            return True
        elif self.hours == t2.hours and self.minutes < t2.minutes:
            return True
        return False

    def tick(self):
        if self.minutes == 59:
            self.hours += 1
            self.minutes = 0
        else:
            self.minutes += 1
        if self.hours == 24:
            self.hours = 0

    def shortHelp (self , other):
        if self == other:
            return Time(0, 0)
        elif self.isBefore(other):
            return other.shortHelp(self)
        mins = 0
        hours = 0
        while self != other:
            self.tick()
            mins += 1
            if mins == 60:
                hours += 1
                mins = 0
        return Time(hours, mins)

    def shortTimeApart(self, other):
        selfHours = self.hours
        selfMinutes = self.minutes
        otherHours = other.hours
        otherMinutes = other.minutes

        self1 = Time(selfHours, selfMinutes)
        other1 = Time(otherHours, otherMinutes)
        short = self1.shortHelp(other1)

        self2 = Time(selfHours, selfMinutes)
        other2 = Time(otherHours, otherMinutes)
        long = self2.longHelp(other2)
        
        if short.isBefore(long):
            return short
        return long

    def longHelp(self, other):
        if self == other:
            return Time(0, 0)
        elif not self.isBefore(other):
            return other.longHelp(self)
        mins = 0
        hours = 0
        while self != other:
            self.tick()
            mins += 1
            if mins == 60:
                hours += 1
                mins = 0
        return Time(hours, mins)

    def longTimeApart(self, other):
        selfHours = self.hours
        selfMinutes = self.minutes
        otherHours = other.hours
        otherMinutes = other.minutes

        self1 = Time(selfHours, selfMinutes)
        other1 = Time(otherHours, otherMinutes)
        short = self1.shortHelp(other1)

        self2 = Time(selfHours, selfMinutes)
        other2 = Time(otherHours, otherMinutes)
        long = self2.longHelp(other2)
        
        if not short.isBefore(long):
            return short
        return long

t = Time(12,1)
str(t)
print(t)

t2 = Time(17, 59)
print(t2)

print(t == t2)

print(t.isAfterNoon())
print(t2.isAfterNoon())

print(t.isBefore(t2))
print(t2.isBefore(t))

t3 = Time(23, 59)
t3.tick()
print(t3)

t4 = Time(0, 1)
t4.tick()
print(t4)

print("t5")
t5 = Time(23, 59)
t6 = Time(0, 1)
print(t5.shortTimeApart(t6)) # 0:02
print(t6.shortTimeApart(t5)) # 0:02

print("t7")
t7 = Time(0, 0)
t8 = Time(23, 59)
print(t8.longTimeApart(t7)) # 23:59

print("t9")
t9 = Time(13,00)
t10 = Time(13, 30)
print(t9.shortTimeApart(t10)) # 0:30

print("t11")
t11 = Time(13,00)
t12 = Time(13, 30)
print(t11.longTimeApart(t12)) # 23:30

print("t13")
t13 = Time(13,00)
t14 = Time(13, 00)
print(t13.shortTimeApart(t14)) # 0:00