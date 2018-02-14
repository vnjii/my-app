# fruits = ['apples','banana', 'orange', 'strawberry']
# vegetables = ['lettuce', 'cucmber', 'carrots']
#
# fruits_and_vegetables = fruits + vegetables
# print fruits_and_vegetables
#
#
# drawer = ['documents', 'envelopes', 'pens']
# #access the drawer with index of 0 and print value
# print drawer[0]  #prints documents
# #access the drawer with index of 1 and print value
# print drawer[1] #prints envelopes
# #access the drawer with index of 2 and print value
# print drawer[2] #prints pens
#
#
# x = [1,2,3,4,5]
# x.append(99)
# print x
# #the output would be [1,2,3,4,5,99]
# age = 15
# if age >= 18:
#   print 'Legal age'
# else:
#   print 'You are so young!'
# if age >= 18:
#   print 'Legal age'
# elif age == 17:
#   print 'You are seventeen.'
# else:
#   print 'You are so young!'
#
# for count in range(0,5):
#     print "looping -", count
# name = Charles

def add(a,b):
 x = a + b
 return x
result =add(3,5)
print result

def say_hi(name):
    print "Hi," + name
say_hi("Michael")
