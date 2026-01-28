

def ceaser_cypher(string_to_shift , shift , direction):
    encrypted_string =[]
    shft = shift
    if direction == 1:
        shft = -shift
    else:
        pass
    print(shft)
    for i in string_to_shift:
        ascii_char =ord(i)
        shifted_char = chr(ascii_char+shft)
        encrypted_string.append(shifted_char)

    return ''.join(encrypted_string)



while True:
    shift = int(input('Enter the number of to shift: '))
    string_to_shift = input('Enter the string to shift: ')
    direction = int(input("Do you want to encrypt or decrypt?( 0 to incrypt and 1 do decrypt) "))

    shifted_string = ceaser_cypher(string_to_shift , shift , direction)
    print('Your required string is : ' , shifted_string)

    choice = input('Do you want to continue (Y or N):').lower()
    if choice == 'y':
        print('OK!')
    else:
        print('See ya SUcker!!!!')
        break

    

