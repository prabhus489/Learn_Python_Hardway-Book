from sys import argv

script, file_name = argv

txt = open(file_name)

print "Please check the content of your file %r as below:" % file_name
print txt.read()
print "Type the same file name once again:"
same_filename_again = raw_input("> ")
txt_again = open(same_filename_again)
print txt_again.read()
