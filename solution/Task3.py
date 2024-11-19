def remove_repeats(intervals: list[int]) -> list[int]:
    result = [[intervals[0], intervals[1]]]
    for i in range(2, len(intervals) - 1, 2):
        start, end = intervals[i], intervals[i + 1]
        if start <= result[-1][1] < end:
            result[-1] = [result[-1][0], end]
        elif result[-1][0] <= start and end <= result[-1][-1]:
            continue
        else:
            result.append([start, end])
    intervals = []
    for i in result:
        intervals.extend(i)
    return intervals


def appearance(intervals: dict[str, list[int]]) -> int:
    lesson_start, lesson_end = intervals['lesson']
    if len(intervals['pupil']) == 0 or len(intervals['tutor']) == 0:
        return 0
    pupil_intervals = remove_repeats(intervals['pupil'])
    tutor_intervals = remove_repeats(intervals['tutor'])

    pupil_times = [(pupil_intervals[i], pupil_intervals[i + 1]) for i in range(0, len(pupil_intervals), 2)]
    tutor_times = [(tutor_intervals[i], tutor_intervals[i + 1]) for i in range(0, len(tutor_intervals), 2)]

    ans = 0
    i = 0
    j = 0

    while i < len(pupil_times) and j < len(tutor_times):
        pupil_start, pupil_end = pupil_times[i]
        tutor_start, tutor_end = tutor_times[j]

        pupil_start = max(pupil_start, lesson_start)
        pupil_end = min(pupil_end, lesson_end)
        tutor_start = max(tutor_start, lesson_start)
        tutor_end = min(tutor_end, lesson_end)

        print(pupil_start, pupil_end, tutor_start, tutor_end)
        if pupil_end > tutor_start and tutor_end > pupil_start:
            mina = max(pupil_start, tutor_start)
            maxa = min(pupil_end, tutor_end)

            ans += maxa - mina

        if pupil_end < tutor_end:
            i += 1
        else:
            j += 1

    return ans


tests = [
    {
        'intervals': {
            'lesson': [1594663200, 1594666800],
            'pupil': [1594663340, 1594663389, 1594663390, 1594663395, 1594663396, 1594666472],
            'tutor': [1594663290, 1594663430, 1594663443, 1594666473]
        },
        'answer': 3117
    },
    {
        'intervals': {
            'lesson': [1594702800, 1594706400],
            'pupil': [1594702789, 1594704500, 1594702807, 1594704542, 1594704512, 1594704513, 1594704564, 1594705150,
                      1594704581, 1594704582, 1594704734, 1594705009, 1594705095, 1594705096, 1594705106, 1594706480,
                      1594705158, 1594705773, 1594705849, 1594706480, 1594706500, 1594706875, 1594706502, 1594706503,
                      1594706524, 1594706524, 1594706579, 1594706641],
            'tutor': [1594700035, 1594700364, 1594702749, 1594705148, 1594705149, 1594706463]
        },
        'answer': 3577
    },
    {
        'intervals': {
            'lesson': [1594692000, 1594695600],
            'pupil': [1594692033, 1594696347],
            'tutor': [1594692017, 1594692066, 1594692068, 1594696341]
        },
        'answer': 3565
    },
    {
        'intervals': {
            'lesson': [1594692000, 1594695600],
            'pupil': [1594692000, 1594695600],
            'tutor': [1594692000, 1594695600]
        },
        'answer': 3600
    },
    {
        'intervals': {
            'lesson': [1594692000, 1594695600],
            'pupil': [1594692000, 1594694000],
            'tutor': [1594694000, 1594695600]
        },
        'answer': 0
    },
    {
        'intervals': {
            'lesson': [1594692000, 1594695600],
            'pupil': [1594691000, 1594692005, 1594692020, 1594693000],
            'tutor': [1594692005, 1594692999]
        },
        'answer': 979
    },
    {
        'intervals': {
            'lesson': [1594692000, 1594695600],
            'pupil': [],
            'tutor': [1594692000, 1594695600]
        },
        'answer': 0
    },
    {
        'intervals': {
            'lesson': [1594692000, 1594695600],
            'pupil': [1594692500, 1594693000],
            'tutor': []
        },
        'answer': 0
    },
    {
        'intervals': {
            'lesson': [1594692000, 1594695600],
            'pupil': [1594692500, 1594693000, 1594693100, 1594694000],
            'tutor': [1594692000, 1594692500, 1594695500, 1594695600]
        },
        'answer': 0
    },
    {
        'intervals': {
            'lesson': [1594692000, 1594695600],
            'pupil': [1594692000, 1594692500, 1594692600, 1594695000],
            'tutor': [1594692500, 1594694000, 1594694100, 1594695500]
        },
        'answer': 2300
    }
]

if __name__ == '__main__':
    for i, test in enumerate(tests):
        test_answer = appearance(test['intervals'])
        assert test_answer == test['answer'], f'Error on test case {i}, got {test_answer}, expected {test["answer"]}'
