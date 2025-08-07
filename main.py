from functions import add_student ,add_course,add_grade,student_list,show_student_grades,avg_student

DB = {
    'alireza' : {
        'math' : [20,20,20],
        'physic' : [20],
        'programming' : [20 ]
    } ,
    'mohammad' : {
        'math' : [10 , 9],
        'physic' : [20 , 14],
        'programming' :[9]
    }
}

add_student(DB , 'ali')
add_student(DB , 'mamad')
add_course(DB, 'ali' , 'math')
add_grade(DB , 'ali' , 'math' , 20)
add_grade(DB , 'ali' , 'math' , 18)
print(avg_student(DB , 'alireza'))
