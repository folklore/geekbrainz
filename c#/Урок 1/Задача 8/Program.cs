Console.Clear();

Console.Write("Введите число: ");
int number = Convert.ToInt32(Console.ReadLine());

int current = 2;

while (current <= number)
{
    Console.WriteLine(current);
    current += 2;
}
