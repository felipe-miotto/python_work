cafés = ['Frutas Amarelas', 'Frutas Verdes', 'Gourmet']
print("Original:")
print(cafés)
print(f"\nMeu favorito é o {cafés[0]}.")
print(f"\nO que eu menos gosto é o {cafés[-1]}.")

cafés[1] = 'Frutas Vermelhas'
print(f"\nOps, percebi um erro! O correto é {cafés}.")

cafés.append('Caramelo e Mel')
print(f"\nAdicionando mais um do pacote: \n{cafés}")

cafés.insert(0, 'Caramelo e Chocolate')
print(f"\nMais um pra conta: \n{cafés}")

del cafés[3]
print(f"\nComo nem gosto tanto, vamos remover o 'Gourmet':\n{cafés}\n")

popped_café = cafés.pop()
print(cafés)
print(f"Removido mais um, o {popped_café}")

segundo_café_preferido = cafés.pop(2)
print(f"\nO meu segundo café preferido é o {segundo_café_preferido}.")

cafés.remove('Caramelo e Chocolate')
cafés.insert(0, 'Frutas Vermelhas')
print(f"\nVamos deixar os dois melhores então:\n{cafés}")

cafés.insert(1, 'Gourmet')
cafés.append('Caramelo e Mel')
cafés.append('Caramelo e Chocolate')
print(f"\nLista completa dos cafés:\n{cafés}")

print(f"\nAgora em ordem alfabética:\n{sorted(cafés)}")
print(f"\nVoltando ao normal:\n{cafés}")
cafés.reverse()
print(f"\nE ao contrário: \n{cafés}")

print(f"\nO número total de cafés desse pacote é {len(cafés)}.")
