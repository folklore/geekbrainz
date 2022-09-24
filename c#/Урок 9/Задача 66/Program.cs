Console.Clear();

Console.Write("Введите M: ");
int m = Convert.ToInt32(Console.ReadLine());
Console.Write("Введите N: ");
int n = Convert.ToInt32(Console.ReadLine());

Console.Write($"M = {m}; N = {n}. -> ");

int enumeration_calculator(int start, int finish) {
    if(start >= finish) { return finish; }
    return start + enumeration_calculator(start + 1, finish);
}

Console.Write($"{enumeration_calculator(m, n)}");

Console.WriteLine("");
