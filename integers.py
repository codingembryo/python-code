#License: https://bit.ly/3oLErEI

#Write a Python program to test a list of one hundred integers between 0 and 999,which all differs by ten from one another.Return True or False
def test(li):
    return all(i in range(1000) and abs(i - j) >= 10 
    for i in li for j in li if i != j) and len(set(li)) == 100
nums = list(range(0, 1000, 10))
print("Original list:")
print(nums)
# print("Check whether the said list contains one hundred integers between 0 and 999 which all differ by ten from one another:")
print(test(nums))
nums = list(range(0, 1000, 20))
print("Original list:")
print(nums)
# print("Check whether the said list contains one hundred integers between 0 and 999 which all differ by ten from one another:")
# print(test(nums))
