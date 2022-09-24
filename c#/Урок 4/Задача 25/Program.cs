Console.Clear();

double multiplier(int a, int n) {
    return Math.Pow(a, n);
}

string answer = "yes";

while(answer == "yes" || answer == "y") {
    Console.Write("Введите основание степени: ");
    int base_number = Convert.ToInt32(Console.ReadLine());

    Console.Write("Введите показатель степени: ");
    int index_number = Convert.ToInt32(Console.ReadLine());

    double result = multiplier(base_number, index_number);
    Console.WriteLine($"Число A в натуральной степени B: {result}");

    Console.Write("Повторить [y]es/[n]o: ");
    answer = Console.ReadLine();
}
