class Calculator:
    def __init__(self, equation):
        self.equation = equation

    def evaluate(self):
        try:
            # factorial
            if "!" in self.equation:
                num = self.equation.split("!")[0]
                num = int(num)
                result = 1
                for i in range(1, num + 1):
                    result *= i
                return result
            else:
                # other calculations
                return eval(self.equation)
        except SyntaxError:
            result = "Invalid equation"
        return result




