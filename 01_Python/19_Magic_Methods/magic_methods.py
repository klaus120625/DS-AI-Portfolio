
#Program 1: __str__() Method

class Student:
    def __init__(self, name, course, score):
        self.name = name
        self.course = course
        self.score = score

    def __str__(self):
        return (
            f"Student: {self.name} | "
            f"Course: {self.course} | "
            f"Score: {self.score}"
        )


student = Student("Alex", "AI Engineering", 92)

print(student)
print(str(student))




#Program 2: __len__() Method

class Dataset:
    def __init__(self, name, records):
        self.name = name
        self.records = records

    def __len__(self):
        return len(self.records)


dataset = Dataset(
    "Salary Dataset",
    [45000, 52000, 61000, 70000, 85000]
)

print("Dataset name:", dataset.name)
print("Number of records:", len(dataset))




#Program 3: __add__() Method

class DatasetBatch:
    def __init__(self, name, records):
        self.name = name
        self.records = records

    def __add__(self, other):
        combined_records = self.records + other.records
        return DatasetBatch(
            "Combined Dataset",
            combined_records
        )


batch1 = DatasetBatch("Training Batch 1", [10, 20, 30])
batch2 = DatasetBatch("Training Batch 2", [40, 50, 60])

combined = batch1 + batch2

print("Dataset name:", combined.name)
print("Combined records:", combined.records)
print("Total records:", len(combined.records))


