
student_data = { 'id1':
                {'name' : ['Sara'], 
                 'class' : ['V'],
                'subject' : ['Math', 'Science', 'English'],
                },

                'id2':
                {'name' : ['David'], 
                 'class' : ['V'],
                'subject' : ['Math', 'Science', 'English'],
                },

                'id3':
                {'name' : ['Sara'], 
                 'class' : ['V'],
                'subject' : ['Math', 'Science', 'English'],
                },

                'id4':
                {'name' : ['Surya'], 
                 'class' : ['V'],
                'subject' : ['Math', 'Science', 'English'],
                },
}

result = {}

for key,value in student_data.items():
    if value not in result.values():
        result[key] = value

print(result)

# Frequency test:

test_dic = {'codlingal' : 2, 'is' : 2, 'the' : 2, 'best' : 2, 'for' : 2, 'coding' : 1}

# print in the orginal format:
print("the orginal dictonary is" + str(test_dic))

# intitalize the value:
k = 2

# using loop:
# selective values in Key dictonary:
res = 0

for key in test_dic:
    if test_dic [key] == k:
        res = res + 1

# printing the result:
print("Frequency of K is: " + str(res))


# Finding the country code:

con_code = {'India' : '0091',
            'Australia': '0025',
            'Neplal' : '00977'}

# search dictornary for country code if India:
print("country code for India - ")
print(con_code.get('India', 'not found'))
# search dictonary for country code of Japan:
print("country code for Japan - ")
print(con_code.get('Japan', 'not found'))