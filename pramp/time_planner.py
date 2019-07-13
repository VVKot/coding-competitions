def meeting_planner(slotsA, slotsB, dur):
    a_idx = b_idx = 0
    while a_idx < len(slotsA) and b_idx < len(slotsB):
        a_start, a_end = slotsA[a_idx]
        b_start, b_end = slotsB[b_idx]
        start = max(a_start, b_start)
        end = min(a_end, b_end)
        possible_end = start + dur
        if possible_end <= end:
            return [start, possible_end]
        if a_end < b_end:
            a_idx += 1
        else:
            b_idx += 1
    return []
