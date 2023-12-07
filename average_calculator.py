class AverageCalculator:
    @staticmethod
    def calculate_average(lst):
        if not lst:
            return 0
        return sum(lst) / len(lst)

    @staticmethod
    def compare_averages(list1, list2):
        avg1 = AverageCalculator.calculate_average(list1)
        avg2 = AverageCalculator.calculate_average(list2)

        if avg1 > avg2:
            return "Первый список имеет большее среднее значение"
        elif avg2 > avg1:
            return "Второй список имеет большее среднее значение"
        else:
            return "Средние значения равны"
