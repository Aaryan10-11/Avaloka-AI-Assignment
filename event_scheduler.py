
def can_attend_all(events):
    if not events:
        return True

    ordered = sorted(events, key=lambda event: event[0])

    for i in range(1, len(ordered)):
        if ordered[i][0] < ordered[i - 1][1]:
            return False

    return True


def min_rooms_required(events):
    if not events:
        return 0

    starts = sorted(start for start, end in events)
    ends = sorted(end for start, end in events)

    rooms_in_use = 0
    max_rooms = 0
    end_index = 0

    for start in starts:
        while end_index < len(ends) and ends[end_index] <= start:
            rooms_in_use -= 1
            end_index += 1

        rooms_in_use += 1
        max_rooms = max(max_rooms, rooms_in_use)

    return max_rooms
