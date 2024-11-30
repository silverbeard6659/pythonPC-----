if False:
    print('hello world')
    
x = -1
if x > 0:
    print('x is greater than 0')
elif x < 0:
    print('x is less than 0')
else:
    print('x is 0')

print('\n_______________')

y = 10
if y > 2 and x < 0:
    print('y is > 2 and x < 0')
if y > 5:
    print('y is > 5')
    
print('\n_______________')

#msg=('Hello world')
msg=('')
if msg:
    print('msg is filled with str:', msg)
if not msg:
    print('msg is empty')
else:
    print('msg is not exist')
    
psg=('')
if bool(psg):
    print('psg is filled with str:', psg)
    
psg=('')
if psg:
    print('psg is filled with str:', psg)
    
x=3
if x:
    print('if x 0 then there is no message for x, but if you see it then x=', x)