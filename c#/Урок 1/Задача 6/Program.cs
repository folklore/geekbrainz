Console.Clear();

Console.Write("Введите число: ");
int number = Convert.ToInt32(Console.ReadLine());

int remainder = number % 2;

Console.Write($"Число {number} ");
if (remainder == 0) { Console.WriteLine("четное"); }
else { Console.WriteLine("нечетное"); }
