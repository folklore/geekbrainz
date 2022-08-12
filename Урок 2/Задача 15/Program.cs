Console.Clear();

Console.Write("Введите цифру обозначающую день недели [1..7]: ");
int number = Convert.ToInt32(Console.ReadLine());

switch (number) {
    case 1:
    case 2:
    case 3:
    case 4:
    case 5:
        Console.WriteLine($"Введенная цифра {number} обозначает рабочий день.");
        break;
    case 6:
    case 7:
        Console.WriteLine($"Введенная цифра {number} обозначает выходной день.");
        break;
    default:
        Console.WriteLine($"Введенная цифра {number} не обозначает день недели.");
        break;
}
