from src.Tyradex import Pokemon


def test_pokemon():
    all = Pokemon.all()
    last = all[-1].pokedex_id

    def transform(x):
        x = str(x)
        cut = []
        mem = ''
        for digit in x:
            if int(mem + digit) > last:
                cut.append(int(mem))
                mem = ''
            mem += digit
        cut.append(int(mem))

        return [Pokemon.get(obj) for obj in cut]

    print(transform(306100860922888193))
    print(transform(306429397701885952))
    print(transform(336443651628728322))
