import pulp

model = pulp.LpProblem("Maximize_Production", pulp.LpMaximize)
lemonade = pulp.LpVariable("Lemonade", lowBound=0, cat="Integer")
fruit_juice = pulp.LpVariable("Fruit_Juice", lowBound=0, cat="Integer")

# Цільова функція: максимізувати загальну кількість продуктів (лимонад + фруктовий сік)
model += lemonade + fruit_juice, "Total_Production"

# Обмеження на ресурси
model += 2 * lemonade + fruit_juice <= 100, "Water_Limit"
model += lemonade <= 50, "Sugar_Limit"
model += lemonade <= 30, "Lemon_Juice_Limit"
model += 2 * fruit_juice <= 40, "Fruit_Puree_Limit"

model.solve()
print(f"Статус: {pulp.LpStatus[model.status]}")
print(f"Кількість лимонаду: {lemonade.varValue}")
print(f"Кількість фруктового соку: {fruit_juice.varValue}")
print(f"Максимальна кількість вироблених продуктів: {pulp.value(model.objective)}")
