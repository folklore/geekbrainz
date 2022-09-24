Console.Clear();

string answer = "yes";
double[] numbers = new double[] {};
int greater_than_0_count = 0;
int index = 0;

while(answer == "yes" || answer == "y") {
    Console.Write("Введите число: ");
    double number = Convert.ToDouble(Console.ReadLine());

    if(number > 0) { greater_than_0_count++; };

    Array.Resize(ref numbers, index + 1);
    numbers[index] = number;

    Console.Write("Продолжить ввод? [y]es/[n]o: ");
    answer = Console.ReadLine();

    index++;
}

Console.WriteLine($"[{String.Join(", ", numbers)}] -> {greater_than_0_count}");
