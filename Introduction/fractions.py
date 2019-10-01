def gcd(num, den):
    while num%den != 0:
        old_num = num
        old_den = den

        num = old_den
        den = old_num % old_den
    
    return den

def int_chk(number):
    if type(number) is int:
        return True
    else:
        raise TypeError


class Fraction():

    def __init__(self, num, den):
        # validate num, den as ints
        int_chk(num)
        int_chk(den)
        
        common_div = gcd(num, den)
        self.num = num//common_div
        self.den = den//common_div
        
    def __str__(self):
        return str(self.num) + "/" + str(self.den)
    
    def __repr__(self):
        return f'Fraction({self.num}, {self.den})'

    def show(self):
        return str(self.num) + "/" + str(self.den)

    def getNum(self):
        return self.num

    def getDen(self):
        return self.den

    def __add__(self, other_fraction):
        #check for whole number instead of fraction
        if type(other_fraction) == int:
            new_num = self.num  + self.den * other_fraction
            new_den = self.den 
        else:
            new_num = self.num * other_fraction.den + self.den * other_fraction.num
            new_den = self.den * other_fraction.den

        return Fraction(new_num, new_den)

    # Implement add classes
    __radd__ = __add__
    __iadd__ = __add__
    

    def __sub__(self, other_fraction):
        
        new_num = self.num * other_fraction.den - self.den * other_fraction.num
        new_den = self.den * other_fraction.den
        
        return Fraction(new_num, new_den)

    def __mul__(self, other_fraction):

        new_num = self.num * other_fraction.num
        new_den = self.den * other_fraction.den

        common_div = gcd(new_num, new_den)

        return Fraction(new_num//common_div, new_den//common_div)

    def __truediv__(self, other_fraction):

        new_num = self.num * other_fraction.den
        new_den = self.den * other_fraction.num

        common_div = gcd(new_num, new_den)

        return Fraction(new_num//common_div, new_den//common_div)
        

    def __eq__(self, other_fraction):

        first_num = self.num * other_fraction.den
        second_num = self.den * other_fraction.num

        return first_num == second_num

    def __ne__(self, other_fraction):

        first_num = self.num * other_fraction.den
        second_num = self.den * other_fraction.num

        return first_num != second_num

    def __gt__(self, other_fraction):

        first_num = self.num * other_fraction.den
        second_num = self.den * other_fraction.num

        return first_num > second_num

    def __ge__(self, other_fraction):

        first_num = self.num * other_fraction.den
        second_num = self.den * other_fraction.num

        return first_num >= second_num

    def __lt__(self, other_fraction):

        first_num = self.num * other_fraction.den
        second_num = self.den * other_fraction.num

        return first_num < second_num

    def __le__(self, other_fraction):

        first_num = self.num * other_fraction.den
        second_num = self.den * other_fraction.num

        return first_num <= second_num

if __name__ == '__main__':
    f1 = Fraction(1, 2)
    f2 = Fraction(2, 3)

    print(f1/f2 == Fraction(3,4))
    print(Fraction(1,2) + 5)
    print(5 + Fraction(1,2))
   
    i = Fraction(1,3)
    i +=1
    print(i)

    print(str(i))
    print(repr(i))
