import unittest
from primer_12_4 import Runner
import logging

logging.basicConfig(level=logging.INFO, filemode='w', filename='runner_tests.log', encoding='UTF-8',
                        format='%(asctime)s | %(levelname)s | %(message)s')

class RunnerTest(unittest.TestCase):

    def test_walk(self):

        """ Тест метода walk. Создаем объект класса Runner. Вызываем метод walk 10 раз.
        Сравниваем аттрибут distance этого со значением 50 """

        try:
            runner_1 = Runner('Ivan', -10) # Отрицательная скорость

            for i in range(10):
                runner_1.walk()

            self.assertEqual(runner_1.distance, 50)
            logging.info('"test_walk" выполнен успешно')

        except ValueError:
            logging.warning('Неверная скорость для Runner')
            raise ValueError(f'Скорость не может быть отрицательной, сейчас')

    def test_run(self):

        """ Тест метода run. Вызываем метод run 10 раз. Создаем объект класса Runner.
        Сравниваем аттрибут distance этого со значением 100 """

        try:
            runner_2 = Runner(False, 10) # Некорректное имя

            for i in range(10):
                runner_2.run()

            self.assertEqual(runner_2.distance, 100)
            logging.info('"test_run" выполнен успешно')
        except TypeError:
            logging.warning('Неверный тип данных для объекта Runner')
            raise TypeError(f'Имя должно быть строкой, передано {type(runner_2.name).__name__}')


if __name__ == '__main__':
    unittest.main()
