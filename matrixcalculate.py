class MatrixCalculate:
    def __init__(self, matrix):
        self.matrix = matrix
        self.row = len(self.matrix)
        self.column = len(self.matrix[0])


    def __add__(self, other):
        matrix = []
        for row in range(self.row):
            matrix.append([])
            for column in range(self.column):
                matrix[row].append(self.matrix[row][column] + other.matrix[row][column])
        return matrix

    def __sub__(self, other):
        matrix = []
        for row in range(self.row):
            matrix.append([])
            for column in range(self.column):
                matrix[row].append(self.matrix[row][column] - other.matrix[row][column])
        return matrix

    def __mul__(self, other):
        matrix = []
        for row in range(self.row):
            matrix.append([])
            for column in range(other.column):
                matrix[row].append(0)

        for row in range(self.row):
            for column in range(other.column):
                for equivalent_number in range(self.column):
                    matrix[row][column] += self.matrix[row][equivalent_number] * other.matrix[equivalent_number][column]
        return matrix

    def print(self):
        print(self.matrix)


if __name__ == "__main__":
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    m1 = MatrixCalculate(matrix)
    m2 = MatrixCalculate(matrix)
    m3 = m1 * m2
    print(m3)
