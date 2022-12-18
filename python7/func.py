import view
import func
def select_(dict,s):
    s = str(s)
    dict_selected = {}
    for (k,v) in dict.items():
        for i in range(3):
            if s in v[i]:
                dict_selected[k]= [v[0], v[1], v[2]]
    return dict_selected            

def insert_(dict):
    s = view.new_contact()
    # l = []
    l = list(map(lambda i: i, s.split()))
    # print(l)
    dict[len(dict)+1] = l

def update_(dict):
    s = view.groupe_for_update_or_delete()
    dict_selected = func.select_(dict,s)
    view.view_all(dict_selected)
    s = view.contact_for_update()
    k,v0,v1,v2 = map(lambda i: i, s.split())
    k = int(k)
    dict[k] = [v0, v1, v2]
    return dict

def delete_(dict):
    s = view.groupe_for_update_or_delete()
    dict_selected = func.select_(dict,s)
    view.view_all(dict_selected)
    s = view.contact_for_delete()
    s = int(s)
    dict_new = {}
    for (k,v) in dict.items():
        if s != k:
            dict_new[k] = v
    return(dict_new)





