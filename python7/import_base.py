
def from_base(file_extension):
    if file_extension == 1:
        path = r'bs.txt'
        with open(path,'r') as f:
            dict = {}
            key = 0
            i = 0
            l_in_dict = []
            for line in f:
                if i<3:
                    l_in_dict.append(line[:-1])
                else:
                    dict[key] = l_in_dict
                    i = 0
                    l_in_dict = []
                    l_in_dict.append(line[:-1])
                    key +=1
                i +=1
        dict[key] = l_in_dict  

    else:
        path = r'bs.csv'
        with open(path,'r') as f:
            dict = {}
            key = 0
            i = 0
            l_in_dict = []
            for line in f:
                l_in_dict = list(line[:-1].split(';'))
                dict[key] = l_in_dict
                key +=1
    return dict






       