# Комплексные числа

def comp (one_number, second_number, sign):
    if second_number == 0 and sign == '/':
        return 'Это не комплексное число'

    for i in one_number:
        if '+' or '-' in i:
            x_complex = complex(one_number)    
            break
        if '+' or '-' not in i:
            x_complex = f'0+{one_number}'
            complex(x_complex)

    for i in second_number:
        if '+' or '-' in i:
            y_complex = complex(second_number)    
            break
        if '+' or '-' not in i:
            y_complex = f'0+{second_number}'
            complex(second_number) 

    match sign:
        case'+':
            result = str(x_complex + y_complex)
            if '1j' in result:
                result.replace('1j','j')
            return result
        case'-':
            result = str(x_complex - y_complex)
            if '1j' in result:
                result.replace('1j','j')
            return result
        case '*': 
            result = str(x_complex * y_complex)
            if '1j' in result:
                result.replace('1j','j')
            return result
        case '/': 
            result = str(x_complex / y_complex)
            if '1j' in result:
                result.replace('1j','j')
                return result
            return result                
