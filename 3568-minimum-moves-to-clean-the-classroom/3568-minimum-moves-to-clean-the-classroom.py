class Solution:
    def minMoves(self, classroom: List[str], energy: int) -> int:
        rows, cols = len(classroom), len(classroom[0])
        litter_positions = []
        start_pos = (0,0)

        for r in range(rows):
            for c in range(cols):
                if classroom[r][c] == 'S':
                    start_pos = (r, c)
                elif classroom[r][c] == 'L':
                    litter_positions.append((r, c))

        target_mask = (1 << len(litter_positions)) - 1
        if target_mask == 0:
            return 0

        q = deque([(0, start_pos[0], start_pos[1], 0, energy)])

        visited = {(start_pos[0], start_pos[1], 0): energy}

        while q:
            moves, r ,c, mask, curr_energy = q.popleft()
            if curr_energy == 0:
                continue

            for dr, dc in [(-1,0),(1,0),(0,-1),(0,1)]:
                nr, nc = r + dr, c + dc

                if 0 <= nr < rows and 0 <= nc < cols and classroom[nr][nc] != 'X':
                    next_energy = curr_energy - 1
                    next_mask = mask

                    if classroom[nr][nc] == 'R':
                        next_energy = energy
                    if classroom[nr][nc] == 'L':
                        next_mask |= (1 << litter_positions.index((nr, nc)))
                    if next_mask == target_mask: 
                        return moves + 1

                    state = (nr, nc, next_mask)
                    if state not in visited or visited[state] < next_energy:
                        visited[state] = next_energy
                        q.append((moves + 1, nr, nc, next_mask, next_energy))
        return -1
