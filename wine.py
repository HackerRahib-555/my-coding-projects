import pandas as pd
from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn import tree
import matplotlib.pyplot as plt
import time

time_limit = 600
time_spent = time.time()

wine = load_wine()
while time.time() - time_spent < time_limit:
    
    df = pd.DataFrame(wine.data, columns=wine.feature_names)
    df['target'] = wine.target

# Step 3: Split the dataset into training and testing sets
    X = df.drop('target', axis=1)  # Features
    y = df['target']  # Target labels
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 4: Train the Decision Tree model
    model = DecisionTreeClassifier(random_state=42)
    model.fit(X_train, y_train)

# Step 5: Make predictions
    y_pred = model.predict(X_test)

# Step 6: Evaluate the model
    accuracy = accuracy_score(y_test, y_pred)
    conf_matrix = confusion_matrix(y_test, y_pred)

    print(f"Accuracy: {accuracy}")
    print(f"Confusion Matrix:\n{conf_matrix}")

# Step 7: Visualize the decision tree (optional)
    plt.figure(figsize=(12,8))
    tree.plot_tree(model, feature_names=wine.feature_names, class_names=wine.target_names, filled=True, rounded=True)
    plt.show()
