Console.Clear();

Console.Write("Введите M: ");
int m = Convert.ToInt32(Console.ReadLine());
Console.Write("Введите N: ");
int n = Convert.ToInt32(Console.ReadLine());

Console.Write($"M = {m}; N = {n}. -> ");

// https://ru.wikipedia.org/wiki/%D0%A4%D1%83%D0%BD%D0%BA%D1%86%D0%B8%D1%8F_%D0%90%D0%BA%D0%BA%D0%B5%D1%80%D0%BC%D0%B0%D0%BD%D0%B0

int ackermann_func(int m, int n) {
    if(m == 0) {
        return n + 1;
    }
    else if(m == 0 && n == 0) {
        return 1;
    }
    else if(m > 0 && n == 0) {
        return ackermann_func(m - 1, 1);
    }
    else {
        return ackermann_func(m - 1, ackermann_func(m, n - 1));
    }
}

Console.Write($"{ackermann_func(m, n)}");

Console.WriteLine("");
