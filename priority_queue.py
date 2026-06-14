import heapq


class Task:
    def __init__(self, task_id, priority, arrival_time, deadline):
        self.task_id = task_id
        self.priority = priority
        self.arrival_time = arrival_time
        self.deadline = deadline

    def __lt__(self, other):
        return self.priority < other.priority


class PriorityQueue:
    def __init__(self):
        self.heap = []

    def insert(self, task):
        heapq.heappush(self.heap, task)

    def extract_min(self):
        if not self.is_empty():
            return heapq.heappop(self.heap)
        return None

    def decrease_key(self, task_id, new_priority):
        for task in self.heap:
            if task.task_id == task_id:
                task.priority = new_priority
                heapq.heapify(self.heap)
                break

    def increase_key(self, task_id, new_priority):
        for task in self.heap:
            if task.task_id == task_id:
                task.priority = new_priority
                heapq.heapify(self.heap)
                break

    def is_empty(self):
        return len(self.heap) == 0


# Test Code
if __name__ == "__main__":
    pq = PriorityQueue()

    pq.insert(Task("T1", 2, "09:00", "12:00"))
    pq.insert(Task("T2", 1, "09:10", "11:00"))
    pq.insert(Task("T3", 4, "09:20", "15:00"))
    pq.insert(Task("T4", 3, "09:30", "14:00"))

    pq.decrease_key("T3", 0)

    while not pq.is_empty():
        task = pq.extract_min()
        print(task.task_id, task.priority)