Console.Clear();

Console.Write("Введите число (количество элементов массива): ");
int size = Convert.ToInt32(Console.ReadLine());

double[] numbers = new double[size];
double sum = 0;
Random rand = new Random();

for(int index = 0; index < size; index++) {
    numbers[index] = rand.Next();

    if((index + 1) % 2 != 0) { sum += numbers[index]; }
}

Console.WriteLine($"[{String.Join(", ", numbers)}] -> {sum}");
