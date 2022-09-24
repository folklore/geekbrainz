Console.Clear();

int rows_count = 4;
int cols_count = 5;

int[,] table = new int[rows_count, cols_count];

void fill_array(int[,] empty_array) {
    Random rand = new Random();

    for(int row_index = 0; row_index < empty_array.GetLength(0); row_index++) {
        for(int col_index = 0; col_index < empty_array.GetLength(1); col_index++) {
            int number = rand.Next(1, 100);
            empty_array[row_index, col_index] = number;
        }
    }
}

void print_array(int[,] filled_array) {
    int max_number_length = 2;

    for(int row_index = 0; row_index < filled_array.GetLength(0); row_index++) {
        for(int col_index = 0; col_index < filled_array.GetLength(1); col_index++) {
            string element = Convert.ToString(filled_array[row_index, col_index]);
            string padded_element = element.PadLeft(max_number_length);

            Console.Write($"{padded_element} ");
        }
        Console.WriteLine("");
    }
    Console.WriteLine("");
}

void sort_rows_array(int[,] filled_array) {
    for(int row_index = 0; row_index < filled_array.GetLength(0); row_index++) {
        for(int col_index = 0; col_index < filled_array.GetLength(1); col_index++) {
            for(int yet_another_col_index = 0; yet_another_col_index < filled_array.GetLength(1) - 1; yet_another_col_index++) {
                if(filled_array[row_index, yet_another_col_index] < filled_array[row_index, yet_another_col_index + 1]) {
                    int temp = filled_array[row_index, yet_another_col_index];

                    filled_array[row_index, yet_another_col_index] = filled_array[row_index, yet_another_col_index + 1];
                    filled_array[row_index, yet_another_col_index + 1] = temp;
                }
            }
        }

    }
}

fill_array(table);

print_array(table);

// 25 11 38  5 40 
// 18  5 68  6 33 
// 12 97 98 14 92 
// 80 44  8 27 74

sort_rows_array(table);

print_array(table);

// 40 38 25 11  5 
// 68 33 18  6  5 
// 98 97 92 14 12 
// 80 74 44 27  8
