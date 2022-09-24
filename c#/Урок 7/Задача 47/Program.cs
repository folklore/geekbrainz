Console.Clear();

int rows_count = 3;
int cols_count = 4;

double[,] table = new double[rows_count, cols_count];

void fill_array(double[,] empty_array) {
    Random rand = new Random();

    for(int row_index = 0; row_index < empty_array.GetLength(0); row_index++) {
        for(int col_index = 0; col_index < empty_array.GetLength(1); col_index++) {
            double number = Math.Round(rand.NextDouble() * rand.Next(-99, 100), 1);
            empty_array[row_index, col_index] = number;
        }
    }
}

fill_array(table);

void print_array(double[,] filled_array) {
    int max_number_length = 5;

    for(int row_index = 0; row_index < filled_array.GetLength(0); row_index++) {
        for(int col_index = 0; col_index < filled_array.GetLength(1); col_index++) {
            string element = Convert.ToString(filled_array[row_index, col_index]);
            string padded_element = element.PadLeft(max_number_length);

            Console.Write($"{padded_element} ");
        }
        Console.WriteLine("");
    }
}

print_array(table);

// -39.2  -1.8  21.9 -45.2 
//  -7.1  20.9 -42.3  -4.5 
// -45.9  70.4  26.5 -36.3
