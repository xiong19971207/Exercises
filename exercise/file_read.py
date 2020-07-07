with open('file_math') as file:
    lines = file.readlines()

pi_string = ''
for line in lines:
    pi_string = pi_string + line.strip()
print(pi_string[-1:-10])
# print(len(pi_string))

p = '0123456789'
print(p[::-1])
