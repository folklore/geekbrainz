Console.Clear();

double cubic_multiplier(int n) {
    return Math.Pow(n, 3);
}

Console.Write("Введите число: ");
int number = Convert.ToInt32(Console.ReadLine());

double[] cubics = new double[number];

for(int index = 0; index < number; index++) {
    cubics[index] = cubic_multiplier(index+1);
}

Console.WriteLine($"{number} => {String.Join(", ", cubics)}");
