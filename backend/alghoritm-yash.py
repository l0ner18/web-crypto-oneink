from tkinter import *
import sys

def Decimal_number(number):
    x=''
    decimal_number = number
    if decimal_number != '':
        decimal_number = int(decimal_number)
        binary_representation = bin(int(decimal_number))[2:]
        if len(binary_representation) < 16:
            x = '0' * (16 - len(binary_representation)) + binary_representation
        else:
            x = binary_representation
    return x

def Decimal_number_key(key):
    k=''
    decimal_number_key = key
    if decimal_number_key != '':
        decimal_number_key = int(decimal_number_key)
        binary_representation = bin(decimal_number_key)[2:]
        if len(binary_representation) < 24:
            k = '0' * (24 - len(binary_representation)) + binary_representation
        
    return k

def permutation_with_expansion(data_for_permutation, keyE1): #перестановка с расширением
    result = ''
    for i in range(0, 12):
        result = result + data_for_permutation[int(keyE1[i]) - 1]
    return result

def summ_with_key(data, key):
    result = ''
    for i in range(0, 12):
        if data[i] == key[i]:
            result += "0"
        else:
            result += "1"
    return result

def summ_with_left_side(left_side, data):
    result = ''
    for i in range(0, 8):
        if data[i] == left_side[i]:
            result += "0"
        else:
            result += "1"
    return result

def permutation(data, key):
    result = ''
    for i in range(0, 8):
        result = result + data[int(key[i]) - 1]
    return result

def Answer(data, key):
    x = data
    k = key
    dict1 = {
        '0000': '100', '0001': '110', '0010': '001', '0100': '101',
        '0011': '011', '0111': '101', '0101': '111', '0110': '010',
        '1000': '101', '1001': '111', '1010': '010', '1100': '110',
        '1011': '100', '1111': '110', '1101': '001', '1110': '011'
    }
    dict2 = {
        '0001': '101', '0010': '111', '0000': '011', '0011': '010',
        '0101': '110', '0110': '001', '0111': '111', '0100': '100',
        '1001': '110', '1010': '001', '1000': '100', '1011': '011',
        '1101': '111', '1110': '010', '1111': '001', '1100': '101'
    }
    dict3 = {
        '0001': '10', '0010': '11', '0000': '01', '0011': '01',
        '0101': '11', '0110': '01', '0111': '10', '0100': '10',
        '1001': '01', '1010': '10', '1000': '11', '1011': '11',
        '1101': '10', '1110': '11', '1111': '01', '1100': '01'
    }

    k1 = k[:12]
    k2 = k[6:18]
    k3 = k[12:24]

    left_side = str(x[:8])
    data_for_permutation = str(x[8:] * 2)

    keyE1 = "341268573824"
    keyE2 = "87325416"

    f3_1 = ""

    f1_1 = permutation_with_expansion(data_for_permutation, keyE1) #перестановка с расширением
    f2_1 = summ_with_key(f1_1, k1) #сумма с ключем
    f3_1 = f3_1 + dict1[f2_1[:4]] + dict2[f2_1[4:8]] + dict3[f2_1[8:]] #поиск по таблицам 3956874
    f4_1 = permutation(f3_1, keyE2) #перестановка
    f5_1 = summ_with_left_side(left_side, f4_1) #сложение с левой частью

    x1 = str(x[8:])
    x2 = f5_1
    f3_2 = ""

    f1_2 = permutation_with_expansion(x2, keyE1) #перестановка с расширением
    f2_2 = summ_with_key(f1_2, k2) #сумма с ключем
    f3_2 = f3_2 + dict1[f2_2[:4]] + dict2[f2_2[4:8]] + dict3[f2_2[8:]] #поиск по таблицам
    f4_2 = permutation(f3_2, keyE2) #перестановка
    f5_2 = summ_with_left_side(x1, f4_2) #сложение с левой частью

    x1 = x2
    x2 = f5_2

    f3_3 = ""

    f1_3 = permutation_with_expansion(x2, keyE1) #перестановка с расширением
    f2_3 = summ_with_key(f1_3, k3) #сумма с ключем
    f3_3 = f3_3 + dict1[f2_3[:4]] + dict2[f2_3[4:8]] + dict3[f2_3[8:]]
    f4_3 = permutation(f3_3, keyE2) #перестановк
    f5_3 = summ_with_left_side(x1, f4_3) #сложение с левой частью

    answer = f5_3 + x2
    answer_final = (int(answer, 2))
    return answer_final

key = Decimal_number(sys.argv[1])
data = Decimal_number_key(sys.argv[2])

result = Answer(key, data)
print(result)