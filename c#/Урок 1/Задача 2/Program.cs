Console.Clear();

Console.Write("Введите первое число: ");
int number1 = Convert.ToInt32(Console.ReadLine());

Console.Write("Введите второе число: ");
int number2 = Convert.ToInt32(Console.ReadLine());

Console.Write("Наибольшее число ");
if (number1 > number2) { Console.WriteLine($"первое ({number1})"); }
else { Console.WriteLine($"второе ({number2})"); }
