Console.Clear();

double distance(int a, int b, int c, int o, int p, int k) {
    return Math.Sqrt(Math.Pow(o - a, 2) + Math.Pow(p - b, 2) + Math.Pow(k - c, 2));
}

Console.Write("Введите X первой точки: ");
int x1 = Convert.ToInt32(Console.ReadLine());
Console.Write("Введите Y первой точки: ");
int y1 = Convert.ToInt32(Console.ReadLine());
Console.Write("Введите Z первой точки: ");
int z1 = Convert.ToInt32(Console.ReadLine());

Console.Write("Введите X второй точки: ");
int x2 = Convert.ToInt32(Console.ReadLine());
Console.Write("Введите Y второй точки: ");
int y2 = Convert.ToInt32(Console.ReadLine());
Console.Write("Введите Z второй точки: ");
int z2 = Convert.ToInt32(Console.ReadLine());

double result = distance(x1, y1, z1, x2, y2, z2);
Console.WriteLine($"Расстояние между точками в 3D пространстве равно {result:f2}");
