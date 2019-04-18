def calculate(data, findall):
    '''Имя переменной слева.
Знак перед = (если есть).
Имя переменной справа (если есть).
Число (если есть) со знаком (если есть).'''
    matches = findall(r"([a,b,c])([+,-]?)=([+,-]?[a,b,c])?([-,+]?\d*)")   # Если придумать хорошую регулярку, будет просто
    for v1, s, v2, n in matches:  # Если кортеж такой структуры: var1, [sign]=, [var2], [[+-]number]
        # Если бы могло быть только =, вообще одной строкой все считалось бы, вот так:

        predresult = data.get(v2, 0) + int(n or 0)
        if s:
            if s == '+':
                data[v1] += predresult
            elif s == '-':
                data[v1] -= predresult
        else:
            data[v1] = predresult

    return data