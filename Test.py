import pytest
from Tarea import BeverageManager  # Importa la clase BeverageManager desde el módulo beverage_module

# Fixture que crea una instancia de BeverageManager antes de cada prueba
@pytest.fixture
def manager():
    return BeverageManager()

# Prueba para verificar que un nombre de bebida válido se agrega correctamente
def test_valid_beverage_name(manager):
    manager.add_beverage("Coffee,12,16,20")
    assert len(manager.beverages) == 1  # Verifica que se haya agregado una bebida correctamente

# Verifica que no se agregue ninguna bebida que cotenga caracteres no alfabéticos
def test_invalid_non_alpha_name(manager):
    manager.add_beverage("c4f3,12,16,20")
    assert len(manager.beverages) == 0  

# Prueba para verificar que un nombre de bebida con menos de 2 caracteres no se acepta
def test_invalid_short_beverage_name(manager):
    manager.add_beverage("C,12,16,20")
    assert len(manager.beverages) == 0  # Verifica que no se haya agregado ninguna bebida

# Prueba para verificar que un nombre de bebida con más de 15 caracteres no se acepta
def test_invalid_long_beverage_name(manager):
    manager.add_beverage("ThisIsAVeryLongBeverageName,12,16,20")
    assert len(manager.beverages) == 0  # Verifica que no se haya agregado ninguna bebida

# Prueba para verificar que los tamaños de bebida están dentro del rango permitido
def test_valid_size_range(manager):
    manager.add_beverage("Tea,1,5,10,20")
    assert len(manager.beverages) == 1  # Verifica que se haya agregado una bebida correctamente

# Prueba para verificar que los tamaños de bebida fuera del rango no se aceptan
def test_invalid_size_range(manager):
    manager.add_beverage("OrangeJuice,0,5,10,20")
    assert len(manager.beverages) == 0  # Verifica que no se haya agregado ninguna bebida

# Prueba para verificar que los tamaños de bebida son números enteros
def test_valid_integer_size(manager):
    manager.add_beverage("Water,1,2,3,4,5")
    assert len(manager.beverages) == 1  # Verifica que se haya agregado una bebida correctamente

# Prueba para verificar que los tamaños de bebida se ingresan en orden ascendente
def test_valid_sizes_order(manager):
    manager.add_beverage("Soda,5,10,15,20")
    assert manager.beverages[0].sizes == [5, 10, 15, 20]  # Verifica que los tamaños estén en orden ascendente

# Prueba para verificar que se acepta un máximo de cinco tamaños por bebida
def test_valid_max_sizes(manager):
    manager.add_beverage("Juice,1,2,3,4,5")
    assert len(manager.beverages[0].sizes) == 5  # Verifica que se hayan agregado cinco tamaños

# Pruebas para verificar que se aceptan tamaños con valores enteros en un rango de 1-48
def test_valid_min_size(manager):
    manager.add_beverage("Coffee,1")
    assert len(manager.beverages) == 1  # Verifica que se haya agregado una bebida correctamente

def test_valid_max_size(manager):
    manager.add_beverage("Tea,48")
    assert len(manager.beverages) == 1  # Verifica que se haya agregado una bebida correctamente

def test_invalid_min_size(manager):
    manager.add_beverage("Coffee,-1")
    assert len(manager.beverages) == 0  # Verifica que no se haya agregado una bebida

def test_invalid_max_size(manager):
    manager.add_beverage("Tea,49")
    assert len(manager.beverages) == 0  # Verifica que no se haya agregado una bebida

# Prueba para verificar que la entrada con espacios en blanco se procesa correctamente
def test_valid_input_spaces(manager):
    manager.add_beverage("       Soda        ,   1  ,  2,    3 ,  4 ")
    assert len(manager.beverages) == 1  # Verifica que se haya agregado una bebida correctamente
    assert manager.beverages[0].name == "Soda"  # Verifica que el nombre se haya procesado correctamente
    assert manager.beverages[0].sizes == [1, 2, 3, 4]  # Verifica que los tamaños se hayan procesado correctamente

# Prueba para verificar que la entrada con espacios en blanco en el nombre de la bebida no se acepta
def test_invalid_input_spaces(manager):
    manager.add_beverage("   ,   1  ,  2,    3 ,  4 ")
    assert len(manager.beverages) == 0  # Verifica que no se haya agregado ninguna bebida
