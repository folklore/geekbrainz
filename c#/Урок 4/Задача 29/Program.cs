// Сделал без пользовательского ввода.

Console.Clear();

const int size = 8;

double[] numbers = new double[size];

Random rand = new Random();

for(int index = 0; index < size; index++) {
    numbers[index] = rand.Next(0, int.MaxValue);
}

Console.WriteLine($"[{String.Join(", ", numbers)}]");
