trainees = [
    {"name": "Sara", "checkin": "09:40", "on_time": 5, "report_on_time": False, "scores": [8, 8, 8, 8, 8]},
    {"name": "Omar", "checkin": "10:15", "on_time": 4, "report_on_time": True, "scores": [9, 9, 9, 9, 0]},
    {"name": "Lina", "checkin": "08:55", "on_time": 5, "report_on_time": True, "scores": [10, 9, 9, 10, 8]}
]

total_tasks = 5


# تحويل الوقت إلى دقائق
def to_minutes(time_text):
    time = time_text.split(":")
    return int(time[0]) * 60 + int(time[1])


# حساب النقاط
def daily_points(checkin, on_time, total_tasks, report_on_time, scores):
    points = 0

    if to_minutes(checkin) < 600:
        points += 10

    if total_tasks > 0:
        points += (on_time / total_tasks) * 10

        total = 0
        for score in scores:
            total += score

        points += (total / (total_tasks * 10)) * 10

    if report_on_time:
        points += 5

    return round(points, 2)


# حساب نقاط المتدربين
for trainee in trainees:
    trainee["points"] = daily_points(
        trainee["checkin"],
        trainee["on_time"],
        total_tasks,
        trainee["report_on_time"],
        trainee["scores"]
    )

    print(trainee["name"], trainee["points"])


# حساب المتوسط
total = 0

for trainee in trainees:
    total += trainee["points"]

print("Average:", round(total / len(trainees), 2))


# أفضل متدرب
best = trainees[0]

for trainee in trainees:
    if trainee["points"] > best["points"]:
        best = trainee

print("Best of the Day:", best["name"])


# إضافة متدرب جديد
trainees.append({
    "name": "Me",
    "checkin": "09:00",
    "on_time": 5,
    "report_on_time": True,
    "scores": [10, 10, 10, 9, 9]
})

me = trainees[3]

me["points"] = daily_points(
    me["checkin"],
    me["on_time"],
    total_tasks,
    me["report_on_time"],
    me["scores"]
)

print("My points:", me["points"])
print("Difference:", round(me["points"] - trainees[2]["points"], 2))


# اختبار يوم بدون مهام
print("No tasks:", daily_points("09:00", 0, 0, True, []))