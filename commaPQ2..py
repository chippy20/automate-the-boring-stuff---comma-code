def comma(x):
    
    for i in range(len(x)-2):
            print (str(x[i]) + ', ', end='')
    print (x[-2] + ' and ' + x[-1])

spam = ['apples', 'bananas', 'tofu', 'cats']
comma(spam)

