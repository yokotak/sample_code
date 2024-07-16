KANSUJI_DIC = { key: str(no) for no, key in enumerate(['K','A','N','S','U','J','I']) }
print(KANSUJI_DIC)

KANSUJI_DIC = {f"{no}": str(x) for x, no in enumerate(['K','A','N','S','U','J','I'])}
print(KANSUJI_DIC)

print({no:str(x) for x, no in [(1, 'ds'),(100, 'fasjoi')]})