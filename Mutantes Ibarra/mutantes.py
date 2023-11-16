

 #-----------------FUNCION PARA VERIFICAR SI ES MUTANTE O NO-------------------
     
def is_mutant(dna):
    sumamutan=0
  
    n = len(dna)

     #-----------------------------VERIFICO VERTICALMENTE-------------------------
    
    for j in range(n):
        column = ''.join(dna[i][j] for i in range(n))
        if has_mutant_sequence(column):
            sumamutan+=1
                        
     # --------------------------VERIFICO HORIZONTALMENTE-------------------------
     
    for i in range(n):
        if has_mutant_sequence(dna[i]):
            sumamutan+=1
                       
     #----------------------------------------------------------------------------
     # ----------------------------VERIFICO DIAGONALES----------------------------
    
    for i in range(n - 3):
        for j in range(n - 3):
            diagonal = ''.join(dna[i + k][j + k] for k in range(4))
            if has_mutant_sequence(diagonal):
                sumamutan+=1
                
     #----------------------------------------------------------------------------           
     #-------------------------AHORA DIAGONALES INVERSAS--------------------------
    for i in range(3, n):
        for j in range(n - 3):
            diagonal = ''.join(dna[i - k][j + k] for k in range(4))
            if has_mutant_sequence(diagonal):
                sumamutan+=1
     #----------------------------------------------------------------------------
     #------------------VERIFICO LA CANTIDAD DE COINCIDENCIAS--------------------- 
       
    if sumamutan>=2:         
      return True
    
    return False
    
#------------------------------------------------------------------------------
       
#----FUNCION PARA VERIFICAR SI CONTIENE SECUENCIA DE LAS LETRAS A,C,T o G------ 
 
def has_mutant_sequence(sequence):
       return 'AAAA' in sequence or 'TTTT' in sequence or 'CCCC' in sequence or 'GGGG' in sequence

#------------------------------------------------------------------------------


# -------------------VERIFICAR SI COLO CONTIENE A, T, C, G)--------------------
def cadena_valida(cadena):
    
    cadena = cadena.upper()

    
    for caracter in cadena:
        if caracter not in 'ATCG':
            return False


    return True
#------------------------------------------------------------------------------ 

#---------------------------------INPUT DE ADN---------------------------------
dna = []
for i in range(6):
    palabra = input(f"_Ingrese secuencia del ADN N° {i + 1} (debe tener 6 letras y solo contener A, T, C, G): ")

   
    while len(palabra) != 6 or not cadena_valida(palabra):
        print("La palabra ingresada no cumple con los requisitos. Por favor, inténtelo de nuevo.")
        palabra = input(f"Ingrese la palabra {i + 1} (debe tener 6 letras y solo contener A, T, C, G): ")

    
    dna.append(palabra)
# ---------------------------RESULTADO: ES MUTANTE?----------------------------
if is_mutant(dna):
    print("---------------")
    print("¡Es un mutante!")
    print("---------------")
else:
    print("-----------------------------")
    print("La persona no es un mutante!.")
    print("-----------------------------")
#------------------------------------------------------------------------------
