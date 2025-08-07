def add_student(DB:dict, name : str):
    duplicate_name(DB , name)
    name = name.lower().replace(' ', '')
    DB[name] = {}
    return DB

def add_course(DB:dict , name:str , course_name:str):
    
    duplicate_name(DB[name] , course_name)
    DB[name][course_name] = []
    return DB

def add_grade(DB : dict , name :str , course:str , grade:float):
    cant_fine(DB , name)
    cant_fine(DB[name] , course)
    DB[name][course].append(grade)
    return DB


def duplicate_name(DB:dict , name :str):
    if name in DB:
        raise Exception(f'this is => {name} add before !!! ')
def cant_fine(DB:dict , name :str):
    if not(name in DB):
        raise Exception(f'can`t fine {name}!!!')
    
    