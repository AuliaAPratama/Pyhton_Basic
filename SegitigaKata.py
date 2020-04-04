def segitigakata(x):
    x = x.replace(' ','')
    fab = []
    for i in range(len(x)):
        X = int((i*(i+1))/2)
        fab.append(X)
    if len(x) not in fab:
        print('Mohon maaf, jumlah karakter tidak memenuhi syarat membentuk pola')
    else:
        n = fab.index(len(x))
        k = 0
        for i in range(0,n):
            for _ in range(0,i+1):
                print(x[k] + ' ',end = '')
                k += 1
            print()
        k = 0
        for i in range(n,0,-1):
            for _ in range(1,i+1):
                print(x[k] + ' ',end = '')
                k += 1
            print()

segitigakata('Purwadhika')
segitigakata('Purwadhika Startup and Coding School @BSD')
segitigakata('kode')
segitigakata('kode python')
segitigakata('lintang')