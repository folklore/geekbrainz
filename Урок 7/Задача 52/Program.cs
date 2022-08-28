Console.Clear();

int[,] table = new int[,] {
    {1, 4, 7, 2},
    {5, 9, 2, 3},
    {8, 4, 2, 4}
};

void average_counter(int[,] filled_array) {
    int rows_count = filled_array.GetLength(0);

    for(int col_index = 0; col_index < filled_array.GetLength(1); col_index++) {
        double summa = 0;

        for(int row_index = 0; row_index < rows_count; row_index++) {
            summa += filled_array[row_index, col_index];
        }

        double average = summa / rows_count;
        Console.Write($"{average:f1} ");
    }
    Console.WriteLine();
}

average_counter(table); // => 4.7 5.7 3.7 3.0
