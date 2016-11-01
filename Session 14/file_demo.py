import os
# fout = open('output.txt', 'w')                  # w = write, if it were r it would be read

# line_1= "How many roads must a man walk down\n" # \n = new line

# fout.write(line_1)

# line_2 = "Before you call him a man?\n"
# fout.write(line_2)

# fout.close()

# print(os.path.exists('output.txt'))

# print(os.path.isdir('output.txt'))          #folder name

# def walk2(dirname):
#     """Prints the names of all files in 
#     dirname and its subdirectories.

#     dirname: string name of directory
#     """
#     count = 0
#     for root, dirs, files in os.walk(dirname):
#         for filename in files:
#             print(os.path.join(root, filename))        #prints all the files in the current folder
#             count+=1
#     print(count, 'files in total.')
# walk2(os.getcwd())

try:    
    fin = open('bad_file')
except:
    print('Something went wrong.')

print('still works here.')
