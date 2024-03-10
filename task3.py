
def quicksort(arr: list) -> list:
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quicksort(left) + middle + quicksort(right)


"""
Это реализация быстрой сортировки.
Быстрая сортировка обычно имеет среднюю сложность O(nlogn).
Однако, в худшем случае (когда массив уже отсортирован в обратном порядке), время выполнения может быть O(n^2).

Я считаю, что данная сортировка подходит больше всего, т.к. для большинства случаев она имеет хорошую сложность O(nlogn)
"""