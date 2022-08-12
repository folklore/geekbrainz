// Отрицательные числа не рассматриваю.
// Игнорирую "правило": не работать с числами как со строками.

Console.Clear();

Console.Write("Введите трехзначное число: ");
int number = Convert.ToInt32(Console.ReadLine());

if(number < 100 || number > 999) {
    Console.WriteLine($"Введенное число {number} не трехзначное.");
}
else {
    Console.WriteLine($"Вторая цифра {number.ToString()[1]}.");
}
