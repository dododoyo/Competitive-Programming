class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        # create a set of all possible cell positions in the grid.
        cells_set = set((r, c) for r in range(m) for c in range(n))

        # create a set of all possible cell position of the guards.
        guards_set = set((row, column) for row, column in guards)

        # create a set of all possible cell position of the walls
        walls_set = set((row, column) for row, column in walls)

        # create the walls and guards from the grid
        cells_set -= guards_set
        cells_set -= walls_set

        # seen_cells keeps track of the cells that are seen by the guards.
        guard_cells = set()


        for guard_r, guard_c in guards_set:
            # moving to right
            row, column = guard_r, guard_c + 1
            while (row, column) in cells_set:
                guard_cells.add((row, column))
                column += 1

            # moving to left
            row, column = guard_r, guard_c - 1
            while (row, column) in cells_set:
                guard_cells.add((row, column))
                column -= 1

            # moving down
            row, column = guard_r + 1, guard_c
            while (row, column) in cells_set:
                guard_cells.add((row, column))
                row += 1

            # moving up
            row, column = guard_r - 1, guard_c
            while (row, column) in cells_set:
                guard_cells.add((row, column))
                row -= 1

        return len(cells_set - guard_cells)

