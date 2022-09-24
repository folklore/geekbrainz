Console.Clear();

double[] ArrayGenerator(int size) {
    double[] numbers = new double[size];
    Random rand = new Random();

    for(int index = 0; index < size; index++) {
        numbers[index] = rand.NextDouble() * rand.Next();
    }

    return numbers;
}

Console.Write("Введите число (количество элементов массива): ");
int size = Convert.ToInt32(Console.ReadLine());

double[] numbers = ArrayGenerator(size);

double min = int.MaxValue;
double max = int.MinValue;

foreach(double number in numbers) {
    if(number < min) { min = number; }
    if(number > max) { max = number; }
}

double sum = min + max;

Console.WriteLine($"[{String.Join(", ", numbers)}]: {min} + {max} = {sum}");
