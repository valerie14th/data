import time

print("- screen size = 720x1280")
print("- device processor = Qualcomm Snapdragon\n")
#line
print(70*"—")
print("\t\t\t    DATA CONVERTER")
print("\t\t\t     Using (def)")
print(70*"—")
#end of line

time.sleep(1)
def main():
    while True:
        inp_num = int(input("\ninput a number: "))
       #if inp_num == str:
       #    print("TRACE_BACK:ERROR:COMMAND-INPUT-SHOULD-A-NUMBER!")
       #    break
        time.sleep(2)
        print(70*"_")
        
        #==========================#
        bina = bin(inp_num)
        hexa = hex(inp_num)
        octa = oct(inp_num)
       #asci = ascii(inp_num)
        id_bina = id(bin(inp_num))
        id_hexa = id(hex(inp_num))
        id_octa = id(oct(inp_num))
       #id_asci = id(ascii(inp_num))
        #==========================#
        print(f"binary from [{inp_num}] = \t\t\t|\t{bina}")        
        print(f"hex from [{inp_num}] =    \t\t\t|\t{hexa}")
        print(f"octal from [{inp_num}] =  \t\t\t|\t{octa}")
       #print(f"ascii from [{inp_num}] =  \t\t\t|\t{asci}")
        print(70*"—")
        print(f"id from [{bina}] = \t\t|\t{id_bina}")        
        print(f"id from [{hexa}] =    \t\t\t|\t{id_hexa}")
        print(f"id from [{octa}] =  \t\t\t|\t{id_octa}")
       #print(f"id ascii from [{asci}] =  \t\t|\t{id_asci}")
        
        #line
        #==========================#
        print(70*"—")
        #end of line
        #tanyakan lagi
        time.sleep(2)
        tanya = str(input("lakukan pemrogramannya lagi? (y/n)\n - "))
        if tanya == "n":
            break
        elif tanya == "y":
            continue
        else:
            print("ERROR-COMMAND!")
            break
        #line
        print(70*"-")
        #end of line
        #==========================#
time.sleep(1)
main()
