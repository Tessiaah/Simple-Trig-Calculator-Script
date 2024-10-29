from sympy import *


class Calculator:

    @staticmethod
    def main():
        solutions = [sympify(input("Enter the first solution: ")), (sympify(input("Enter the second solution: ")))]
        lower_bound = input("Inter the lower bound using interval notation (e.g. [3 or ]3): ")
        upper_bound = input("Inter the upper bound using interval notation (e.g. 3] or 3[): ")
        solutions = Calculator.solver(solutions, lower_bound, upper_bound)
        print(solutions)

    @staticmethod
    def solver(solutions: list, lbound: str, ubound: str):
        new_solutions =[]

        if lbound.startswith("[") and ubound.endswith("]"):
            lbound = sympify(lbound[1:])
            ubound = sympify(ubound[:-1])
            for i in solutions:
                for j in range(-5, 11):
                    if lbound <= i+sympify(f"2*pi*{j}") <= ubound:
                        new_solutions.append(i+sympify(f"2*pi*{j}"))

        elif lbound.startswith("[") and ubound.endswith("["):
            lbound = sympify(lbound[1:])
            ubound = sympify(ubound[:-1])
            for i in solutions:
                for j in range(-5, 11):
                    if lbound <= i+sympify(f"2*pi*{j}") < ubound:
                        new_solutions.append(i+sympify(f"2*pi*{j}"))

        elif lbound.startswith("]") and ubound.endswith("]"):
            lbound = sympify(lbound[1:])
            ubound = sympify(ubound[:-1])
            for i in solutions:
                for j in range(-5, 11):
                    if lbound < i+sympify(f"2*pi*{j}") <= ubound:
                        new_solutions.append(i+sympify(f"2*pi*{j}"))

        elif lbound.startswith("]") and ubound.endswith("["):
            lbound = sympify(lbound[1:])
            ubound = sympify(ubound[:-1])
            for i in solutions:
                for j in range(-5, 11):
                    if lbound < i+sympify(f"2*pi*{j}") < ubound:
                        new_solutions.append(i+sympify(f"2*pi*{j}"))

        return new_solutions




Calculator.main()