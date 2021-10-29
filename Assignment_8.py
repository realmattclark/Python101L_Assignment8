test_scores = []
assignment_scores = []

def add_test():
    score = int(input('Add test score: \n'))
    str(score)
    test_scores.append(score)
    

def remove_test():
    
    test_scores.remove[-1]

def clear_test():
    test_scores.clear()

def add_assignment():
    assign_score = int(input('Enter Assignment Grade: \n'))
    str(assign_score)
    assignment_scores.append(assign_score)

def remove_assignment():
    assignment_scores.remove[-1]

def clear_assignments():
    assignment_scores.clear()

def find_mean():
    mean = test_scores[0] + test_scores[n] / len(test_scores)

    return mean



main_menu = input('Welcome to the Grade Menu. Please select an option: \n1) - Add Test \n2) - Remove Tests \n3) - Clear Tests \n4) - Add Assignment \n5) - Remove Assignment \n6) - Clear Assignments \nD) - Display Scores \nQ) - Quit \n==> ')

while main_menu != 'Q' or 'q':
    if main_menu == '1':
        str(main_menu)
        add_test()
    elif main_menu == '2':
        str(main_menu)
        remove_test()
    elif main_menu == '3':
        str(main_menu)
        clear_test()
    elif main_menu == '4':
        str(main_menu)
        add_assignment()
    elif main_menu == '5':
        str(main_menu)
        remove_assignment()
    elif main_menu == '6':
        str(main_menu)
        clear_assignments()
    elif main_menu == 'D' or 'd':
        print(test_scores, assignment_scores)
    else:
        print('Thanks!')
        quit()
