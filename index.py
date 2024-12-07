import pandas as pd

data1 = pd.read_csv('D:/capstone/data/nutrition.csv')

def recommend_foods(classification):
    if classification == "Severely Stunting":
        print('A Recommendation Nutrition for Severely Stunting')
        criteria = (data1['calories'] > 300) & (data1['proteins'] > 20)
    elif classification == "Stunting":
        print('A Recommendation Nutrition for Stunting')
        criteria = (data1['calories'] > 200) & (data1['proteins'] > 10)
    elif classification == "Normal":
        print('A Recommendation Nutrition for Normal')
        criteria = (data1['calories'] <= 200) & (data1['calories'] > 100)
    elif classification == "High":
        print('A Recommendation Nutrition for High')
        criteria = (data1['calories'] > 500)
    else:
        return "Invalid classification"

    recommended = data1[criteria]

    food_categories = {
        'Meat': [],
        'Vegetable': [],
        'Fruit': [],
        'Dairy': [],
        'Grain': [],
        'Others': []
    }

    for index, row in recommended.iterrows():
        if 'daging' in row['name'].lower():
            food_categories['Meat'].append({'Name': row['name'], 'Calories': row['calories'], 'Proteins': row['proteins']})
        elif 'sayur' in row['name'].lower():
            food_categories['Vegetable'].append({'Name': row['name'], 'Calories': row['calories'], 'Proteins': row['proteins']})
        elif 'buah' in row['name'].lower():
            food_categories['Fruit'].append({'Name': row['name'], 'Calories': row['calories'], 'Proteins': row['proteins']})
        elif 'susu' in row['name'].lower() or 'dairy' in row['name'].lower():
            food_categories['Dairy'].append({'Name': row['name'], 'Calories': row['calories'], 'Proteins': row['proteins']})
        elif 'beras' in row['name'].lower() or 'roti' in row['name'].lower():
            food_categories['Grain'].append({'Name': row['name'], 'Calories': row['calories'], 'Proteins': row['proteins']})
        else:
            food_categories['Others'].append({'Name': row['name'], 'Calories': row['calories'], 'Proteins': row['proteins']})

    recommendations = []
    for category in food_categories:
        if food_categories[category]:
            recommendations.append(food_categories[category][0])  

    return recommendations

classification_input = input('Enter your classification (Severely Stunting, Stunting, Normal, High): ') 
recommended_foods = recommend_foods(classification_input)

if recommended_foods:
    recommendations_df = pd.DataFrame(recommended_foods)
    print(recommendations_df.to_string(index=False))
else:
    print("No recommendations found.")