from reading_csv import file1, file2

# creating subject function
def subject(subjectin):
    c = []                  # creating an empty list to append the classmarks during iteration
    s = []            # creating an empty list to append the subjects during iteration for part subject names
    for x in file1: 
        if subjectin in x[0]:
            if x[0] not in s:           # get distinct subjects
                s.append(x[0])
            if x[1] not in c:           # get distinct classmarks
                c.append(x[1])          # appending the classmarks to 'c'
            for y in file2:
                if y[0] == x[1]:
                    loc = y[1]      # 'loc' is the location of the subject that was given
    c_con = ", ".join(c)            # converting the list to strings
    s_con = ", ".join(s)
    output = 'Subject: ' + s_con + '\n' +'Classmark: ' + c_con + '\n' + 'Location: ' + loc 
    return output

# creating classmark function                        
def classmark(classmarkin):
    sub = []
    for x in file1:
        if classmarkin == x[1]:
            if x[0] not in sub:
                sub.append(x[0])                  # 'sub' is the subject name
            for y in file2:
                if y[0] == x[1]:
                    loc = y[1]
    sub_con = ", ".join(sub)
    output='Classmark: ' + classmarkin + '\n' +'Subject: ' + sub_con + '\n'+ 'Location: ' + loc 
    return output

def location(locationin):
    clm = []                # 'clm' is the classmark
    sub = []                # 'sub' is the subject name 
    for x in file2:
        if locationin == x[1]:
            if x[0] not in clm:                 # get distinct classmarks
                clm.append(x[0])
            for y in file1:
                if x[0] == y[1]:
                    if y[0] not in sub:         # get distinct subject names
                        sub.append(y[0])
    clm_con = ", ".join(clm)
    sub_con = ", ".join(sub)
    output='Location: ' + locationin + '\n' + 'Classmark: ' + clm_con + '\n' + 'Subject: ' + sub_con
    return output

