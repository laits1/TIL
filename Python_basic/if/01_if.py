# password = 1234
password = int(input())
yo = "요"

if password == 1234:
    print(f'맞음{yo}')
else:
    print(f'틀림{yo}')

print(f'끝')

# else 문이나 if 문에서 아무것도 수행하지 않게 하려면

if password == 1234:
    print(f'맞음{yo}')
else:
    pass # 수행없이 문장을 종료
