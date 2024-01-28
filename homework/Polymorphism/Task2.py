"""
Создать базовый класс ОЛИМПИАДНЫЕ ЗАДАНИЯ (данные об участнике, количество тестовых примеров,
количество пройденных тестов).
Создать производные классы ЗАДАНИЯ «ВСЕ ИЛИ НИЧЕГО»
(задается максимальное количество баллов за задание (даются только когда все тесты пройдены)
и ЗАДАНИЯ «ЧЕМ БЫСТРЕЕ, ТЕМ ЛУЧШЕ» (задается время участника на решение,
лучшее время всех участников, максимальное количество баллов за задание,
процент снижения балла в минуту отставания от лучшего времени).
Для заданных примеров задач, которые решали участники,
упорядочить участников по росту набранных баллов и определить суммарное количество баллов,
набранных заданным участником олимпиады.
Для проверки использовать действия над списком,
в котором разместить объекты разных производных классов.
"""

class OlympiadTasks:
    def __init__(self, participant_data, num_test_cases, num_passed_tests):
        self.participant_data = participant_data
        self.num_test_cases = num_test_cases
        self.num_passed_tests = num_passed_tests

    def total_points(self):
        raise NotImplementedError("Метод должен быть переопределен в производных классах")


class AllOrNothingTask(OlympiadTasks):
    def __init__(self, participant_data, num_test_cases, num_passed_tests, max_points):
        super().__init__(participant_data, num_test_cases, num_passed_tests)
        self.max_points = max_points

    def total_points(self):
        if self.num_passed_tests == self.num_test_cases:
            return self.max_points
        else:
            return 0


class FastestTask(OlympiadTasks):
    def __init__(self, participant_data, num_test_cases, num_passed_tests, time_taken, best_time, max_points, point_reduction):
        super().__init__(participant_data, num_test_cases, num_passed_tests)
        self.time_taken = time_taken
        self.best_time = best_time
        self.max_points = max_points
        self.point_reduction = point_reduction

    def total_points(self):
        points = self.max_points
        if self.time_taken > self.best_time:
            time_difference = self.time_taken - self.best_time
            points -= time_difference * self.point_reduction
        return points


# Пример использования
all_or_nothing_task1 = AllOrNothingTask("Участник1", 5, 5, 10)
fastest_task1 = FastestTask("Участник1", 10, 7, 25, 20, 15, 0.5)

all_or_nothing_task2 = AllOrNothingTask("Участник2", 5, 4, 10)
fastest_task2 = FastestTask("Участник2", 10, 8, 23, 20, 15, 0.5)

task_list = [all_or_nothing_task1, fastest_task1, all_or_nothing_task2, fastest_task2]

sorted_by_points = sorted(task_list, key=lambda x: x.total_points(), reverse=True)
for task in sorted_by_points:
    print(f"Участник {task.participant_data} набрал {task.total_points()} баллов.")