import wod_dict_en as txt

PHY = 'physical'
MEN = 'mental'
SOC = 'social'


class Character:
    pass
    # self.name
    # self.age
    # self.player
    # self.concept
    # self.virtue
    # self.vice
    # self.chronicle

class Trait(Character):

    @property
    def value(self):
        return self.dots
        
    @property
    def name(self):
        return txt.WOD[self.key][0]
    
    @property
    def description(self):
        return txt.WOD[self.key][1]    
        
    def up(self):
        if 0<=self.dots<=3:
            cost=1
        elif self.dots==4:
            cost=2
        else:
            print('no on up')
            return
            
        if self.type == PHY:
            temp=(self.phy, self.soc, self.men, self.breaks)
        elif self.type == SOC:
            temp=(self.soc, self.phy, self.men, self.breaks)
        elif self.type == MEN:
            temp=(self.men, self.soc, self.phy, self.breaks)
            
        if self.abscheck(*temp, cost):
            self.dots+=1
            self.points(self.type, 'min', cost)

    def down(self):
        if self.breaks[0]<self.dots<5:
            cost=1
        elif self.dots==5:
            cost=2
        else:
            print('no on down')
            return

        self.dots-=1
        self.points(self.type, 'pl', cost)
 
    @classmethod
    def points(cls, type, min_pl, cost):
        
        if type == PHY:
            if min_pl == 'min':
                cls.phy+=cost
            else:
                cls.phy-=cost
                
        elif type == SOC:
            if min_pl == 'min':
                cls.soc+=cost
            else:
                cls.soc-=cost
                
        elif type == MEN:
            if min_pl == 'min':
                cls.men+=cost
            else:
                cls.men-=cost
        print('points spent:\nmental:', cls.men, '\nsocial:', cls.soc, '\nphysical:', cls.phy)

    
    @staticmethod
    def abscheck(x, y, z, breaks, cost):
        fix=1 if cost==2 else 0
        if x >= breaks[3]-fix:
            print('max', x, 'vs', breaks[3])
            return False
        elif (y > breaks[2]) or (z > breaks[2]) and (x >= breaks[2]-fix):
            print('max', x, y, z, 'vs', breaks[2])
            return False
        elif (y > breaks[1]) and (z > breaks[1]) and (x >= breaks[1]-fix):
            print('max', x, y, z, 'vs', breaks[1])
            return False
        return True


class Attribute(Trait):
    breaks=1,3,4,5
    phy=0
    men=0
    soc=0
    
    def __init__(self, type, key):
        self.dots=1
        self.type=type
        self.key=key

class Skill(Trait):
    breaks=0,5,7,11
    phy=0
    soc=0
    men=0
    
    specialties=3
    
    def __init__(self, type, key):
        self.specialty=set()
        self.dots=0
        self.type=type
        self.key=key
        
    @property
    def value(self):
        if self.type == MEN and self.dots == 0:
            print('men -3')
            return -3
        elif (self.type == SOC or self.type == PHY) and self.dots == 0:
            print('soc or phy -1')
            return -1
        else:
            print('dots != 0')
            return self.dots
        
        
    def mkspec(self, title):
        if Skill.specialties>0:
            self.specialty.add(title)
            Skill.specialties-=1
        else: print('no on mkspec')
    
    def rmspec(self, title):
        if title in self.specialty:
            self.specialty.remove(title)
            Skill.specialties+=1
        else: print('no on remspec')
        
class Clan(Character):
    pass
class Dependable(Character):
    pass
class Discipline(Trait):
    pass
class Merit(Trait):
    pass
class Flaw(Trait):
    pass
class Inventory(Character):
    pass

Str = Attribute(PHY, "Str")
Dex = Attribute(PHY, "Dex")
Sta = Attribute(PHY, "Sta")

Pre = Attribute(SOC, "Pre")
Man = Attribute(SOC, "Man")
Com = Attribute(SOC, "Com")

Int = Attribute(MEN, "Int")
Wit = Attribute(MEN, "Wit")
Res = Attribute(MEN, "Res")

ath = Skill(PHY, "ath")
bra = Skill(PHY, "bra")
dri = Skill(PHY, "dri")
fir = Skill(PHY, "fir")
lar = Skill(PHY, "lar")
ste = Skill(PHY, "ste")
sur = Skill(PHY, "sur")
wea = Skill(PHY, "wea")

aca = Skill(MEN, "aca")
com = Skill(MEN, "com")
cra = Skill(MEN, "cra")
inv = Skill(MEN, "inv")
med = Skill(MEN, "med")
occ = Skill(MEN, "occ")
pol = Skill(MEN, "pol")
sci = Skill(MEN, "sci")

ani = Skill(SOC, "ani")
emp = Skill(SOC, "emp")
exp = Skill(SOC, "exp")
int = Skill(SOC, "int")
per = Skill(SOC, "per")
soc = Skill(SOC, "soc")
str = Skill(SOC, "str")
sub = Skill(SOC, "sub")


