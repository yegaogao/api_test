class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score


def avg_score(students):
    if not students:
        raise ValueError("学生列表不能为空")
    return sum(s.score for s in students) / len(students)


students = [
    Student("张三", 88),
    Student("李四", 92),
    Student("王五", 75),
]

try:
    print("平均分：", avg_score(students))
    score_map = {s.name: s.score for s in students}
    print("成绩字典：", score_map)
    with open("students.txt", "w", encoding="utf-8") as f:
        for s in students:
            f.write(f"{s.name},{s.score}\n")
except Exception as e:
    print("出错了：", e)
finally:
    print("程序结束")

with open("students.txt", "r", encoding="utf-8") as f:
    print(f.read())