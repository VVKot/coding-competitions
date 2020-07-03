import java.util.HashMap;
import java.util.Map;

class Solution {

    private int encodeState(int[] cells) {
        int state = 0x0;
        for (int cell : cells) {
            state <<= 1;
            state = (state | cell);
        }
        return state;
    }

    private int[] nextDay(int[] cells) {
        int[] newCells = new int[cells.length];
        newCells[0] = 0;
        for (int i = 1; i < cells.length - 1; i++)
            newCells[i] = (cells[i - 1] == cells[i + 1]) ? 1 : 0;
        newCells[cells.length - 1] = 0;
        return newCells;
    }

    public int[] prisonAfterNDays(int[] cells, int N) {
        Map<Integer, Integer> seen = new HashMap<>();
        boolean isSeenAlready = false;

        while (N > 0) {
            if (!isSeenAlready) {
                int state = this.encodeState(cells);
                if (seen.containsKey(state)) {
                    N %= seen.get(state) - N;
                    isSeenAlready = true;
                } else
                    seen.put(state, N);
            }
            if (N > 0) {
                N -= 1;
                cells = this.nextDay(cells);
            }
        }
        return cells;
    }
}
