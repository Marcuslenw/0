'''
Just a script I used to process some raw data I collected from some tests
source of raw data should be in the same folder as the script
'''
rf = open("timestamp+bytes.txt", "r")
fl = rf.read()
fl = fl.split()
rf.close()

fld = {}
for i in range(0,len(fl),2):
    if fl[i] not in fld:
        fld[fl[i]] = int(fl[i+1])
    else:
        fld[fl[i]] += int(fl[i+1])
    
for key, value in fld.items():
    print(key, value)
