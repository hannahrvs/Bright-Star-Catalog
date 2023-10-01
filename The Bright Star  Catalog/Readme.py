# File: ReadFile.py
# Description: Takes the .dat file and converts to a .csv file
# Name: Hannah Sepnio
# UT EID: hvs337
# Date: Sept 27, 2023

import sys

def main():
    print("HR,Name,DM,HD,SAO,FK5,IRflag,r_IRflag,Multiple,ADS,ADScomp,VarID,RAh1900,RAm1900,RAs1900,DE-1900,DEd1900,DEm1900,DEs1900,RAh,RAm,RAs,DE-,DEd,DEm,DEs,GLON,GLAT,Vmag,n_Vma,u_Vmag,B-V,u_B-V,U-B,u_U-B,R-I,n_R-I,SpType,n_SpType,yr pmRA,yr pmDE,n_Parallax,Parallax,RadVel,n_RadVel,l_RotVel,RotVel,u_RotVel,Dmag,Sep,MultID,MultCnt,NoteFlag")
    for line in sys.stdin:
        line = line.rstrip( )
        line = line.replace(",", " ")
        s = " "
        s = s + line[0:4] + ','
        s = s + line[4:14] + ','
        s = s + line[14:25] + ','
        s = s + line[25:31] + ','
        s = s + line[31:37] + ','
        s = s + line[37:41] + ','
        s = s + line[41:42] + ','
        s = s + line[42:43] + ','
        s = s + line[43:44] + ','
        s = s + line[44:49] + ','
        s = s + line[49:51] + ','
        s = s + line[51:60] + ','
        s = s + line[60:62] + ','
        s = s + line[62:64] + ','
        s = s + line[64:68] + ','
        s = s + line[68:69] + ','
        s = s + line[69:71] + ','
        s = s + line[71:73] + ','
        s = s + line[73:75] + ','
        s = s + line[75:77] + ','
        s = s + line[77:79] + ','
        s = s + line[79:83]+ ','
        s = s + line[83:84]  + ','
        s = s + line[84:86] + ','
        s = s + line[86:88] + ','
        s = s + line[88:90] + ','
        s = s + line[90:96] + ','
        s = s + line[96:102] + ','
        s = s + line[102:107] + ','
        s = s + line[107:108]  + ','
        s = s + line[108:109]  + ','
        s = s + line[109:114] + ','
        s = s + line[114:115] + ','
        s = s + line[115:120] + ','
        s = s + line[120:121] + ','
        s = s + line[121:126] + ','
        s = s + line[126:127] + ','
        s = s + line[127:147] + ','
        s = s + line[147:148] + ','
        s = s + line[148:154] + ','
        s = s + line[154:160] + ','
        s = s + line[160:161]  + ','
        s = s + line[161:166] + ','
        s = s + line[167:170] + ','
        s = s + line[170:174] + ','
        s = s + line[174:176] + ','
        s = s + line[176:179] + ','
        s = s + line[179:180]  + ','
        s = s  + line[180:184] + ','
        s = s + line[184:190] + ','
        s = s + line[190:194] + ','
        s = s + line[194:196] + ','
        s = s + line[196:197]
        print(s)


if __name__ == "__main__":
    main()

# cd /Users/hannahsepnio/Desktop/DataVis/HW4
# python Readme.py < bsc5.dat > bsc5.csv
