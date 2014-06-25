from sys import argv # use the argv module

script, filename = argv # argvs are the script file and the txt filename

txt = open(filename) # txt = opens the txt file

print "Here's your file %r:" % filename # prints the name of the file
print txt.read() # uses .read() to read the contents of the txt file

print "Type the filename again:"
file_again = raw_input("> ") # 

txt_again = open(file_again)

print txt_again.read()