


#Source code
def split(word): 
    return [char for char in word]
    
# Driver code 
word = 'HELLO WORLD! '

print(split(word))

def star(input):
    char_list = split(input)
    print(char_list)
    output_list = []
    
    
    for char in char_list:
    
        if char == "a":
            output_list.append("012")
        elif char == "b":
            output_list.append("10002")
        elif char == "c":
            output_list.append("10102")
        elif char == "d":
            output_list.append("1002")
        elif char == "e":
            output_list.append("02")
        elif char == "f":
            output_list.append("00102")
        elif char == "g":
            output_list.append("1102")
        elif char == "h":
            output_list.append("00002")
        elif char == "i":
            output_list.append("002")
        elif char == "j":
            output_list.append("01112")
        elif char == "k":
            output_list.append("1012")
        elif char == "l":
            output_list.append("01002")
        elif char == "m":
            output_list.append("112")
        elif char == "n":
            output_list.append("102")
        elif char == "o":
            output_list.append("1112")
        elif char == "p":
            output_list.append("01102")
        elif char == "q":
            output_list.append("11012")
        elif char == "r":
            output_list.append("0102")
        elif char == "s":
            output_list.append("0002")
        elif char == "t":
            output_list.append("12")
        elif char == "u":
            output_list.append("0012")
        elif char == "v":
            output_list.append("00012")
        elif char == "w":
            output_list.append("0112")
        elif char == "x":
            output_list.append("10012")
        elif char == "y":
            output_list.append("10112")
        elif char == "z":
            output_list.append("11002")
        elif char == ".":
            output_list.append("7")
        elif char == " ":
            output_list.append("3")
        else:
            output_list.append("9")
    
    
    
    
    return  output_list
    
final = star(split(word))
final_str = ''.join(map(str, final))
print(final_str)


            



