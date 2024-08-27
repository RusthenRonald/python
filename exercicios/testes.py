for c in range(0,1):
    temp_1=int(input(f"Digite a  {c+1}° temperatura:"))
    escala_1=str(input(f"Digite a  {c+1}° escala"))
    c+=1
    temp_2=int(input(f"Digite a {c+1}° temperatura:"))
    escala_2=str(input(f"Digite a {c+1} escala"))

    if escala_1 in "Cc" and escala_2 in "Ff":
        temp_1=(temp_1*1.8)+32

    if escala_1 in "Ff" and escala_2 in "Cc":
        temp_2=(temp_2*1.8)+32

    if temp_1>temp_2:
        maior=temp_1
        escala_maior=escala_1
    else :
        maior=temp_2
        escala_maior=escala_2
print(f"A maior temperatura foi de {maior} na escala {escala_maior}")
