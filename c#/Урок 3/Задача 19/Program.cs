Console.Clear();

Console.Write("Введите пятизначное число: ");
int number = Convert.ToInt32(Console.ReadLine());

if(number < 10000 || number > 99999) {
    Console.WriteLine($"Введенное число {number} не пятизначное.");
}
else {
    int duplicate_number = number;
    int reverse = 0;

    while(number > 0) {
        int remainder = number % 10;
        reverse = (reverse * 10) + remainder;
        number = number / 10;
    }

    if(duplicate_number == reverse) {
        Console.WriteLine($"Введенное число {duplicate_number} палиндромом.");
    }
    else {
        Console.WriteLine($"Введенное число {duplicate_number} не палиндромом.");
    }
}
