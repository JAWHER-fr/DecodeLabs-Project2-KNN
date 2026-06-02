import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix, classification_report, f1_score


print("🤖 PROJECT 2: INITIALIZING MACHINE LEARNING PIPELINE")
print("==================================================================")

# 1. INPUT PHASE: Load the Iris Benchmark Dataset
iris = load_iris()
X = iris.data  # Features: Sepal/Petal Length & Width
y = iris.target  # Classes: Setosa, Versicolor, Virginica

# 2. PROCESS PHASE: Structural Integrity (Shuffle & Split 80%-20%)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.20, random_state=42, shuffle=True
)

# 3. GATEKEEPER RULE: Feature Scaling using StandardScaler
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# 4. MODEL TUNING: Instantiate & Train KNN Classifier (K=5)
print("🤖 Model Status: Training K-Nearest Neighbors Classifier (K=5)...")
model = KNeighborsClassifier(n_neighbors=5)
model.fit(X_train_scaled, y_train)

# 5. PREDICTION LAYER
predictions = model.predict(X_test_scaled)

# 6. OUTPUT VALIDATION: Diagnostic Tools (Confusion Matrix & F1-Score)
print("\n==================================================================")
print("📊 OUTPUT EVALUATION METRICS")
print("==================================================================")

# Generate Confusion Matrix (TP, FP, FN, TN)
conf_matrix = confusion_matrix(y_test, predictions)
print("📋 Confusion Matrix:")
print(conf_matrix)

# Calculate F1 Score & Print Complete Report
macro_f1 = f1_score(y_test, predictions, average='macro')
print(f"\n🎯 Macro F1-Score: {macro_f1:.4f}")

print("\n📝 Detailed Classification Report:")
print(classification_report(iris.target_names, y_test, target_names=iris.target_names))
