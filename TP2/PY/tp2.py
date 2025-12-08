#!/usr/bin/env python3

import os, sys, time
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

os.system("cls" if os.name == "nt" else "clear")

print(""" \033[91m
                                   .-''-.     
        _________   _...._       .' .-.  )    









   `'-'                     ( _.-'            
\033[94m""")
time.sleep(0.2)
os.system("cls" if os.name == "nt" else "clear")

print(""" \033[91m
                                   .-''-.     
        _________   _...._       .' .-.  )    
        \\        |.'      '-.   / .'  / /     
     .|  \\        .'```'.    '.(_/   / /      






   
   `'-'                     ( _.-'            
\033[94m""")
time.sleep(0.2)
os.system("cls" if os.name == "nt" else "clear")

print(""" \033[91m
                                   .-''-.     
        _________   _...._       .' .-.  )    
        \\        |.'      '-.   / .'  / /     
     .|  \\        .'```'.    '.(_/   / /      
   .' |_  \\      |       \\     \\    / /       
 .'     |  |     |        |    |   / /        


   |  |    |     | '-....-'`   .' '  _.'.-''  
   |  '.' .'     '.           /  /.-'_.'      
   |   /'-----------'        /    _.'         
   `'-'                     ( _.-'            
\033[94m""")
time.sleep(0.2)
os.system("cls" if os.name == "nt" else "clear")

print(""" \033[91m
                                   .-''-.     
        _________   _...._       .' .-.  )    
        \\        |.'      '-.   / .'  / /     
     .|  \\        .'```'.    '.(_/   / /      
   .' |_  \\      |       \\     \\    / /       
 .'     |  |     |        |    |   / /        
'--.  .-'  |      \\      /    .   . '         
   |  |    |     |\\`'-.-'   .'   / /    _.-') 
   |  |    |     | '-....-'`   .' '  _.'.-''  
   |  '.' .'     '.           /  /.-'_.'      
   |   /'-----------'        /    _.'         
   `'-'                     ( _.-'            
\033[94m""")
time.sleep(0.2)


def main():
    print("\033[97m[!]\033[94m Selectati tipul vectrorului")
    var = input("\033[91m[▲]\033[94m (2D[*]/3D) ").upper() or "2D"
    if var == "2D":
        os.system("cls" if os.name == "nt" else "clear")
        vec_2d_num = int(input("\033[91m[▲]\033[94m Inserati numarul vectorilor 2D:"))
        if not isinstance(vec_2d_num, int):
            print("\033[97m[!]\033[94m Input invalid")
            quit()
        else:
            array_list = np.ndarray(shape=(vec_2d_num, 2))
            # print(array_list)
            for pos, vec_2d in enumerate(array_list):
                print("Vector nr:", pos)
                array_list[pos, 0] = input("Dati X:")
                array_list[pos, 1] = input("Dati Y:")
                os.system("cls" if os.name == "nt" else "clear")
            for pos, vec_2d in enumerate(array_list):
                print(
                    "Norma vectorului {0} este:{1}".format(
                        (pos), np.linalg.norm(vec_2d)
                    )
                )
    elif var == "3D":
        os.system("cls" if os.name == "nt" else "clear")
        vec_3d_num = int(input("\033[91m[▲]\033[94m Inserati numarul vectorilor 3D:"))
        if not isinstance(vec_3d_num, int):
            print("\033[97m[!]\033[94m Input invalid")
            quit()
        else:
            array_list = np.ndarray(shape=(vec_3d_num, 3))
            for pos, vec_3d in enumerate(array_list):
                print("Vector nr:", pos)
                array_list[pos, 0] = input("Dati X:")
                array_list[pos, 1] = input("Dati Y:")
                array_list[pos, 2] = input("Dati Z:")
                os.system("cls" if os.name == "nt" else "clear")
            print("Vectorii sunt:")
            for pos, vec_3d in enumerate(array_list):
                print("Vector {0} = {1}".format(pos, vec_3d))
            for pos, vec_3d in enumerate(array_list):
                print(
                    "Norma vectorului {0} este:{1}".format(
                        (pos), np.linalg.norm(vec_3d)
                    )
                )
            vec_add = np.zeros(shape=(1, 3))
            vec_dif = array_list[0]
            for pos, vec_3d in enumerate(array_list):
                vec_add += vec_3d
                if pos != 0:
                    vec_dif -= vec_3d

            print("Suma vectorilor:", vec_add)
            print("Diferenta vectorilor:", vec_dif)

    else:
        print("\033[97m[!]\033[94m Input invalid")
        quit()


if __name__ == "__main__":
    main()
