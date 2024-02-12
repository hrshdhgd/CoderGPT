"""Test python code."""

def calculate_sum(numbers):
    """
    Calculate the sum of a list of numbers.

    :param numbers: A list of numbers.
    :type numbers: list[int]
    :return: The sum of the numbers.
    :rtype: int
    """
    result = 0
    for number in numbers:
        result += number
    return result


class MathOperations:
    def multiply(self, a, b):
        """
        Multiply two numbers.

        :param a: The first number.
        :type a: int
        :param b: The second number.
        :type b: int
        :return: The product of the two numbers.
        :rtype: int
        """
        answer = 0
        for i in range(b):
            answer += a
        return answer
