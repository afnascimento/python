def tem_convert(var):
    try:
        return int(var)
    except ValueError as error:
        print('error ocurred', error)

tem_convert('syz')