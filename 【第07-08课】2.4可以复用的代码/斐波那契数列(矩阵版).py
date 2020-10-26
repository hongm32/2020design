# 兔子问题
# 假设一对大兔子每个月可以生一对小兔子，一对小兔子出生后需1个月长大为大兔子。
# 则一对小兔子一年内能繁殖成多少对？10年呢？

def fib_matrix_power(n):
    matrix = [1, 1, 1, 0]
    result = 0
    if n > 0:
        matrix_power(matrix, n - 1)
        result = matrix[0]
    return result


# 2 x 2 matrix power
def matrix_power(mat, n):
    rows, cols = 2, 2  # 2 x 2 matrix
    if n <= 0:
        return None
    elif 0 == n:
        mat[:] = [1, 0, 0, 1]  # identity matrix
    elif 1 == n:
        pass
    elif 2 == n:
        tmp_mat1, tmp_mat2 = [], []
        tmp_mat1.extend(mat)
        tmp_mat2.extend(mat)
        # matrix multiplication
        for i in range(rows):
            for j in range(cols):
                mat[i * cols + j] = inner_product(tmp_mat1[i::cols], tmp_mat2[j::cols])
    elif n % 2 == 0:  # even case
        matrix_power(mat, n / 2)
        matrix_power(mat, 2)
    else:
        # temporarily save mat
        tmp_mat1 = []
        tmp_mat1.extend(mat)
        # recursive call
        matrix_power(mat, n - 1)
        # multiply with former temporary value
        tmp_mat2 = []
        tmp_mat2.extend(mat)
        for i in range(rows):
            for j in range(cols):
                mat[i * cols + j] = inner_product(tmp_mat1[i::cols], tmp_mat2[j::cols])
    return mat


def inner_product(vec1, vec2):
    product = 0
    if vec1 and vec2 and len(vec1) == len(vec2):
        for i in range(len(vec1)):
            product += vec1[i] * vec2[i]
    return product


num = int(input('输入需要计算的月份数：'))
print('兔子总对数为：', fib_matrix_power(num))
input("运行完毕，请按回车键退出...")
