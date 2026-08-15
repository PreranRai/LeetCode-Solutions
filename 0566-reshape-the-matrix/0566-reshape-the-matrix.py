class Solution(object):
    def matrixReshape(self, mat, r, c):
        """
        :type mat: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        m = len(mat)
        n = len(mat[0])

        # Cannot reshape if the number of elements is different
        if m * n != r * c:
            return mat

        result = [[0] * c for _ in range(r)]

        for i in range(m):
            for j in range(n):
                index = i * n + j
                result[index // c][index % c] = mat[i][j]

        return result