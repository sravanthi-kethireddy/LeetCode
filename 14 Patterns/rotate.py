input_matrix = [
  [1,2,3],
  [4,5,6],
  [7,8,9]
]

def rotate_matrix(matrix):
    matrix =matrix[::-1]
    for i in range(len(matrix)):
        for j in range(i):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    return matrix

# print(rotate_matrix(input_matrix)) 

def rotate(nums, k):
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        a = [0]*n
        for i in range(n):
              print(i+k, (i+k)%n)
              a[(i+k)%n] = nums[i]
        nums[:] = a
        print(nums)
          
rotate([1,2,3,4,5,6,7], 3)