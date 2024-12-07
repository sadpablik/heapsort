import unittest

def heapify(arr, n, i):
    largest = i  # Инициализируем наибольший элемент как корень
    left = 2 * i + 1  # левый = 2*i + 1
    right = 2 * i + 2  # правый = 2*i + 2

    # Если левый дочерний элемент больше корня
    if left < n and arr[i] < arr[left]:
        largest = left

    # Если правый дочерний элемент больше, чем самый большой элемент на данный момент
    if right < n and arr[largest] < arr[right]:
        largest = right

    # Если самый большой элемент не корень
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # поменять местами

        # Рекурсивно heapify поддерево
        heapify(arr, n, largest)

def heapsort(arr):
    n = len(arr)

    # Построение max-heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Извлечение элементов из кучи
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]  # Переместить текущий корень в конец
        heapify(arr, i, 0)               # Восстановить кучу для оставшихся элементов

# Тесты
class TestHeapSort(unittest.TestCase):

    def test_sorted_array(self):
        """Тест уже отсортированного массива"""
        arr = [1, 2, 3, 4, 5]
        heapsort(arr)
        self.assertEqual(arr, [1, 2, 3, 4, 5])

    def test_reverse_sorted_array(self):
        """Тест массива, отсортированного в обратном порядке"""
        arr = [5, 4, 3, 2, 1]
        heapsort(arr)
        self.assertEqual(arr, [1, 2, 3, 4, 5])

    def test_unsorted_array(self):
        """Тест неотсортированного массива"""
        arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
        heapsort(arr)
        self.assertEqual(arr, sorted(arr))

    def test_empty_array(self):
        """Тест пустого массива"""
        arr = []
        heapsort(arr)
        self.assertEqual(arr, [])

    def test_single_element_array(self):
        """Тест массива с одним элементом"""
        arr = [42]
        heapsort(arr)
        self.assertEqual(arr, [42])

    def test_duplicates(self):
        """Тест массива с дубликатами"""
        arr = [4, 2, 4, 2, 4, 2]
        heapsort(arr)
        self.assertEqual(arr, [2, 2, 2, 4, 4, 4])

    def test_large_array(self):
        """Тест большого массива"""
        arr = list(range(1000, 0, -1))  # массив от 1000 до 1
        heapsort(arr)
        self.assertEqual(arr, list(range(1, 1001)))

# Запуск тестов
if __name__ == "__main__":
    # unittest.main() - для использования тестов
    arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    print(f"Original array: {arr}")
    heapsort(arr)
    print(f"Sorted array: {arr}")
