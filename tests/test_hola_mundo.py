from hola_mundo_poetry import generar_saludo

def test_generar_saludo():
    assert generar_saludo("Cristina") == "¡Hola mundo! Tu nombre es Cristina"
    assert generar_saludo("Juan") == "¡Hola mundo! Tu nombre es Juan"