class aptUnit:
    num_of_units_occupied = 0

    def __init__(self, rent, tenants=None):
        self.rent = rent
        if tenants == None:
            self.tenants = []
        else:
            self.tenants = tenants
        
    @staticmethod
    def totalRent(rent, utilities):
        rent = rent[0].amount
        utils = utilities
        return rent + utils

class oneBedUnit(aptUnit):
    nbeds = 1

    def __init__(self, unitNo, rent, tenants):
        super().__init__(rent, tenants)
        self.unitNo = unitNo
        self.isOccupied = True

class twoBedUnit(aptUnit):
    nbeds = 2

    def __init__(self, unitNo, rent, tenants):
        super().__init__(rent, tenants)
        self.unitNo = unitNo
        self.isOccupied = True

class Tenant:

    #movein and only for family heads
    def __init__(self, name, age, gender, movein=None, isFamilyHead=False):
        self.name = name
        self.age = age
        self.gender = gender
        if isFamilyHead:
            self.movein = movein

class Rent:
    def __init__(self, unitNo, amount, datePaid, month, year):
        self.unitNo = unitNo
        self.amount = amount
        self.datePaid = datePaid
        self.rmonth = month
        self.ryear = year

    
    def toString(self):
        return f"Unit No: {self.unitNo}\nRent amount: {self.amount}\nRent Paid Date: {self.datePaid}\nPaid for Month: {self.rmonth}"

class Monthly_utilities:
    ebcommon = 0
    def __init__(self, eb, water, maint, misc):
        self.eb = eb
        self.water = water
        self.maint = maint
        self.misc = misc
        self.utilsTotal = self.water + self.maint + self.misc

    def toString(self):
        return f"EB: {self.eb}\nWater: {self.water}\nMaintenace: {self.maint}\nMiscellaneous: {self.misc}"
    
import datetime
movein = datetime.date(2019,11,1)

v = Tenant('Vijay', 23, 'M', movein, True) #movein and only for family heads
j = Tenant('Jeevitha', 23, 'F')
u1 = twoBedUnit(1,11000,[v,j])
#rent details
rentdate = datetime.date(2019,12,1)
r1 = Rent(1,11000,rentdate,2,2025)
#monthly utilities
mu1 = Monthly_utilities(250.23,300,125,0)
u1.rent=[]
u1.rent.append(r1)
u1.utilities=[]
u1.utilities.append(mu1)
u1.totalRent = aptUnit.totalRent(u1.rent, u1.utilities)

print(u1.isOccupied)
print(u1.tenants[0].name)
print(u1.totalRent)
print(u1.rent[0].toString())
print(mu1.toString())




# u2 = oneBedUnit(2,7000,['g','l'])
# u3 = twoBedUnit(3,11000,['d','p'])
# u4 = twoBedUnit(4,9500,['n','k'])
# u5 = oneBedUnit(5,6800,['i'])
# u6 = twoBedUnit(6,10800,['s','k'])
# u7 = twoBedUnit(7,9800,['d','p'])
# u8 = oneBedUnit(8,7000,['m'])


