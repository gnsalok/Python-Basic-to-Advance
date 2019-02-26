

def square(nums):
    for i in nums:
            #after executing thread go back to main call
        yield i*i


numbers = square([1, 2, 3, 4, 5])

for num in numbers:
    print(num)


# print(next(numbers))
# print(next(numbers))
# print(next(numbers))
# print(next(numbers))
# print(next(numbers))
# print(next(numbers))
