import pandas as pd
import numpy as np
from catboost import CatBoostRegressor

# Load the data
df = pd.read_csv('filtered_train.csv') 
df = df.fillna(0) # Fill missing values with 0 (if still exist)

# Define the target variable y and feature set x for 2022 data
drop_columns = ['Anne Calisma Durumu','Baba Calisma Durumu','Daha Once Baska Bir Universiteden Mezun Olmus','Degerlendirme Puani', 'Basvuru Yili']
y = df['Degerlendirme Puani']
x = df.drop(columns= drop_columns)

# Create and train the CatBoost model
catboost_model = CatBoostRegressor(verbose = 0)  # 'verbose = 0' to suppress output during training
model = catboost_model.fit(x, y)

model_score = model.score(x, y)
# Print the model score
print("CatBoost Model Score:", model_score)

# Load the new data for prediction
df_test = pd.read_csv('filtered_test_x.csv')
df_test.fillna(0, inplace = True)

# Predict using the CatBoost model
test_drop_columns = ['Anne Calisma Durumu','Baba Calisma Durumu','Daha Once Baska Bir Universiteden Mezun Olmus','Basvuru Yili']
results = model.predict(df_test.drop(columns = test_drop_columns))

# Round the predictions to the nearest integer
results = np.round(results)

# Create a DataFrame with the ID and predictions
df_result = pd.DataFrame({
    'id': df_test.index,
    'Degerlendirme Puani': results
})

# Save the results to a new CSV file
df_result.to_csv('submission_result.csv', index=False)