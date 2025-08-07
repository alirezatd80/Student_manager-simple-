from functions import add_student ,add_course,add_grade

DB = {
    'alireza' : {
        'math' : [12,15],
        'physic' : [20],
        'programming' : [20 , 14]
    } ,
    'mohammad' : {
        'math' : [10 , 9],
        'physic' : [20 , 14],
        'programming' :[9]
    }
}

add_student(DB , 'ali')
add_course(DB, 'ali' , 'math')
add_course(DB , 'alireza' , 'opennig')
add_grade(DB , 'ali' , 'math' , 20)
add_grade(DB , 'ali' , 'math' , 18)
add_grade(DB , 'alireza' , 'opennig' , 8)

print(DB)