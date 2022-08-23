Console.Clear();

Console.WriteLine("Уравнения прямых: y = k1 * x + b1; y = k2 * x + b2;");
Console.WriteLine();

Console.Write("Введите k1 для первого уравнения: ");
double k1 = Convert.ToDouble(Console.ReadLine());
Console.Write("Введите b1 для первого уравнения: ");
double b1 = Convert.ToDouble(Console.ReadLine());

Console.Write("Введите k2 для второго уравнения: ");
double k2 = Convert.ToDouble(Console.ReadLine());
Console.Write("Введите b2 для второго уравнения: ");
double b2 = Convert.ToDouble(Console.ReadLine());

double x = (b2 - b1) / (k1 - k2);
double y = k2 * x + b2;

Console.WriteLine();
Console.WriteLine($"y = {k1} * x + {b1}; y = {k2} * x + {b2}");
Console.WriteLine($"Точка пересечения двух прямых ({x}; {y})");
