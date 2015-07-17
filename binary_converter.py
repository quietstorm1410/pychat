BINARY_DICT = {'A': '01000001', 'B': '01000010', 'C': '01000011', 'D': '01000100', 'E': '01000101',
                   'F': '01000110', 'G': '01000111', 'H': '01001000', 'I': '01001001', 'J': '01001010',
                   'K': '01001011', 'L': '01001100', 'M': '01001101', 'N': '01001110', 'O': '01001111',
                   'P': '01010000', 'Q': '01010001', 'R': '01010010', 'S': '01010011', 'T': '01010100',
                   'U': '01010101', 'V': '01010110', 'W': '01010111', 'X': '01011000', 'Y': '01011001',
                   'Z': '01011010', ' ': '00000000', '[': '01011011', '\\': '01011100', ']': '01011101',
                   '^': '01011110', '_': '01011111', '`': '01100000', '!': '00100001', '"': '00100010',
                   '#': '00100011', '$': '00100100', '%': '00100101', '&': '00100110', "'": '00100111',
                   '(': '00101000', ')': '00101001', '*': '00101010', '+': '00101011', ',': '00101100',
                   '-': '00101101', '.': '00101110', '/': '00101111', '0': '00110000', '1': '00110001',
                   '2': '00110010', '3': '00110011', '4': '00110100', '5': '00110101', '6': '00110110',
                   '7': '00110111', '8': '00111000', '9': '00111001', ':': '00111010', ';': '00111011',
                   '<': '00111100', '=': '00111101', '>': '00111110', '?': '00111111', '@': '01000000',
                   '\n': '01111111'}


def convert_to_binary(text):
    converted_text = ''
    if text != '\n': 
        text = text.rstrip('\n')
    
        for letters in text:
            letters = letters.upper()
            if BINARY_DICT.get(letters) != None:
                converted_text += BINARY_DICT.get(letters)
    else:
        converted_text += BINARY_DICT.get(text)
    return converted_text

def convert_to_text(binary_text):
    ascii = ''
    try:
        for i in range(0, len(binary_text), 8):
            if BINARY_DICT.keys()[BINARY_DICT.values().index(binary_text[i:i+8])] != None:
                ascii += BINARY_DICT.keys()[BINARY_DICT.values().index(binary_text[i:i+8])]

    except Exception:
                print 'Data not formated correctly'
                return
    return ascii

    

def save_data(data):
    print 'Would you like to save to a file?'
    answer = str(raw_input('Yes or No '))
    answer = answer.lower()

    if answer == 'yes' or answer == 'y':
        file_name = str(raw_input('Enter save location: '))
        write_file = open(file_name, 'a+')

        if data[0] == '0':
            data_type = 'BINARY\n'
            write_to_file(file_name, data_type, data)
        else:
            data_type = 'TEXT\n'
            write_to_file(file_name, data_type, data)
        
    else:
        print 'Exiting without saving'
  

    return

def write_to_file(file_name, data_type, data):
    write_file = open(file_name, 'a+')
    write_file.write(data_type)
    write_file.write(data)
    write_file.close()
    print 'Wrote data to file: %s' % file_name 

    return

def print_data(data):
    print 'Do you want to print the data converted from Binary?'
    answer = str(raw_input('Yes or No '))
    answer = answer.lower()

    if answer == 'yes' or answer == 'y':
        print "----------START OF DATA----------"
        print data
        print "----------END OF DATA----------"
    
    return

def main():
    binary_text = ''
    text = ''
    loop = True
    
    print 'What would you like to do?'
    print '1. Input data from a file.'
    print '2. Input data from keyboard.'
    print '3. Exit'

    while loop:
        try:
            selection = int(raw_input('Choose a number above: '))
            loop = False
        except Exception:
            print "Expected an Integer"
            
        
    
    loop = True
    
    while loop:
        if selection == 1:
            file_location = str(raw_input("\nEnter File location: "))
                
            try:    
                with open(file_location, 'r+') as read_file:                    
                    switch = [next(read_file) for x in range(1)]
                    switch = switch[0].rstrip('\n')
                    loop = False
                if switch == 'TEXT':
                    with open(file_location, 'r+') as read_file:
                        next(read_file)
                        for line in read_file:
                            binary_text +=  convert_to_binary(line)
                    print 'Successfully converted text to binary'
                    save_data(binary_text)

                elif switch == 'BINARY':
                    with open(file_location, 'r+') as read_file:
                        next(read_file)
                        for line in read_file:
                            text +=  convert_to_text(line)
                    print 'Successfully converted binary to text'
                    save_data(text)
            except Exception:
                print "Bad Data. Either the file doesn't exist or something was misspelled"

    
                

        elif selection == 2:
            data = str(raw_input("Enter data: "))
    
            if data[0] != '0':
                binary_text = convert_to_binary(data)
                print'Successfully converted data'
                save_data(binary_text)
                loop = False
            
            elif data[0] == '0':
                text = convert_to_text(data)
                if text == None:
                    print 'Nothing was converted'
                    loop = False
                else:
                    print_data(text)
                    save_data(text)
                    loop = False
        else:
            print "Exiting"
    
main()
