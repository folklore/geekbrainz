coord_angle = int(input('Укажите координатный угол (1-4): '))

if coord_angle == 1:
    print('x ∈ (0, ∞); y ∈ (0, ∞)')
elif coord_angle == 2:
    print('x ∈ (0, -∞); y ∈ (0, ∞)')
elif coord_angle == 3:
    print('x ∈ (0, -∞); y ∈ (0, -∞)')
elif coord_angle == 4:
    print('x ∈ (0, ∞); y ∈ (0, -∞)')
else:
    print('Такого координатного угла не существует')
