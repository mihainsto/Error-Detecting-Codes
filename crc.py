def crc_remainder(input_bitstring, polynomial_bitstring):
    print("Input String: " + str(input_bitstring))
    print("Polynom: " + str(polynom))

    print("Starting Algorithm!")
    print("Bitstring:")
    print(' '.join(list(input_bitstring)))
    print("The first step is to add padding, we will add " + str(len(polynomial_bitstring)-1) + " bits of padding")
    polynomial_bitstring = polynomial_bitstring.lstrip('0')
    len_input = len(input_bitstring)
    initial_padding = "0" * (len(polynomial_bitstring) - 1)
    input_padded_array = list(input_bitstring + initial_padding)
    print("Added padding, now starting algorithm!")
    print(' '.join(input_padded_array))
    while '1' in input_padded_array[:len_input]:
        cur_shift = input_padded_array.index('1')
        print(' '*2*cur_shift+' '.join(list(polynomial_bitstring)))
        for i in range(len(polynomial_bitstring)):
            input_padded_array[cur_shift + i] = str(int(polynomial_bitstring[i] != input_padded_array[cur_shift + i]))
        print(' '.join(input_padded_array))

    return ''.join(input_padded_array)[len_input:]


def crc_check(input_bitstring, polynomial_bitstring, check_value):
    print("Input String: " + str(input_bitstring))
    print("Polynom: " + str(polynom))

    print("Starting Algorithm!")
    print("Bitstring:")
    print(' '.join(list(input_bitstring)))
    print("The first step is to add the CRC as padding")
    
    polynomial_bitstring = polynomial_bitstring.lstrip('0')
    len_input = len(input_bitstring)
    initial_padding = check_value
    input_padded_array = list(input_bitstring + initial_padding)
    print("Added padding, now starting algorithm!")
    print(' '.join(input_padded_array))
    while '1' in input_padded_array[:len_input]:
        cur_shift = input_padded_array.index('1')
        print(' '*2*cur_shift+' '.join(list(polynomial_bitstring)))
        for i in range(len(polynomial_bitstring)):
            input_padded_array[cur_shift + i] = str(int(polynomial_bitstring[i] != input_padded_array[cur_shift + i]))
        print(' '.join(input_padded_array))
        
    return ('1' not in ''.join(input_padded_array)[len_input:])

string_input = '11010011101100'
polynom = '1011'
print("Solver of CRC from Computer Networks exam:")
print("Choose an option:")
print("0 for computing CRC")
print("1 for checking CRC")
option = input()
if option == '0':
    print("Type the input bitstring:")
    string_input = input()
    print("Type the polynom: ")
    polynom = input()
    crc = crc_remainder(string_input, polynom)
    print("The CRC IS:")
    print(crc)
elif option == '1':
    print("Type the input bitstring:")
    string_input = input()
    print("Type the polynom: ")
    polynom = input()
    print("Type the CRC: ")
    crc = input()
    check = crc_check(string_input, polynom, crc)
    print(check)
else:
    print("Wrong option")
