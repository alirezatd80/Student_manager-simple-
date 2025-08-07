from functions import cant_fine,add_student ,add_course,add_grade,student_list,show_student_grades,avg_student

DB_computer={}

def main():
    print('welcome to this programming')
    while True:
        order = int(input('1 for add student\n2 for panel student\n3 for exit\n'))
        if order == 1 :
            try:
                add_student(DB_computer , input('enter student name : '))
            except:
                print('-------------name is exist!!!-------------')
        if order == 2 :
            try : 
                stu_name = input('enter student_name : ')
                cant_fine(DB_computer,stu_name)
            except:
                print('------------cant find student!!!-------------- ')
                continue
            while True:
                new_order = int(input(f'hi {stu_name}\n1 for add course\n2 for course panel\n3 for grade student \n4 for average \n5 for back\n'))
                if new_order ==1 :
                    try :
                        add_course(DB_computer , stu_name,input(f'enter course name for {stu_name} : '))
                    except :
                        print('-----------this course is exist !!!-----------')
                if new_order ==2 :
                    try:
                        course_name = input('enter coursename :')
                        cant_fine(DB_computer[stu_name] , course_name)
                    except:
                        print('-----------cant find course name !!!-----------')
                        continue
                    while True:
                        newes_order = int(input('1 for add grade\n2 for back\n'))
                        if newes_order ==1 :
                            try:
                                add_grade(DB_computer,stu_name,course_name,int(input(f'enter grade for {course_name} :')))
                            except : 
                                print("-----error cant add grade !!! ------")
                                
                        if newes_order ==2 :
                            break
                if new_order ==3:
                    try :
                        print(f'{stu_name} grades = {show_student_grades(DB_computer,stu_name)}')
                    except  e:
                        print(f'cant show expet becuse {e}')
                if new_order ==4 :
                    try :
                        print(f'average {stu_name} = {avg_student(DB_computer,stu_name)}')
                    except Exception as e:
                        print(f"I can't calculate the average score.")
                
                if new_order==5 :
                    break
        if order == 3 :
            break
            




if __name__ == "__main__":
    main()