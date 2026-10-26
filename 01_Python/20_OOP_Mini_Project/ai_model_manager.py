
# AI Model Management System
# Program 1: Create and display an AI model

class AIModel:
    def __init__(self, name, algorithm, accuracy):
        self.name = name
        self.algorithm = algorithm
        self.accuracy = accuracy

    def __str__(self):
        return (
            f"Model: {self.name} | "
            f"Algorithm: {self.algorithm} | "
            f"Accuracy: {self.accuracy}%"
        )


model1 = AIModel("Salary Predictor", "Linear Regression", 89.5)
model2 = AIModel("Spam Detector", "Random Forest", 94.2)

print(model1)
print(model2)


# Program 2: AI Model Registry

class AIModelRegistry:
    def __init__(self):
        self.models = []

    def register_model(self, model):
        self.models.append(model)
        print(f"Registered: {model.name}")

    def display_models(self):
        print("\n--- Registered AI Models ---")

        for model in self.models:
            print(model)

    def total_models(self):
        return len(self.models)


# Create model objects
model1 = AIModel("Salary Predictor", "Linear Regression", 89.5)
model2 = AIModel("Spam Detector", "Random Forest", 94.2)
model3 = AIModel("Customer Groups", "K-Means", 87.0)

# Create registry
registry = AIModelRegistry()

# Register models
registry.register_model(model1)
registry.register_model(model2)
registry.register_model(model3)

# Display registered models
registry.display_models()

print("\nTotal models:", registry.total_models())


# Program 3: Encapsulation and Validation

class SecureAIModel:
    def __init__(self, name, algorithm, accuracy):
        self.name = name
        self.algorithm = algorithm
        self.__accuracy = None
        self.set_accuracy(accuracy)

    def get_accuracy(self):
        return self.__accuracy

    def set_accuracy(self, accuracy):
        if isinstance(accuracy, (int, float)) and not isinstance(accuracy, bool) and 0 <= accuracy <= 100:
            self.__accuracy = accuracy
            print("Accuracy updated successfully.")
        else:
            print("Error: Accuracy must be between 0 and 100.")

    def __str__(self):
        return (
            f"Model: {self.name} | "
            f"Algorithm: {self.algorithm} | "
            f"Accuracy: {self.__accuracy}%"
        )


# Create a secure model
secure_model = SecureAIModel(
    "Image Classifier",
    "CNN",
    96.5
)

print(secure_model)
print("Current accuracy:", secure_model.get_accuracy())

# Try valid and invalid updates
secure_model.set_accuracy(98)
secure_model.set_accuracy(150)

print("Final accuracy:", secure_model.get_accuracy())

