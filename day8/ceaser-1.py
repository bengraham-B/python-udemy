alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.

    #TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.  
    #e.g. 
    #plain_text = "hello"
    #shift = 5
    #cipher_text = "mjqqt"
    #print output: "The encoded text is mjqqt"

    ##HINT: How do you get the index of an item in a list:
    #https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list

    ##🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛
    
def encrypt(text, shift):
    
    encrypted_code = ""
    
    for letter in text:
        index_int = int(alphabet.index(letter))
        encoded_index = index_int + shift
        
        if encoded_index >= 26:
            repeat_index = encoded_index - 26
            encrypted_code += alphabet[repeat_index]
            
        else:
            encrypted_code += alphabet[encoded_index]
        
    print(encrypted_code)
    return encrypted_code

def decrypt(text, shift):
    decrypted_code = ""
    
    for letter in text:
        index_int = alphabet.index(letter)
        decoded_index = index_int - shift
        
        if decoded_index <= 0:
            repeate_index = 0 + decoded_index
            decrypted_code += alphabet[repeate_index]

        else:
            decrypted_code += alphabet[decoded_index]
    
    print(decrypted_code)

#TODO-3: Call 
if direction == "e":
    encrypt(text=text, shift=shift)
elif direction == "d":
    decrypt(text=text, shift=shift)
