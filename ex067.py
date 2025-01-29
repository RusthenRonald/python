times = (
    "Flamengo", "Palmeiras", "Atlético-MG", "Fluminense", "São Paulo",
    "Corinthians", "Internacional", "Grêmio", "Botafogo", "Athletico-PR",
    "Vasco da Gama", "Cruzeiro", "Fortaleza", "Santos", "Bahia",
    "Cuiabá", "Gremio", "Red Bull Bragantino", "América-MG", "Goias"
)
print("=-"*10)
print(f"Os times da tabela do brasileirão são {times}")
print("=-"*10)
print(f"Os cinco primeiros colocados são {times[:5]}")
print("=-"*10)
print(f"Os times em ordem alfabética são {sorted(times)}")
print("=-"*10)
print(f"O Flamengo está na posição {times.index("Flamengo")+1}°")