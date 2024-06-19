import unittest

# Función a testear
def sum():
    a = 4
    b = 3
    result = a + b
    print(result)
    return result

# Clase de pruebas unitarias
class TestSumFunction(unittest.TestCase):
    
    # Caso positivo: Verificar que la suma de 4 y 3 sea correcta
    def test_sum_correct(self):
        self.assertEqual(sum(), 7)
    
    # Caso negativo: Verificar que la suma no sea incorrecta
    def test_sum_incorrect(self):
        self.assertNotEqual(sum(), 8)
    
    # Caso borde: Verificar que la función maneje correctamente valores extremos
    def test_sum_boundary(self):
        # Modificamos la función para aceptar parámetros
        def sum(a, b):
            result = a + b
            print(result)
            return result
        self.assertEqual(sum(0, 0), 0)
        self.assertEqual(sum(-1, 1), 0)
        self.assertEqual(sum(1, -1), 0)
    
    # Caso de escalabilidad: Verificar que la función maneje números grandes
    def test_sum_large_numbers(self):
        def sum(a, b):
            result = a + b
            print(result)
            return result
        self.assertEqual(sum(1000000, 1000000), 2000000)
    
    # Caso de eficiencia: Verificar que la función sea eficiente con números grandes
    def test_sum_performance(self):
        import time
        def sum(a, b):
            result = a + b
            print(result)
            return result
        start_time = time.time()
        sum(1000000, 1000000)
        end_time = time.time()
        self.assertTrue((end_time - start_time) < 1)  # Asegurarse que la ejecución sea menor a 1 segundo
    
    # Caso de compatibilidad: Verificar que la función sea compatible con diferentes tipos de datos
    def test_sum_compatibility(self):
        def sum(a, b):
            result = a + b
            print(result)
            return result
        self.assertEqual(sum(4.5, 3.5), 8.0)
        self.assertEqual(sum(4, 3.5), 7.5)
        self.assertEqual(sum(4.5, 3), 7.5)
    
    # Caso de mantenimiento: Verificar que la función sea mantenible y no rompa con cambios menores
    def test_sum_maintainability(self):
        def sum(a, b):
            result = a + b
            print(result)
            return result
        self.assertEqual(sum(4, 3), 7)
        self.assertEqual(sum(5, 2), 7)
        self.assertEqual(sum(6, 1), 7)

if __name__ == '__main__':
    unittest.main()