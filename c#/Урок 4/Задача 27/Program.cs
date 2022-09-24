Console.Clear();

Console.Write("Введите число: ");
int number = Convert.ToInt32(Console.ReadLine());

int summa = 0;

while(number > 0) {
    int remainder = number % 10;

    number = number / 10;
    summa = summa + remainder;
}

Console.WriteLine($"Сумма цифр в числе равна {summa}.");
