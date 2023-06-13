# Создайте класс с тестами и напишите фикстуры в conftest.py:
# 1) Фикстуру для класса и используйте её. Например, печать времени начала выполнения класса с тестами и окончания
# 2) Фикстуру для конкретного теста и используйте её не для всех тестов. Например, время выполнения теста.
import pytest


@pytest.mark.usefixtures("start_end_time")
class TestExample:
    def test_1(self):
        pass

    def test_2(self, execution_time):
        pass

    def test_3(self):
        pass

    def test_4(self, execution_time):
        pass

    def test_5(self):
        pass
