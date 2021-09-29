
while True:
    Parole_da_concatenare = [] #Creo una lista che conterrà tutte le parole
    contatore = 0 #Creo un contatore per quante saper quante parole sono state scritte
    
    
    while True: #Creo un ciclo infinito
        try:
            Quante_parole = int(input("Quante parole vuoi concatenare?  ")) #Chiedo un numero in input
            print("")
            break  #Se il  valore dato dall'utente è corretto rompo il ciclo
        except: #Se non è corretto avverto l'utente di inserire un numero valido e richiedo l'input
            print('''Mi dispiace, è possibile inserire solo numeri interi... 
    Ritenta di nuovo

    ''')
            
    for i in range(Quante_parole): #Ripeto per il numero di parole da scrivere 
        contatore += 1 #Aumento il contatore in modo da sapere qual'è il numero della prossima parola da scrivere
        Parole_da_concatenare.append(str(input(f"Qual è la {contatore}ª parola da concatenare?  "))) #Chiedo la parola in input e la aggiungo ad una lista
    print("")   
    print(" ".join(Parole_da_concatenare)) #Concateno tutte le parole della lista e le restituisco in output
    input("Premi ctrl + c per chiudere il programma oppure premi invio per concatenare altre parole") #Se l'utente da un input il ciclo si ripete mentre se preme ctrl + c alza un eccezione che chiude il programma 