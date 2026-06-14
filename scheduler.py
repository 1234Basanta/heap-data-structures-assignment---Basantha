from priority_queue import PriorityQueue, Task

pq = PriorityQueue()

pq.insert(Task("Email", 3, "08:00", "17:00"))
pq.insert(Task("Report", 1, "08:30", "12:00"))
pq.insert(Task("Meeting", 2, "09:00", "13:00"))
pq.insert(Task("Presentation", 4, "10:00", "16:00"))

print("Task Execution Order:")

while not pq.is_empty():
    task = pq.extract_min()
    print(
        f"{task.task_id} | Priority {task.priority} | "
        f"Arrival {task.arrival_time} | Deadline {task.deadline}"
    )