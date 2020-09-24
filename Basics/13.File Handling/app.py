#working with files 

import os

#To Check file of directory exits or not

print(os.path.isfile('./main.py'))


#To walk directory

# for file in os.walk('./'):
#     print(file)


#Creating directory 

# if not os.path.exists('mydir'):
#     os.makedirs('mydir')

# if not os.path.exists('mydir'):
#     try:
#         os.makedirs('mydir')
#     except OSError as e:
#         if e.errno != errno.EEXIST:
            


#Creating a file
#This will create a file with context and after writing it will close.

# def main():
#     with open('test.txt','w') as file:
#         file.write('This is sample text!')


# if __name__ == '__main__':
#     main()


#Now writing with cotext manager 


# file = open('test.txt', 'w')
# file.write('This is sample text 2!')
# file.close()


def main():
    with open('test.txt', 'r') as file:
        for line in file:
            print(line)



if __name__ == '__main__':
    main()

