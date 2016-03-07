import unittest

import scheduled_task as st


class MyTestCase(unittest.TestCase):
    def test_priority(self):
        priority = 0
        scheduled_task = st.Task(priority=priority)
        self.assertEqual(scheduled_task.priority, priority)

    def test_priority_weight(self):
        priority = 1
        scheduled_task = st.Task(priority=priority)
        self.assertEqual(scheduled_task.weight(), priority)

    def test_prioritize_above_objectively_stronger_task(self):
        scheduled_task = st.Task(priority=1)
        scheduled_task_stronger = st.Task(priority=2)
        succeeded = scheduled_task.prioritize_above(scheduled_task_stronger)
        self.assertFalse(succeeded)


if __name__ == '__main__':
    unittest.main()
