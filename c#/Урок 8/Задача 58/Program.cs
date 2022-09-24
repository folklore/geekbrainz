Console.Clear();

int rows_count = 2;
int cols_count = 2;

int[,] matrix_1 = new int[rows_count, cols_count];
int[,] matrix_2 = new int[rows_count, cols_count];

void fill_array(int[,] empty_array) {
    Random rand = new Random();

    for(int row_index = 0; row_index < empty_array.GetLength(0); row_index++) {
        for(int col_index = 0; col_index < empty_array.GetLength(1); col_index++) {
            int number = rand.Next(1, 10);
            empty_array[row_index, col_index] = number;
        }
    }
}

fill_array(matrix_1);
fill_array(matrix_2);

void print_array(int[,] filled_array) {
    for(int row_index = 0; row_index < filled_array.GetLength(0); row_index++) {
        for(int col_index = 0; col_index < filled_array.GetLength(1); col_index++) {
            Console.Write($"{filled_array[row_index, col_index]} ");
        }
        Console.WriteLine("");
    }
    Console.WriteLine("");
}

print_array(matrix_1);

// 6 2 
// 6 3 

print_array(matrix_2);

// 7 2 
// 4 9 

void multiplicator(int[,] array_1, int[,] array_2) {
    int[,] result = new int[rows_count, cols_count];

    // https://www.pvsm.ru/matematika/362855

    for (int i = 0; i < rows_count; i++) {
        for (int j = 0; j < cols_count; j++) {
            result[i, j] = 0;

            for (int k = 0; k < rows_count; k++) {
                result[i, j] += array_1[i, k] * array_2[k, j];
            }
        }
    }

    print_array(result);
}

multiplicator(matrix_1, matrix_2);

// 50 30 
// 54 39
