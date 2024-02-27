def ceaser(text, shift, direction):
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    
    return_text = ""
   
    if direction == "d":
        shift *= -1
            
    for letter in text:
        position = alphabet.index(letter)
        
       
        new_postion = position + shift
        return_text += alphabet[new_postion]
        
    print(f"The {direction} text is {return_text}")
    
    print(return_text)
    
ceaser("lttxj", 5, "d")
                
                
            
        
    