Console.Clear();

int rows_count = 3;
int cols_count = 4;

int[,] table = new int[rows_count, cols_count];

void fill_array(int[,] empty_array) {
    Random rand = new Random();

    for(int row_index = 0; row_index < empty_array.GetLength(0); row_index++) {
        for(int col_index = 0; col_index < empty_array.GetLength(1); col_index++) {
            empty_array[row_index, col_index] = rand.Next(1, 10);
        }
    }
}

fill_array(table);

void find_element_in_array(int[,] filled_array, int row_number, int col_number) {
    Console.Write($"Массив[{row_number}, {col_number}] => ");

    if(row_number < filled_array.GetLength(0) && col_number < filled_array.GetLength(1)) {
        Console.WriteLine(filled_array[row_number, col_number]);
    }
    else {
        Console.WriteLine("Элемент c такой позицией отсутствует!");
    }
}

Console.Write($"Введите номер строки в массиве (c нуля до {rows_count - 1}): ");
int row_number = Convert.ToInt32(Console.ReadLine());

Console.Write($"Введите номер столбца в массиве (c нуля до {cols_count - 1}): ");
int col_number = Convert.ToInt32(Console.ReadLine());

find_element_in_array(table, row_number, col_number);
