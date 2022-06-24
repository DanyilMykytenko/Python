def calc(a):
    try:
        if(a > 10):
            pass
            print('It\'s bigger than 10')
        else:
            print('Meeeh')
    except TypeError:
        print('Type Error incomming...')
    finally:
        print('THE END OF THE TRY-EXCEPT')

calc('str')
