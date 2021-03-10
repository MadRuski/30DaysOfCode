import webbrowser
upit=str(input('Zelite li nasumicno(N) ili zelite odabrati zadatke(B)?: '))
if upit.lower()=='b':
    godina=int(input('Koju godinu zelite?: '))
    kolo=str(input('Koje kolo zelite otvoriti?: '))
    name=str(godina)+'_'+str(godina+1)+'/'+str(godina)+'_'+str(godina+1)+'_kolo'+kolo+'_zadaci.pdf'
    import webbrowser 
    webbrowser.open_new(r'name')  
    print(name)
