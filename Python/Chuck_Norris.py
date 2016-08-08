message = input()
bin_message=""
enc_message = message.encode()
for char in enc_message:
    bin_message += format(char, '07b')


unary_message = ""
prev_byte = None
for byte in bin_message:
    # Determine if previous byte is equal to byte
    if byte == prev_byte:
        unary_message += "0"
    else:
        prev_byte = byte
        if unary_message != "":
            unary_message += " "
        if byte == '1':
            unary_message += "0 0"
        else:
            unary_message += "00 0"

print(unary_message)
