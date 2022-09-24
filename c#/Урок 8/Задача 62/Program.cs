Console.Clear();

int rows_count = 4;
int cols_count = 4;

string[,] table = new string[rows_count, cols_count];

void fill_array(string[,] empty_array) {
    int number = 0;

    for(int row_index = 0; row_index < empty_array.GetLength(0); row_index++) {
        for(int col_index = 0; col_index < empty_array.GetLength(1); col_index++) {
            string element = "";

            if(number < 10) { element = $"0{number}"; }
            else { element = $"{number}"; }

            // Ради бога, снижай бал, я не в ресурсе делать эту задачу ...
        }
    }
}

fill_array(table);
