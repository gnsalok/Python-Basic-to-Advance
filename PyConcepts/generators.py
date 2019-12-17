'''
Python generators are a simple way of creating iterators.
We have to use yield keyword insted of return statement.
This function return object.
'''


# def square(nums):
#     for i in nums:
#             #after executing thread go back to main call
#         yield i*i


# numbers = square([1, 2, 3, 4, 5])

# for num in numbers:
#     print(num)

# print(next(numbers))
# print(next(numbers))
# print(next(numbers))
# print(next(numbers))
# print(next(numbers))
# print(next(numbers))


def cube(list):
    for i in list:
        yield i*i*i


li=[1,2,3,4,5,6]
c=cube(li)



for i in c:
    print(i)
