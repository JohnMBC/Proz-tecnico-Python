def calc_media(lista):
    media = sum(lista)/len(lista)
    return media
    
notas = [10, 5, 58]
resultado = calc_media(notas)
print(f"{resultado:.2f}")
