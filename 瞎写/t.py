num = 0
for i in range(10, 100):
    if (i % 2 == 1) and (i % 3 == 2) and (i % 5 == 4):
       num += 1

if __name__ == '__main__':
    print(num)