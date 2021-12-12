cricket = []
badminton = []
football = []

total_cricket = int(input("Enter the number of students who play cricket-\n"))
for i in range(total_cricket):
    roll_number_cricket = int(input("Enter the roll number of the student-\n"))
    if roll_number_cricket not in cricket:
        cricket.append(roll_number_cricket)
    else:
        pass
total_badminton = int(input("Enter the number of students who play badminton-\n"))
for i in range(total_badminton):
    roll_number_badminton = int(input("Enter the roll number of the student-\n"))
    if roll_number_badminton not in badminton:
        badminton.append(roll_number_badminton)
    else:
        pass
total_football = int(input("Enter the number of students who play football-\n"))
for i in range(total_football):
    roll_number_football = int(input("Enter the roll number of the student-\n"))
    if roll_number_football not in football:
        football.append(roll_number_football)
    else:
        pass

def both_cricket_and_badminton(cricket,badminton):
    cricket_and_badminton = []
    for i in cricket:
        if i in badminton:
            cricket_and_badminton.append(i)
    for j in badminton:
        if j in cricket and j not in cricket_and_badminton:
            cricket_and_badminton.append(j)
    return cricket_and_badminton

def cricket_or_badminton_but_not_both(cricket,badminton):
    cricket_or_badminton_not_both = []
    for i in cricket:
        if i not in badminton:
            cricket_or_badminton_not_both.append(i)
        else:
            pass
    for j in badminton:
        if j not in cricket and j not in cricket_or_badminton_not_both:
            cricket_or_badminton_not_both.append(j)
        else:
            pass
    return cricket_or_badminton_not_both

def neither_cricket_nor_badminton(cricket,badminton,football):
    neither_cricket_nor_badminton_count = 0
    for i in football:
        if i not in cricket and i not in badminton:
            neither_cricket_nor_badminton_count += 1
        else:
            pass
    return neither_cricket_nor_badminton_count

def cricket_and_football_not_badminton(cricket,badminton,football):
    cricket_and_football_not_badminton = []
    for i in cricket:
        if i in football and i not in badminton and i not in cricket_and_football_not_badminton:
            cricket_and_football_not_badminton.append(i)
        else:
            pass
    for j in football:
        if j in cricket and j not in badminton and j not in cricket_and_football_not_badminton:
            cricket_and_football_not_badminton.append(j)

    cricket_and_football_not_badminton_count = 0
    for k in cricket_and_football_not_badminton:
        cricket_and_football_not_badminton_count += 1

    return cricket_and_football_not_badminton_count

print("Students who play both cricket and badminton- ",both_cricket_and_badminton(cricket,badminton))
print("Students who play cricket or badminton but not both- ",cricket_or_badminton_but_not_both(cricket,badminton))
print("Number of students who play neither cricket nor badminton- ",neither_cricket_nor_badminton(cricket,badminton,football))
print("Number of students who play cricket and football but not badmininton- ",cricket_and_football_not_badminton(cricket,badminton,football))
