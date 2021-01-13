#HONI 2019/2020 5.KOLO 1.ZAD STEAK.py
n=int(input())
m=['SIJECANJ','VELJACA','OZUJAK','TRAVANJ','SVIBANJ','LIPANJ','SRPANJ','KOLOVOZ','RUJAN','LISTOPAD','STUDENI','PROSINAC']
for i in range(n):
    dan=int(input())
    mjesec=str(input())
    razlika=dan+(m.index(mjesec)*30)
    if razlika%2==0:
        print('BROKULA')
    else:
        print('MRKVA')
