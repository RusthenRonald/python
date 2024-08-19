times_brasileirao_2024 = ("Atlético-MG","Atlético-PR","Bahia","Botafogo","Corinthians",
    "Coritiba","Cruzeiro","Cuiabá","Flamengo","Fluminense","Fortaleza","Goiás","Grêmio","Internacional","Palmeiras","Red Bull Bragantino","Santos","São Paulo","Vasco da Gama","Sport Recife"
)
print(f"Os 5 primeiros times do barsileirão são {times_brasileirao_2024[:6]}")
print(f"Os ultimos 4 colocados são {times_brasileirao_2024[-4:]}")
print(f"Os times em ordem alfabética {sorted(times_brasileirao_2024)}")
print(f"O Internacional está na posição {times_brasileirao_2024.index("Internacional")}°")