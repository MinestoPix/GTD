class Task(object):
    # Tasks will be individual entities, one for each thing to achieve
    modifiers = {
        "priority": 1,
        "test": 1
    }

    def __init__(self, priority=None):
        self.priority = priority

    def weight(self):
        sum_weight = 0
        if self.priority:
            sum_weight += self.priority * self.modifiers["priority"]
        return sum_weight

    def prioritize_above(self, stronger_task):
        if stronger_task.weight() > self.weight():
            return False
