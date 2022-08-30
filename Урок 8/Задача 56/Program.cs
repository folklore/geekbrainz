Console.Clear();

int rows_count = 3;
int cols_count = 4;

int[,] table = new int[rows_count, cols_count];

void fill_array(int[,] empty_array) {
    Random rand = new Random();

    for(int row_index = 0; row_index < empty_array.GetLength(0); row_index++) {
        for(int col_index = 0; col_index < empty_array.GetLength(1); col_index++) {
            int number = rand.Next(1, 10);
            empty_array[row_index, col_index] = number;
        }
    }
}

void print_array(int[,] filled_array) {
    for(int row_index = 0; row_index < filled_array.GetLength(0); row_index++) {
        for(int col_index = 0; col_index < filled_array.GetLength(1); col_index++) {
            Console.Write($"{filled_array[row_index, col_index]} ");
        }
        Console.WriteLine("");
    }
    Console.WriteLine("");
}

void find_row_with_min_sum(int[,] filled_array) {
    int[] temp = new int[filled_array.GetLength(0)];

    for(int row_index = 0; row_index < filled_array.GetLength(0); row_index++) {
        int sum = 0;
        
        for(int col_index = 0; col_index < filled_array.GetLength(1); col_index++) {
            sum += filled_array[row_index, col_index];
        }

        temp[row_index] = sum;
    }

    int index_min_sum_row = 0;
    int min_sum = int.MaxValue;

    for(int index = 0; index < temp.Length; index++) {
        if(temp[index] < min_sum) {
            index_min_sum_row = index;
            min_sum = temp[index];
        }
    }

    // Вывожу номера строк не с нуля ...
    Console.WriteLine($"{index_min_sum_row + 1} строка");
}

fill_array(table);

print_array(table);

// 1 8 9 5 
// 8 3 3 6 
// 5 9 5 7 

find_row_with_min_sum(table);

// 2 строка
