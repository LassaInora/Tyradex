from src.Tyradex import Pokemon

poke_team = lambda discord_id : [Pokemon.get(int(str(discord_id)[i:i+3])) for i in range(0, len(str(discord_id)), 3)]

print(poke_team(306100860922888193))
print(poke_team(306429397701885952))
print(poke_team(336443651628728322))