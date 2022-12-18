import import_base
import view
import export_base  
import func

def button_click():
    dict = import_base.from_base()
    m = -1
    while m !=6:
        m = view.menu_()

        if m == 1:
            view.view_all(dict)

        elif m ==2:
            s = view.contact_for_search()
            dict_selected = func.select_(dict,s) 
            view.view_all(dict_selected) 
        elif m == 3:
            func.insert_(dict)
            # view.view_all(dict)
            export_base.export_(dict)
        
        elif m == 4:   
            dict_new = func.update_(dict)
            # view.view_all(dict)
            export_base.export_(dict_new)

        elif m == 5:
            dict_new = func.delete_(dict) 
            export_base.export_(dict_new)
        input('Нажмите Enter')