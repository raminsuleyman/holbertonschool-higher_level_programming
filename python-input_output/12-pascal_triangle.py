#!/usr/bin/python3
"""pascal triangle"""


def pascal_triangle(n):
    """Paskal üçbucağını n sayda sətir üçün qaytarır."""
    if n <= 0:
        return []
    # Üçbucağı ilk sətirlə başladırıq
    triangle = [[1]]
    # 1-ci sətir artıq var, ona görə 1-dən n-ə qədər dövr qururuq
    for i in range(1, n):
        # Hər sətir həmişə 1 ilə başlayır
        row = [1]
        # Bir əvvəlki sətri götürürük ki, cəmləmə edə bilək
        prev_row = triangle[i - 1]
        # Sətrin daxili rəqəmlərini hesablayırıq
        for j in range(1, i):
            # Sol yuxarıdakı və sağ yuxarıdakı rəqəmlərin cəmi
            row.append(prev_row[j - 1] + prev_row[j])
        # Hər sətir həmişə 1 ilə bitir
        row.append(1)
        # Hazır olan sətri üçbucağa əlavə edirik
        triangle.append(row)

    return triangle
