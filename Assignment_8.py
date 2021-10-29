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

def find_mean_test():
    n = map(input(test_scores))
    mean_test = (test_scores[0] + test_scores[n] / len(test_scores)) * .6
    return mean_test

def find_mean_assignments():
    n = map(input(assignment_scores))
    mean_assignment = (assignment_scores[0] + test_scores[n] / len(assignment_scores)) * .4
def deviation():
    math.sqrt((test_scores[0] - mean_test)**2 + (test_scores[n] - mean_test)**2) / len(test_scores)





def program():
    main_menu = input('Welcome to the Grade Menu. Please select an option: \n1) - Add Test \n2) - Remove Tests \n3) - Clear Tests \n4) - Add Assignment \n5) - Remove Assignment \n6) - Clear Assignments \nD) - Display Scores \nQ) - Quit \n==> ')
    while main_menu != 'Q' or 'q':
        if main_menu == '1':
            str(main_menu)
            add_test()
            back = input('Enter Y to add more scores, N to return to menu ')
            if back == 'Y' or 'y':
                continue
            elif back == 'N' or 'n':
                break
            else:
                print('Invalid Answer')
        elif main_menu == '2':
            str(main_menu)
            remove_test()
            program()
        elif main_menu == '3':
            str(main_menu)
            clear_test()
            program()
        elif main_menu == '4':
            str(main_menu)
            add_assignment()
            program()
        elif main_menu == '5':
            str(main_menu)
            remove_assignment()
            program()
        elif main_menu == '6':
            str(main_menu)
            clear_assignments()
            program()
        elif main_menu == 'D' or 'd':
            print(test_scores, assignment_scores)
            program()
        else:
            print('Thanks!')

program()

