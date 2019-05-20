def listasSonIguales(lista1, lista2):
   
    if (len(lista1) != len(lista2)):
       
 	return False
   
    elif ((lista1 == []) and (lista2 == [])):
    
   	return True
    else:
        
	return lista1[0] == lista2[0] and listasSonIguales(lista1[1:], lista2[1:])