public class ScalarMultiplication {
    public static void main(String[] args) {
        int[][] matrix = {{1, 2, 3}, {4, 5, 6}, {7, 8, 9}};
        int scalar = 2;

        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {
                matrix[i][j] *= scalar;
                System.out.print(matrix[i][j] + " ");
            }
            System.out.println();
        }
    }
}

