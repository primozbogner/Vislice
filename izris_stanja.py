def izris(igra):
    '''Funkcija, ki izriše ustrezno sliko glede na število napačno uganjenih črk'''
    s = igra.stevilo_napak()
    if s == 0:
        return ''

    elif s == 1:
        return '''
            
            
              
              
      ________ '''

    elif s == 2:
        return '''            
       |
       |
       |
       |
      _|______ '''
      
    elif s == 3:
        return '''       _____
       |
       |
       |
       |
      _|______ '''
      
    elif s == 4:
        return '''       _____
       |   |
       |
       |
       |
      _|______ '''
      
    elif s == 5:
        return '''       _____
       |   |
       |   O
       |
       |
      _|______ '''
      
    elif s == 6:
        return '''       _____
       |   |
       |   O
       |   |
       |
      _|______ '''
      
    elif s == 7:
        return '''       _____
       |   |
       |   O
       |  /|
       |
      _|______ '''
      
    elif s == 8:
        return '''       _____
       |   |
       |   O
       |  /|\\
       |
      _|______ '''
      
    elif s == 9:
        return '''       _____
       |   |
       |   O
       |  /|\\
       |  /
      _|______ '''
      
    elif s == 10: 
        return '''       _____
       |   |
       |   O
       |  /|\\
       |  / \\
      _|______ '''
