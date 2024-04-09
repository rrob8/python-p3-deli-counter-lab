def line(people):
    if len(people) == 0:
        print("The line is currently empty.")
    else:
        phrase = 'The line is currently: '
        i = 1
        for person in people:
            if person == people[-1]:
                phrase += f'{i}. {person}'
            else:
                phrase += f'{i}. {person} '
                i += 1

        print(phrase)

def take_a_number (current_line, new_person):
    current_line.append(new_person)
    
    print(f'Welcome, {current_line[-1]}. You are number {current_line.index(new_person)+1} in line.')


def now_serving(current_line):

    

    if len(current_line) == 0:
            print('There is nobody waiting to be served!')

    else:
        
        print(f'Currently serving {current_line[0]}.')
        current_line.remove(current_line[0])
            
    
