# file = open('my_file.txt', 'w')
# my_file = file.write('my first file,number 1.')
# file =  open('my_file.txt', 'r')
# my_file= file.read()
# print(my_file)

try: 
    file = open('my_file.txt', 'a')
    file.write('First additional line\n')
    file.write('Second additional line\n')
    file.write('Third additional line\n')
except FileNotFoundError:
    print('file not found')

finally:
    file.close()