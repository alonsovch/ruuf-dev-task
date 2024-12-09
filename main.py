def fit_rectangles(x, y, a, b):
    if x<=0 or y<=0 or a<=0 or b<=0:
        return 0
    if x<a or y<b:
        return 0
    
    cols = y//b
    rows = x//a
    total_straight_rectangles = cols*rows

    flipped_cols = y//a
    flipped_rows = x//b
    total_flipped_rectangles = flipped_cols*flipped_rows

    if total_straight_rectangles > total_flipped_rectangles:
        leftover_rectangle_width = rows*a
        leftover_rectangle_height = y - cols*b
        return total_straight_rectangles + fit_rectangles(leftover_rectangle_width, leftover_rectangle_height, a, b)
    else:
        leftover_rectangle_width = x - flipped_rows*b
        leftover_rectangle_height = flipped_cols*a
        return total_flipped_rectangles + fit_rectangles(leftover_rectangle_width, leftover_rectangle_height, a, b) 

print(fit_rectangles(4, 2, 1, 2))
print(fit_rectangles(5, 3, 1, 2))
print(fit_rectangles(10, 1, 2, 2))





