import os

all_players = []

folder_path = os.path.abspath(__file__)[:-13] + "stats"

where_ini = input("enter section >>> ")
to_find_ini = input("enter item/stat/entity >>> ")

for filename in os.listdir(folder_path):
    file_path = os.path.join(folder_path, filename)
    if os.path.isfile(file_path):
        
        with open(file_path) as f:
            line = f.readline()
            
            mined =     line.find('"minecraft:mined":')
            used =      line.find('"minecraft:used":')
            picked_up = line.find('"minecraft:picked_up":')
            dropped =   line.find('"minecraft:dropped":')
            custom =    line.find('"minecraft:custom":')
            broken =    line.find('"minecraft:broken":')
            killed_by = line.find('"minecraft:killed_by":')
            killed =    line.find('"minecraft:killed":')
            crafted =   line.find('"minecraft:crafted":')
            
            to_find = '"minecraft:' + to_find_ini + '":'
            
            if where_ini == "used":
                where = used
            elif where_ini == "mined":
                where = mined
            elif where_ini == "picked_up":
                where = picked_up
            elif where_ini == "dropped":
                where = dropped
            elif where_ini == "custom":
                where = custom
            elif where_ini == "broken":
                where = broken
            elif where_ini == "killed_by":
                where = killed_by
            elif where_ini == "killed":
                where = killed
            elif where_ini == "crafted":
                where = crafted

            

            values = [mined, used, picked_up, dropped, custom, broken, killed_by, killed, crafted]

                
            right = len(line)
            for n in values:
                if n == -1 or where == -1 or where == n:
                    pass
                elif right > n and n - where > 0:
                    right = n

            
            
            pos = line[where:right].find(to_find)

            amount = 0
            if pos == -1:
                pass
            
            else:
                amount = ""
                for n in range(12):
                    try:
                        
                        amount += str(int( line[where+pos+len(to_find)+n : where+pos+len(to_find)+1+n]))
                    except:
                        pass
                    

            amount= int(amount)

            all_players.append([amount, filename[:-5]])
            
def myFunc(e):
    if e[0] == "no":
        return 0
    else:
        return e[0]

all_players.sort(key = myFunc)

i = 783
for n in all_players:
    if i >= 100:
        print(i, "   ", n[0], "   ", n[1])
    elif i >= 10:
        print(i, "    ", n[0], "   ", n[1])
    else:
        print(i, "     ", n[0], "   ", n[1])

    i -= 1

print()
input("press [enter] to forget ")
