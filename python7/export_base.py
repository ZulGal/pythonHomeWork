
def export_(dict):
    path = r'bs.txt' 
    with open(path,'w') as f:
        for (k,v) in dict.items():
            for i in range(3):
                f.write(v[i]+'\n')