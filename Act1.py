choose1 = 'piedra'
choose2 = 'papel'

if choose1 == choose2:
    msg = 'Empata'
    winner = 0
elif choose1 == 'piedra' and choose2 == 'tijera':
    msg = 'piedra daña la tijera'
    winner = 1
elif choose1 == 'tijera' and choose2 == 'piedra':
    msg = 'La piedra daña la tijera'
    winner = 2
elif choose1 == 'tijera' and choose2 == 'papel':
    msg = 'tijera corta el papel'
    winner = 1
elif choose1 == 'papel' and choose2 == 'tijera':
    msg = 'tijera corta el papel'
    winner = 2
elif choose1 == 'papel' and choose2 == 'piedra':
    msg = 'papel envuelve la piedra'
    winner = 1
elif choose1 == 'piedra' and choose2 == 'papel':
    msg = 'papel envuelve la piedra'
    winner = 2

if winner == 0:
    msg = 'Empata'
else:
    msg = f'Gana persona{winner}: {msg}'

print(msg)
