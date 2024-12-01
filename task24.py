import string

alpa=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

znaki = string.punctuation

nabor_chisel=input("Ввеилте цифры через пробел: ")
nabor_chisel = nabor_chisel.split()

nabor_slov=''

for i in nabor_chisel:
    if i in znaki:
        nabor_slov+=i
        continue
    if i=='0':
        nabor_slov+=' '
        continue
    nabor_slov+=alpa[int(i)-1]
print(nabor_slov)
