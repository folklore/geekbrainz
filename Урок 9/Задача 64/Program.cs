Console.Clear();

Console.Write("Введите M: ");
int m = Convert.ToInt32(Console.ReadLine());
Console.Write("Введите N: ");
int n = Convert.ToInt32(Console.ReadLine());

Console.Write($"M = {m}; N = {n}. -> ");

void enumeration_printer(int start, int finish) {
    Console.Write($"{start} ");
    if(start < finish) { enumeration_printer(start + 1, finish); }
}

enumeration_printer(m, n);

Console.WriteLine("");
