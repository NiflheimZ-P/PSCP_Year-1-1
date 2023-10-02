"""[Midterm 2023] Home Run"""
def homerun():
    """[Midterm 2023] Home Run"""
    shot = int(input())
    distance = float(input())
    count = 0
    for _ in range(shot):
        distance_field = float(input())
        if distance > distance_field:
            count += 1
    print(count)
homerun()
