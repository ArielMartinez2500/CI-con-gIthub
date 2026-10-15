
import pytest
from unittest.mock import patch

from temperatura import (
    celsius_a_fahrenheit,
    solicitar_temperatura,
    mostrar_conversion,
    mostrar_menu
)


# ==========================================
# PRUEBAS DE CONVERSION
# ==========================================

def test_conversion_correcta():
    """Verifica la conversion de Celsius a Fahrenheit."""
    assert celsius_a_fahrenheit(25) == 77


def test_conversion_cero():
    """Verifica el punto de congelacion del agua."""
    assert celsius_a_fahrenheit(0) == 32


def test_conversion_negativa():
    """Verifica temperaturas negativas."""
    assert celsius_a_fahrenheit(-40) == -40


def test_conversion_decimal():
    """Verifica temperaturas con decimales."""
    assert celsius_a_fahrenheit(37.5) == 99.5


def test_caso_limite():
    """Verifica el cero absoluto."""
    resultado = celsius_a_fahrenheit(-273.15)
    assert resultado == pytest.approx(-459.67)


def test_conversion_texto():
    """Verifica que se rechacen cadenas de texto."""
    with pytest.raises(TypeError):
        celsius_a_fahrenheit("calor")


def test_conversion_booleano():
    """Verifica que se rechacen valores booleanos."""
    with pytest.raises(TypeError):
        celsius_a_fahrenheit(True)


# ==========================================
# PRUEBAS DE ENTRADA DEL USUARIO
# ==========================================

def test_solicitar_temperatura_valida():
    """Verifica que el usuario ingrese un numero."""
    with patch("builtins.input", return_value="25"):
        resultado = solicitar_temperatura()
        assert resultado == 25.0


def test_solicitar_temperatura_decimal():
    """Verifica que se acepten numeros decimales."""
    with patch("builtins.input", return_value="36.5"):
        resultado = solicitar_temperatura()
        assert resultado == 36.5


def test_solicitar_temperatura_invalida(capsys):
    """Verifica que se solicite otro valor si hay error."""
    with patch("builtins.input", side_effect=["abc", "20"]):
        resultado = solicitar_temperatura()

    assert resultado == 20.0

    salida = capsys.readouterr().out
    assert "Error" in salida


# ==========================================
# PRUEBAS DE RESULTADOS
# ==========================================

def test_mostrar_conversion(capsys):
    """Verifica que el resultado aparezca en pantalla."""
    with patch("builtins.input", return_value="25"):
        mostrar_conversion()

    salida = capsys.readouterr().out

    assert "25.00" in salida
    assert "77.00" in salida


def test_mostrar_conversion_negativa(capsys):
    """Verifica resultados de temperaturas negativas."""
    with patch("builtins.input", return_value="-40"):
        mostrar_conversion()

    salida = capsys.readouterr().out

    assert "-40.00" in salida


# ==========================================
# PRUEBAS DEL MENU
# ==========================================

def test_menu_salir(capsys):
    """Verifica que el usuario pueda salir."""
    with patch("builtins.input", return_value="2"):
        mostrar_menu()

    salida = capsys.readouterr().out

    assert "Gracias por utilizar" in salida


def test_menu_opcion_invalida(capsys):
    """Verifica el manejo de opciones incorrectas."""
    with patch("builtins.input", side_effect=["9", "2"]):
        mostrar_menu()

    salida = capsys.readouterr().out

    assert "Opción incorrecta" in salida


def test_menu_conversion(capsys):
    """Verifica la conversion desde el menu."""
    with patch("builtins.input", side_effect=["1", "25", "2"]):
        mostrar_menu()

    salida = capsys.readouterr().out

    assert "77.00" in salida
    assert "Gracias por utilizar" in salida
