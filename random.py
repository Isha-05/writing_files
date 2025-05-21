#import library
import itertools 

#define vowels and consonents
vowels = ['a', 'e', 'i', 'o', 'u']
consonents = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']

#Take input from the user  
number_of_character = int(input("The number of character names to generate: "))
    
number = number_of_character - 3

#create random combination of vowels and consonents  
vow = (list(itertools.combinations(vowels, 3)))
con = (list(itertools.combinations(consonents, number)))

#iterate over each list of vowel and consonent formed  
for i in vow:
    for j in con:
        #combine both  list of vowel and consonent
        names = i+j

        res = []
        for name in names:
            #if duplicate is present then only merge the list
            if name not in res:
                res = ''.join(names)
    
print(res)

#write a file
with open('character_names.txt', 'w') as write_file:
    write_file.write(res)
       
#read a file
with open('character_names.txt', 'r') as read_file:
    read_file.read()