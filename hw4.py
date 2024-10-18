#2.1
numbersList = list(range(0,21))
print(numbersList)

#2.2
def squareList(numbersList):
    return [i ** 2 for i in numbersList]

numbersSquaredList = squareList(numbersList)
print(numbersSquaredList)

#2.3
n = 15
firstFifteenList = numbersSquaredList[:n] #I was trying to get the code to work by making a for loop going through the list and returning every element until it returned the first fifteen, I couldn't figure out how to get it to work. When I was searching how to do it I found this function.
print(firstFifteenList)

#2.4
def fiveList(numbersSquaredList):
    return numbersSquaredList[0::5]    #originally I only had one ":" between the 0 and 5 so it was only giving me the first 5 elements in the list, I had to look up how to do this function to realize that I needed another ":"
everyFifthList = fiveList(numbersSquaredList)
print(everyFifthList)

#2.5
def lastThirty(numbersSquaredList):
    return numbersSquaredList[-30:][::-3] #originally I had 3 seperate functions, one for each action, like slicing the last thirty elemtents, reversing the list, then taking every third number but I felt like there must be a shorter way to do it so with the help of google I made this
lastThirtyReverseThirdsList = lastThirty(numbersSquaredList)

print(lastThirtyReverseThirdsList)

#3.1
def fiveByFive():
    matrix = []
    num = 1
    for i in range(5):
        row = []
        for j in range(5):
            num += 1  # I was getting an error here that the variable num couldn't be located, this was because I forgot to define num = 1 as I did above
            row.append(num)
        matrix.append(row)
    return matrix    
matrix = fiveByFive()
print(matrix)

#3.2
def multiplesThree(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] % 3 == 0:  # before I had it / 3 == int, meaning integer,  basically seeing if the answer was a whole number, which wasn't working, I think this is because int is treated as another variable. I then switched it out for the modulus to find when there are no remainders
                matrix[i][j] = '?'
    return matrix
matrix_modified = multiplesThree(matrix)
print(matrix_modified)

#3.3
def sum_non_question_elements(matrix_modified):
    total_sum = 0
    for i in range(len(matrix_modified)):
        for j in range(len(matrix_modified[i])):
            if matrix_modified[i][j] != '?':
                total_sum =+ matrix_modified[i][j]
    return total_sum
sum = sum_non_question_elements(matrix_modified)
print(sum) #im not sure why this isn't returning the correct value, it returns 26 instead