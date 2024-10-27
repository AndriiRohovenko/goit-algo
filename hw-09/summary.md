# Порівняння жадібних алгоритмів та алгоритмів динамічного програмування для задачі видачі решти

## Вступ

Метою цього завдання є порівняння двох підходів для задачі видачі решти на основі суми та наявних номіналів монет:
1. **Жадібний алгоритм** – на кожному кроці вибирає найбільший номінал, що не перевищує залишок суми.
2. **Алгоритм динамічного програмування** – аналізує всі можливі комбінації номіналів для оптимального результату.

Кожен з цих методів має свої плюси і мінуси. Ми порівняємо їх, щоб зрозуміти, який алгоритм більш ефективний для різних типів задач.

## Опис методів

### Жадібні алгоритми

1. **Greedy Coin Change 1** і **Greedy Coin Change 2**:
   - Обидва жадібні алгоритми працюють однаково: для кожного номіналу монети перевіряють, скільки разів можна використати цей номінал, починаючи з найбільшого.
   - Жадібний підхід підходить для простих випадків, де всі номінали є кратними. Наприклад, для номіналів `[1, 5, 10, 25, 50, 100, 200]` та суми 1000 вони просто вибирають 5 монет по 200.

### Алгоритми динамічного програмування

1. **Memoized DP** (`find_min_coins_memo`):
   - Цей алгоритм використовує рекурсію та зберігає проміжні результати (мемоізацію) для уникнення повторних обчислень.
   - Він підходить для складніших наборів номіналів, де жадібний підхід не завжди дає оптимальний результат.

2. **Bottom-Up DP** (`find_min_coins`):
   - Цей алгоритм поступово будує рішення для всіх можливих підсум до цільової суми, використовуючи метод "знизу-вгору".
   - Він також підходить для складних випадків і забезпечує оптимальне рішення для будь-якого набору номіналів.

## Результати тестування

Ми протестували кожен з алгоритмів на сумі **113** з номіналами `[50, 25, 10, 5, 2, 1]`. Ось результати:

- **Greedy Coin Change 1**: знайшов рішення `{50: 2, 10: 1, 2: 1, 1: 1}`, використавши 5 монет. Виконання зайняло невеликий час, оскільки алгоритм швидко знайшов відповідь.
- **Greedy Coin Change 2**: показав аналогічний результат, також знайшовши `{50: 2, 10: 1, 2: 1, 1: 1}` з 5 монетами.
- **Memoized DP**: знайшов оптимальне рішення `{50: 2, 10: 1, 2: 1, 1: 1}`, використавши 5 монет, за трохи довший час через рекурсію, але швидше завдяки мемоізації.
- **Bottom-Up DP**: також знайшов `{50: 2, 10: 1, 2: 1, 1: 1}` з мінімальною кількістю 5 монет, будуючи рішення поступово без рекурсії і працюючи досить швидко.


### Продуктивність на великих суммах

- **Жадібні алгоритми**: мають складність \(O(n)\), де \(n\) – кількість номіналів, оскільки проходять по кожному номіналу один раз. Для великих сум і простих наборів номіналів жадібні алгоритми є дуже швидкими.
  
- **Алгоритми динамічного програмування**: мають складність \(O(n \times M)\), де \(M\) – сума, яку потрібно видати. Хоча динамічне програмування виконується довше, воно забезпечує оптимальність для всіх випадків, особливо коли номінали не кратні.

### Висновок

- **Жадібний підхід** підходить для простих і великих сум, якщо номінали є кратними один одному.
- **Динамічне програмування** підходить для випадків, де необхідна точна мінімізація кількості монет, незалежно від структури номіналів.

У більш складних ситуаціях динамічне програмування є кращим вибором, тоді як жадібний підхід працює швидше, але підходить лише для обмежених випадків.