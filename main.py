# Main function
def calc(n):
    target = n.split('x')[0].replace(',','')
    exponent = int(n.split('^')[1])
    
    isAlready = False

    if '10^' in n: isAlready = True

    # Scientific Notation Fixer
    if isAlready:
        found = 0
        decimal = False
        
        if target[0] == '0': decimal = True
        else: decimal = False

        if decimal == True:
            zeroCount = 0
            found = target.lstrip('0')
            if int(found) > 10:
                number = found[:1] + '.' + found[1:]
                found = target[:1] + '.' + target[1:]
                
            for i in target:
                if i == '0':
                    zeroCount -=1

            print(f'Zeros: {zeroCount}')
            print(f'Target: {target}')
            print(f'Number: {number}')
            print(f'{number}x10^{exponent + zeroCount}')
            
        if decimal == False:
            found = target.rstrip('0')
            if int(found) > 10:
                number = found[:1] + '.' + found[1:]
                found = target[:1] + '.' + target[1:]

                print(f'{number}x10^{len(found.split(".")[1]) + exponent}')
            else:
                zeroCount = 0
                for i in target:
                    if i == '0':
                        zeroCount +=1
                else:
                    print(f'{target.split("0")[0]}x10^{zeroCount}')
                
calc('0,00054535432x10^-3')
