// Отрицательные числа не рассматриваю.
// Игнорирую "правило": не работать с числами как со строками.

Console.Clear();

Console.Write("Введите число: ");
int number = Convert.ToInt32(Console.ReadLine());

if(number < 100) {
    Console.WriteLine($"Во введенном числе {number} третьей цифры нет.");
}
else {
    Console.WriteLine($"Третья цифра {number.ToString()[2]}.");
}
