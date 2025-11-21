from src.main import validar_correo


def test_correo_valido ():

    assert validar_correo ("usuario@gmail.com") == True
    assert validar_correo ("user.prueba@caminos.co") == True


    def test_correo_invalidos():

        assert validar_correo ("prueba@") == False
        assert validar_correo ("prueba.com") == False
        assert validar_correo ("caminos@caminos,com") == False

        