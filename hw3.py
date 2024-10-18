# Q1
x = 2
y = 3
def computePower(x, y):
    result = 1
    for _ in range(y):
        result *= x
    return result

print(computePower(x, y))

# Q2
readings = [15, 14, 17, 20, 23, 28, 20]
def temperatureRange(readings):
    return (min(readings),max(readings))

print(temperatureRange(readings))

# Q3
def isWeekend(day):
    return day == 6 or day == 7

day = 6
print(isWeekend(day))

# Q4
distance = 70 # miles
fuel = 21.5 # gallons
def fuel_efficiency(distance, fuel):
    result = distance / fuel
    return result

print(fuel_efficiency(distance, fuel))

# Q5
n = 12345
def decodeNumbers(n):
    last_digit = n % 10
    remaining_number = n // 10
    num_digits = 0
    temporary = remaining_number
   
    while temporary > 0:
        temporary //= 10
        
        num_digits += 1
    
    result = last_digit * (10 ** num_digits) + remaining_number
    return result

print(decodeNumbers(n))

# Q6.1
nums = [2024, 98, 131, 2, 3, 72]
def find_min_with_for_loops(nums):
    min_num = float('inf')
    for num in nums:
        if num < min_num:
            min_num = num
    return min_num

def find_max_with_for_loops(nums):
    max_num = float('-inf')
    for num in nums:
        if num > max_num:
            max_num = num
    return max_num

print(find_min_with_for_loops(nums))
print(find_max_with_for_loops(nums))

# Q6.2
nums = [2024, 98, 131, 2, 3, 72]
def find_min_with_while_loop(nums):
    min_num = nums[0]
    index = 1
    while index < len(nums):
        if nums[index] < min_num:
            min_num = nums[index]
        index += 1
    return min_num

def find_max_with_while_loop(nums):
    max_num = nums[0]
    index = 1
    while index < len(nums):
        if nums[index] > max_num:
            max_num = nums[index]
        index += 1
    return max_num

print(find_min_with_while_loop(nums))
print(find_max_with_while_loop(nums))

# Q7
text = "UC Berkeley, founded in 1868!"
def vowel_and_consonant_count(text):
    vowels = "aeiouAEIOU"
    vowel_count = 0
    consonant_count = 0

    for char in text:
        if char.isalpha():
            if char in vowels:
                vowel_count += 1
            else:
                consonant_count += 1

    return (vowel_count, consonant_count)

print(vowel_and_consonant_count(text))

# Q8
num = 2468
def digital_root(num):
    digit_sum = 0
    for digit in str(num):
        digit_sum += int(digit)
    
    while digit_sum >= 10:
        digit_sum = sum(int(d) for d in str(digit_sum))

    return (digit_sum, digit_sum)

print(digital_root(num))