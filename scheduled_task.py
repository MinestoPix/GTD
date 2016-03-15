class Task(object):
    # Tasks will be individual entities, one for each thing to achieve
    modifiers = {
        "priority": 1,
        "test": 1
    }

    def __init__(self, priority=0):
        self.attributes = {"priority": priority}

    def weight(self):
        sum_weight = 0
        for (key, value) in self.attributes.items():
            sum_weight += value * self.modifiers[key]
        return sum_weight

    def prioritize_above(self, other_task):
        stronger = False
        for (key, value) in self.attributes.items():
            if value > other_task.attributes[key]:
                stronger = True
        return stronger
