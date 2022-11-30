def hex_string_to_RGB(hex_string): 
    hex_string = hex_string[1:].upper()
    dec_dict = {}
    dec_list = [int(hex_string[i:i+2],16) for i in range(0,len(hex_string),2)]
    dec_dict.update({'r':dec_list[0],'g':dec_list[1],'b':dec_list[2]})
    return dec_dict
