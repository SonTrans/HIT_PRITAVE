students = [{"id": 1, "name": "An", "score": 8.5},{"id": 2, "name": "Bình", "score": 7.2},{"id": 3, "name": "Chi", "score": 9.0}]
def find_by_id(data, id):
    for sv in data:
        if sv["id"] == id:
            return sv
    return None
def filter_by_score(data, min_score):
    return [student for student in data if student["score"] >= min_score]
def sort_by_score(data, reverse=False):
    return sorted(data, key= lambda x:x['score'],reverse = reverse)
def add_student(data, student_dict):
    data.append(student_dict)  
def remove_student(data, id):
    data[:] = [sv for sv in data if id != sv["id"]]
def statistics(data):
    total_score = sum(student["score"] for student in data)
    mean_score = total_score / len(data)
    highest_score_student = max(data,key= lambda x: x["score"])
    lowest_score_student = min(data,key= lambda x: x["score"])
    return (mean_score, highest_score_student, lowest_score_student)
print(find_by_id(students, 2))
add_student(students, {"id":4, "name":"Dũng", "score":9.5})
print(filter_by_score(students, 8.0))
print(sort_by_score(students))
remove_student(students, 1)
print(students)
print(statistics(students))
