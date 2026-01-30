import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
import random
import time

run_count = 0  
time_limit = 600
time_spent = time.time()

# Run the whole process twice
while time.time() - time_spent < time_limit:
    
    run_count += 1

    # Step 1: Generate dataset
    numbers = np.random.permutation(np.arange(1000))  # Randomly shuffled numbers 0-999 for quicker testing
    labels = numbers % 2  # 0 for even, 1 for odd

    # Step 2: Split the dataset
    X_train, X_test, y_train, y_test = train_test_split(
        numbers.reshape(-1, 1), labels, test_size=0.2, random_state=random.randint(0, 10000)
    )

    # Step 3: Train the Decision Tree model
    model = DecisionTreeClassifier()
    model.fit(X_train, y_train)

    # Step 4: Predict on test set
    y_pred = model.predict(X_test)

    # Step 5: Calculate and print accuracy
    accuracy = accuracy_score(y_test, y_pred)
    print(f"Accuracy (Run {run_count}): {accuracy * 100:.2f}%")

    # Step 6: Predict some new random numbers
    new_data = np.array([random.choice(range(1, 1000)) for _ in range(5)]).reshape(-1, 1)
    predictions = model.predict(new_data)

    # Step 7: Print the predictions
    print("New Data Predictions:")
    for num, pred in zip(new_data.flatten(), predictions):
        print(f"  Number: {num}, Predicted: {'Odd' if pred == 1 else 'Even'}")
    
    print("\n" + "-"*30 + "\n")