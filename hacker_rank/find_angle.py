#Calculate the hypotenuse
import math

#GET THE ANGLE
import math
#RIGHT ANGLE TRIANGLE ONLY
"""


M = midpoint of hypotenuse (AC)

AB = length
BC = Length

So 1 ) calculate hypotenuse from AB BC

2) Calculate midpoint of hyptoenuse

3) calculkate angle - HOW?



Find mid point of hypotenuise
multiple with BC
then find angle

"""


# # 1)
a = 10
b = 10
a2 = a **2
print 'a2= ', a2
b2 = a **2
# #c = hyptoenuse
c = (a**2) + (b**2)
print 'c2=', c
c = math.sqrt(c)
print 'hypotenuse', c
mid_hypotenuse = c /float(2)
print 'mid hypot', mid_hypotenuse

print mid_hypotenuse # for original triangle and new Hypotenuse = MC

#MBC = mid_hypotenuse * b
#print "MBC= " , MBC

##Calulating angle

#1) c2 = b2 + a2 -2abcosC
#2) cosC = a2 + b2 -c2  / 2ab

#1)
print "workign out angle"
csquared = mid_hypotenuse **2 + b**2 - 2 * mid_hypotenuse * b
print 'c2', csquared
#csquared = b2 + a2
cos_c = a2 + b2 - csquared / float(2 * a * b)
print cos_c
print math.acos(cos_c)
#matchcos = math.acos(5)
#print

# # Sin (x) = Opposite / Hypotenuse = 2.5 / 5 = 0.5
#
# angle = math.cos
# #  a2 +b2 - c / 2*(a*b)
# print a2 +b2 - c / 2*a*b

# math.acos(x)
# tan()Opposite / Adjacent

#mathcos = math.cos(a / float(b))
#print math.degrees(mathcos)