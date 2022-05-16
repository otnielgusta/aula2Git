def teste(emp_id:str, kind:str):
    depois(**{f"push__extra_data__emps_failed_{kind}": emp_id})

def depois(**kwargs):
    print("Adicionei essa linha")
    print(kwargs)


teste(emp_id="employee.id", kind="exporter_generate_dict_task_bv_e09")
