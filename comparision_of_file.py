
old_file = open('./old_file.txt', 'r')
new_file = open('./new_file.txt', 'r')

#total lines
old_file_lines = old_file.readlines()
new_file_lines = new_file.readlines()


if ((len(old_file_lines) and len(new_file_lines)) == 0):
    print('Alert: There is a blank file which not comparable !')

elif((len(old_file_lines) or len(new_file_lines)) > 0):    
    for i in range(len(old_file_lines)):
        if old_file_lines[i] != new_file_lines[i]:
            print('\n change in line number : ', i+1)
            print('>>>previous line is: ', old_file_lines[i])
            print('>>>changes is : ', new_file_lines[i])
            print('****---------------****','\n')

        else:
            print('\n unchanged line: ', i+1)

else:
    print('No change detected !', '\n')

print('\n','It\' so funny ..')