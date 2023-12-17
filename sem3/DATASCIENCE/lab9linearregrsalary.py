import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

data=pd.read_csv('/content/drive/MyDrive/dataset/Salary_Data - Salary_Data.csv')

print(data)

X=data[['YearsExperience']]
y=data['Salary']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

model=LinearRegression()

model.fit(X_train, y_train)

x_pred=model.predict(X_train)
y_pred=model.predict(X_test)

import matplotlib.pyplot as mtp
mtp.scatter(X_train, y_train, color="green")
mtp.plot(X_train, x_pred, color="red")
mtp.title("Salary vs Experience (Training Dataset)")
mtp.xlabel("Years of Experience")
mtp.ylabel("Salary(In Rupees)")
mtp.show()

#visualizing the Test set results
mtp.scatter(X_test, y_test, color="blue")
mtp.plot(X_train, x_pred, color="red")
mtp.title("Salary vs Experience (Test Dataset)")
mtp.xlabel("Years of Experience")
mtp.ylabel("Salary(In Rupees)")
mtp.show()

# Evaluate the model
mse = mean_squared_error(y_test, y_pred)
rmse = (mse ** 0.5)
r2 = r2_score(y_test, y_pred)

# Print the model's coefficients and evaluation metrics
print("Coefficients:", model.coef_)
print("Intercept:", model.intercept_)
print("Mean Squared Error:", mse)
print("Root Mean Squared Error:", rmse)
print("R-squared (R2) Score:", r2)

years_of_experience = float(input("Enter years of experience: "))
input_data = pd.DataFrame({'YearsExperience': [years_of_experience]})
predicted_salary = model.predict(input_data)
print(f"Predicted Salary for {years_of_experience} years of experience: rs {predicted_salary[0]:.2f}")