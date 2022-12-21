import import_base
import view
import export_base  
import func
import log_

def button_click():
    file_extension = view.set_()
    dict = import_base.from_base(file_extension)
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
            dict, done_ = func.insert_(dict)
            export_base.export_(file_extension, dict)
            log_.contact_logger(done_)
        
        elif m == 4: 
            dict_new, done_ = func.update_(dict)
            export_base.export_(file_extension, dict_new)
            log_.contact_logger(done_)

        elif m == 5:
            dict_new, done_ = func.delete_(dict) 
            export_base.export_(file_extension,dict_new,)
            log_.contact_logger(done_)
        input('Нажмите Enter')