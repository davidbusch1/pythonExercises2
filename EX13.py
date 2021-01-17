carros = ["POLO", "PALIO", "GOL", "CELTA", "CORSA"]
consumo = [12.5, 15.0, 14.3, 13.9, 16.1]

valor_gas = 2.25
total_km = 1000

for j, c in enumerate(carros):

    consumo_litro = round(total_km / consumo[j], 1)

    print(f"{j+1} - {c} - {consumo[j]} - {consumo_litro} litros - R {round(consumo_litro * valor_gas, 2)}")

print(f'O menor consumo é do {carros[consumo.index(max(consumo))]}')

