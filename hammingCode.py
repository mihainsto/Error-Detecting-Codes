def generate_array(bitstring):
    arr=[]
    arr.append('inf')
    arr.append('inf')
    p2 = 4
    i = 3
    for item in bitstring:
        if i != p2:
            arr.append(item)
            i += 1
            continue
        if i == p2:
            arr.append('inf')
            arr.append(item)
            p2 *= 2
            i += 2
            continue
    return arr
        


def hamming_code(bitarr):
    print(' '.join(bitarr))
    print("Starting algorithm: ")
    print(" ")
    print(" ")
    for i in range(len(bitarr)):
        if bitarr[i] == 'inf':
            positions = []
            print("We update the party bit from the index " + str(i+1))
            bitarr[i] = 0
            k = i+1
            sm = 0
            # making parity
            j = i-1
            while j < len(bitarr):
                j += 1
                for l in range(j, j+k):
                    try:
                        sm += int(bitarr[l])
                        positions.append(l)
                    except:
                        break
                j = j+2*k-1
            print("This bit will contain the parity of the sum of bits on indices: " + str(positions))
            if sm % 2 == 0:
                bitarr[i] = '0'
                print("The sum is even!")
            else:
                bitarr[i] = '1'
                print("The sum is odd!")
            print("The updated bitstring: ")
            print(" ".join(bitarr))
            print(" ")

    return bitarr

def fix_error(hamming):
    print(" ")
    print(" ")
    print("Starting algorithm: ")
    bitarr = []
    p2 = 4
    bitarr.append('inf')
    bitarr.append('inf')
    for i in range(2, len(hamming)):
        if i == p2-1:
            bitarr.append('inf')
            p2 *= 2
        else:
            bitarr.append(hamming[i])
    failed_checks = []

    for i in range(len(bitarr)):
        if bitarr[i] == 'inf':
            positions = []
            print("We compute the party bit from the index " + str(i+1))
            bitarr[i] = 0
            k = i + 1
            sm = 0
            # making parity
            j = i - 1
            while j < len(bitarr):
                j += 1
                for l in range(j, j + k):
                    try:
                        sm += int(bitarr[l])
                        positions.append(l)
                    except:
                        break
                j = j + 2 * k - 1
            print("This bit will contain the parity of the sum of bits on indices: " + str(positions))
            print("The computed bit is: " + str(sm % 2))
            print("The actual bit is : " + str(hamming[i]))
            if sm % 2 == 0:
                if hamming[i] != '0':
                    failed_checks.append(int(i+1))
                    print("The check has failed, appending to failed checks list.")
            else:
                if hamming[i] != '1':
                    print("The check has failed, appending to failed checks list.")
                    failed_checks.append(int(i+1))
            print("Failed checks list: ")
            print(str(failed_checks))
            print(" ")

    if len(failed_checks) == 0:
        print(" ")
        print("We encountered 0 failed checks.")
        print("The hamming code is correct!")
        return hamming
    wrong_bit = sum(failed_checks)
    print(" ")
    print("Computing the wrong bit (sum of failed checks bits).")
    print("wrong bit: " + str(wrong_bit))
    wrong_bit -= 1
    print("Fixing the wrong bit.")
    if hamming[wrong_bit] == '1':
        hamming[wrong_bit] = '0'
    else:
        hamming[wrong_bit] = '1'
    return hamming

def calculate_hamming(test_string):
    print("The initial bitstring is: ")
    print(" ".join(list(test_string)))
    print("The first step is to add the parity bits.")
    bitarr = generate_array(test_string)
    print("The bitstring with the parity bits added is:")
    print(" ".join(bitarr))
    print("Now we update the inf with the partity.")
    hamming = hamming_code(bitarr.copy())
    print(" ")
    print(" ")
    print("Hamming code: ")
    print(" ".join(hamming))
    return hamming

# 10011010
print("Solver of CRC from Computer Networks exam:")
print("Choose Option:")
print("0 for computing hamming code for a given bitstring")
option = input()
if option == '0':
    print("Type the bitstring: ")
    bitstring = input()
    hamming = calculate_hamming(bitstring)

    print(" ")
    print(" ")
    print("Choose an option:")
    print("0 for altering a bit of the hamming code and checking + fixing")
    print("1 for checking the hamming code")
    noption = input()
    if noption == '0':
        print("Type the index of the bit you want to switch: (starting from 1)")
        ind = int(input())
        ind -= 1
        if hamming[ind] == '0':
            hamming[ind] = '1'
        else:
            hamming[ind] = '0'
        print("Altered hamming code: ")
        print(" ".join(hamming))

        print("Checking and fixing the hamming code:")
        new_hamming = fix_error(hamming)
        print("The fixed hamming code is: ")
        print(" ".join(new_hamming))
    elif noption == '0':
        print("Checking the hamming code: ")
        new_hamming = fix_error(hamming)
        print("The hamming code is: ")
        print(" ".join(new_hamming))
    else:
        print("Wrong option")
else:
    print("Wrong option")
