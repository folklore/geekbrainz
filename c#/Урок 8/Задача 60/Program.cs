Console.Clear();

int rows_count = 2;
int cols_count = 2;
int deep_count = 2;

int[, ,] cube = new int[rows_count, cols_count, deep_count];

void fill_cube(int[, ,] empty_cube) {
    Random rand = new Random();
    int index = 0;

    for(int row_index = 0; row_index < empty_cube.GetLength(0); row_index++) {
        for(int col_index = 0; col_index < empty_cube.GetLength(1); col_index++) {
            for(int dep_index = 0; dep_index < empty_cube.GetLength(2); dep_index++) {
                                                               // ¯\_(ツ)_/¯ unique ))
                empty_cube[row_index, col_index, dep_index] = 10 * rand.Next(1, 10) + index;
                index++;
            }
        }
    }
}

void print_cube(int[, ,] filled_cube) {
    for(int row_index = 0; row_index < filled_cube.GetLength(0); row_index++) {
        for(int col_index = 0; col_index < filled_cube.GetLength(1); col_index++) {
            for(int dep_index = 0; dep_index < filled_cube.GetLength(2); dep_index++) {
                int element = filled_cube[row_index, col_index, dep_index];

                Console.WriteLine($"{element} ({row_index}, {col_index}, {dep_index})");
            }
        }
    }
    Console.WriteLine("");
}

fill_cube(cube);

print_cube(cube);

// 60 (0, 0, 0)
// 91 (0, 0, 1)
// 62 (0, 1, 0)
// 83 (0, 1, 1)
// 64 (1, 0, 0)
// 65 (1, 0, 1)
// 36 (1, 1, 0)
// 97 (1, 1, 1)
