digits = ['1','2','3','4','5','6','7','8','9']
en = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
fr = ['un','deux','trois','quatre','cinq','six','sept','huit','neuf']

# Write the necessary code to transform these arrays into a dictionary with the following format:
# { 
#   '1': {'french': 'un', 'english': 'one'},
#   '2': {'french': 'deux', 'english': 'two'},
#   '3': {'french': 'trois', 'english': 'three'},
#   ...
#   '9': {'french': 'neuf', 'english': 'nine'} 
# }

transform = {}
for i in range(len(digits)):
    transform[i+1] = {'French': fr[i], 'English':en[i]}

print (transform)