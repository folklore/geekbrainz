Console.Clear();

double[] ArrayGenerator(int size) {
    double[] numbers = new double[size];
    Random rand = new Random();

    for(int index = 0; index < size; index++) {
        numbers[index] = rand.Next(100, 999);
    }

    return numbers;
}

const int size = 5;

double[] numbers = ArrayGenerator(size);

int EvensCounter(double[] numbers) {
    int evens_count = 0;

    foreach(double number in numbers) {
        if(number % 2 == 0) { evens_count++; }
    }

    return evens_count;
}

int evens_count = EvensCounter(numbers);

Console.WriteLine($"[{String.Join(", ", numbers)}] -> {evens_count}");
