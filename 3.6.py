# This is Problem 6

import math
# Imports the math class
print "Initiate brute force method'\n'"

origin = (0,0,0)
point1 = [20.900,15.300,20.400]
point2 = [0.600,34.700,8.100]
point3 = [12.100,15.800,2.300]
point4 = [15.000,5.800,16.900]


distance1 = math.sqrt(sum([(point1[0]) ** 2 + (point1[1]) ** 2 + (point1[2]) ** 2]))
print "Euclidean distance from point 1 to origin is: ", distance1

distance2 = math.sqrt(sum([(point2[0]) ** 2 + (point2[1]) ** 2 + (point2[2]) ** 2]))
print "Euclidean distance from point 2 to origin is: ", distance2

distance3 = math.sqrt(sum([(point3[0]) ** 2 + (point3[1]) ** 2 + (point3[2]) ** 2]))
print "Euclidean distance from point 3 to origin is: ", distance3

distance4 = math.sqrt(sum([(point4[0]) ** 2 + (point4[1]) ** 2 + (point4[2]) ** 2]))
print "Euclidean distance from point 4 to origin is: ", distance4

minimum = min(distance1, distance2, distance3, distance4)
print "'\n'The shortest distance from the origin is to", min(distance1, distance2, distance3, distance4)
if minimum == distance1:
    print "Which is Point 1"
elif minimum == distance2:
    print "Which is Point 2"
elif minimum == distance3:
    print "Which is Point 3"
elif minimum == distance4:
    print "Which is Point 4"

# This is part 2
apart1 = math.sqrt(sum([(point1[0]-point2[0]) ** 2 + (point1[1]-point2[1]) ** 2 + (point1[2]-point2[2]) ** 2]))
print "'\n''\n'Euclidean distance from point 1 to point 2 is: ", apart1

apart2 = math.sqrt(sum([(point1[0]-point3[0]) ** 2 + (point1[1]-point3[1]) ** 2 + (point1[2]-point3[2]) ** 2]))
print "'\n'Euclidean distance from point 1 to point 3 is: ", apart2

apart3 = math.sqrt(sum([(point1[0]-point4[0]) ** 2 + (point1[1]-point4[1]) ** 2 + (point1[2]-point4[2]) ** 2]))
print "'\n'Euclidean distance from point 1 to point 4 is: ", apart3

apart4 = math.sqrt(sum([(point2[0]-point4[0]) ** 2 + (point2[1]-point4[1]) ** 2 + (point2[2]-point4[2]) ** 2]))
print "'\n'Euclidean distance from point 2 to point 4 is: ", apart4

apart5 = math.sqrt(sum([(point2[0]-point3[0]) ** 2 + (point2[1]-point3[1]) ** 2 + (point2[2]-point3[2]) ** 2]))
print "'\n'Euclidean distance from point 2 to point 3 is: ", apart5

apart6 = math.sqrt(sum([(point3[0]-point4[0]) ** 2 + (point3[1]-point4[1]) ** 2 + (point3[2]-point4[2]) ** 2]))
print "'\n'Euclidean distance from point 3 to point 4 is: ", apart6

min_apart = min(apart1, apart2, apart3, apart4, apart5, apart6)


if min_apart == apart1:
    print "'\n'Point 1 is closest to Point 2"
elif min_apart == apart2:
    print "'\n'Point 1 is closest to Point 3"
elif min_apart == apart3:
    print "'\n'Point 1 is closest to Point 4"
elif min_apart == apart4:
    print "'\n'Point 2 is closest to Point 4"
elif min_apart == apart5:
    print "'\n'Point 2 is closest to Point 3"
elif min_apart == apart6:
    print "'\n'Point 3 is closest to Point 4"
print "They are only", min_apart, "units apart"
