smallNumbers = [
    "zero", "one", "two", "three", "four", "five",
    "six", "seven", "eight", "nine", "ten",
    "eleven", "twelve", "thirteen", "fourteen", "fifteen",
    "sixteen", "seventeen", "eighteen", "nineteen"
]

mediumNumber = [
    "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"
]

semiBigNumber = [
    "hundred", "thousand", "million"
]

num = input("Enter number ")
nums = int(num)
res = ""
numLength = str(nums).__len__()


def getSmallNumber(smallNumber=nums):
    if 20 > smallNumber > 0:
        for i, j in enumerate(smallNumbers):
            if smallNumber == i:
                return j
    else:
        return ""


def getMiddleNumber(middleNumber=nums):
    try:
        starting = int(str(middleNumber)[0])
        ending = int(str(middleNumber)[1])
        return mediumNumber[starting - 2] + " " + str(getSmallNumber(ending))
    except:
        return getSmallNumber(int(middleNumber))


def getBigNumberValue(numberLen):
    """used to get hundreds, thousand etc etch"""
    if numberLen <= 3:
        return semiBigNumber[0]
    else:
        """numbers in maths have a pattern
            1000 -4
            10000 -5
            100000 -6
            1000000 -7
            10000000 -8
            100000000 -9
            so three is a constant that moves the value to a higher plane
            using three as the constant for division gives us a number
        """
        testing = numberLen / 3
        strRep = str(testing)
        if strRep[strRep.__len__() - 1: strRep.__len__()] == "0":
            testing = int(testing) - 2
        else:
            testing = int(testing)

        return semiBigNumber[testing]


def getHundreds(number):
    str_to_be_printed = ''
    """get the number length as it would be used for substring the number to pull out the char values"""
    numberLength = str(number).__len__()

    """loop trhough the number"""
    for i in range(numberLength):
        """if i == len - 2, e.g in the no 102, this would be '02' which would be passed to middleNumber"""
        if i == numberLength - 2:
            """tempno is the substring value of -2 length e.g 02 from 102"""
            temp_no = int(str(number)[i:numberLength])
            middleNumber = getMiddleNumber(temp_no)
            """if midle number is blank skip"""
            if middleNumber != "":
                str_to_be_printed += " and "
                str_to_be_printed += middleNumber

        """if i == 0, loop at the beginning to get the first value e.g 102 = '1' which means one hundred """
        if i == 0:
            """get the small number value of the first e.g 102 = '1', [one hundred]"""
            smallNumber = getSmallNumber(int(str(number)[i]))
            if smallNumber != "":
                str_to_be_printed += smallNumber + " "
                """get big number value gets the number significance e.g 'hundred', 'thousand' based on length of the number"""
                str_to_be_printed += getBigNumberValue(numberLength)
    return str_to_be_printed


def getAbove(number):
    """get above handles from 1k down wards"""
    """it counts from back to from e.g 1000 = 000|1, 3000000 = 000|000|3"""
    result = []
    """valid paths divides the number by three and rounds up to the nearst whole no
        e.g 1000 returns 1 valid path as there is 1|000|
        10000 returns 1 als valid path = 10|000
        100000 returns 2 as valid paths = 100|000
        valid paths is then used to loop through the number length in 3's getting their values 
        in hundreds
    """
    valid_paths = int(numLength / 3)
    """remainder is for values like 1000 as the valid path is just 1, and the length is 4, 
    so therefore there is a remainder of one.
    in this instance if the valid path's hundred is returned, the remainder is used to determine
     the thousand i.e 1000 = 1|000(hundred), |1| = thousand
    one thousand
    """
    remainder = numLength % 3

    """to substring acurately, the counter_For_Valid_paths is used to multiply 3's 
    to get the values in the number in 3's 
    """
    counter_for_valid_paths = 1
    str_r = ''
    for i in range(valid_paths):
        """if i is 0, then it is in the initial stage pull out from the len - (3 * CFVP)
        e.g if len is 4(1000) then 4 - (3 *1) assuming CFVP is still 1
        = 4 -3 == 1
        so therefore, substring from 1 - 4 which is (1000)(indexes: 0,1,2,3) 
        i.e the values of 1-2-3 would be used for hundreds
        """
        if i == 0:
            str_r += " " + getHundreds(num[numLength - (3 * counter_for_valid_paths):numLength])
            result.append(getHundreds(num[numLength - (3 * counter_for_valid_paths):numLength]))
        else:
            str_r += " " + semiBigNumber[counter_for_valid_paths - 1]
            result.append(semiBigNumber[counter_for_valid_paths - 1])

            str_r += " " + getHundreds(
                num[numLength - (3 * counter_for_valid_paths): 3 + numLength - (3 * counter_for_valid_paths)])
            result.append(getHundreds(
                num[numLength - (3 * counter_for_valid_paths): 3 + numLength - (3 * counter_for_valid_paths)]))

        # print(semiBigNumber[counter_for_valid_paths - 1])


        counter_for_valid_paths = counter_for_valid_paths + 1

    if remainder > 0:
        str_r += " " + semiBigNumber[counter_for_valid_paths - 1]
        """get the bigNoVal(hundred,thousand etc etc) for the remainder"""
        result.append(semiBigNumber[counter_for_valid_paths - 1])
        """if the subtring of the remainder is greater than twenty, 
        it is a middle number else ir is a small number
        e.g rem value = 50, 50 is greater than 20 i.e a middle number
        """
        if int(num[0:remainder]) < 20:
            str_r += " " + getSmallNumber(int(num[0:remainder]))
            res = getSmallNumber(int(num[0:remainder]))
        else:
            str_r += " " + getMiddleNumber(int(num[0:remainder]))
            res = getMiddleNumber(int(num[0:remainder]))
        result.append(res)

    FinalPrint = ''
    for s in result.__reversed__():
        FinalPrint += s + ' '
    print(FinalPrint, 'dollars')


if nums >= 20:
    if numLength == 2:
        print(getMiddleNumber(nums), 'dollars')
    elif numLength == 3:
        print(getHundreds(nums), 'dollars')
    elif numLength > 3:
        getAbove(nums)
else:
    if getSmallNumber() != "":
        print(getSmallNumber(), 'dollars')
    else:
        print("zero")
