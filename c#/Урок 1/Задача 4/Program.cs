Console.Clear();

Console.Write("Введите первое число: ");
int number1 = Convert.ToInt32(Console.ReadLine());

Console.Write("Введите второе число: ");
int number2 = Convert.ToInt32(Console.ReadLine());

Console.Write("Введите третье число: ");
int number3 = Convert.ToInt32(Console.ReadLine());

int maximum = number1;

if (number2 > maximum) { maximum = number2; }
if (number3 > maximum) { maximum = number3; }

Console.Write("Наибольшее число: ");
Console.WriteLine(maximum);
