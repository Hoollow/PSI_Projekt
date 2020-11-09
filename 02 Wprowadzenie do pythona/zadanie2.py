def funkcja2(data_text):
    slownik = {}
    lista = list(data_text)
    slownik = dict([("length", len(data_text)), ("letters", lista), ("big_letters", data_text.upper()),
                    ("small_letters", data_text.lower())])
    return slownik
