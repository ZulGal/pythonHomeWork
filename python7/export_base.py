
def export_(file_extension,dict):
    if file_extension == 1:
        path = r'bs.txt' 
        with open(path,'w') as f:
            for (k,v) in dict.items():
                for i in range(3):
                    f.write(v[i]+'\n')
    else: 
        path = r'bs.csv' 
        with open(path,'w') as f:
            for (k,v) in dict.items():
                f.write(v[0]+';'+v[1]+';'+v[2]+'\n')                