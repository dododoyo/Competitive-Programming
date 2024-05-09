def king_path(r, c, rows, cols):
  moves = []
  for dx, dy in [[1, 1], [1, -1], [-1, 1], [-1, -1], [1, 0], [0, 1], [-1, 0], [0, -1]]:
    x, y = dx+r, dy+c

    if 0 <= x < rows and 0 <= y < cols:
      moves.append((x, y))
  return moves

