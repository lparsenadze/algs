from sys import stdin
from collections import namedtuple

Segment = namedtuple('Segment', 'start end')

def optimal_points(segments):
    points = []
    segments = sorted(segments, key=lambda x: x.end)
    curr_end = None
    for s in segments:
        if curr_end is None or s.start > curr_end:
            curr_end = s.end
            points.append(curr_end)
    return points


if __name__ == '__main__':
    input = stdin.read()
    n, *data = map(int, input.split())
    segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    points = optimal_points(segments)
    print(len(points))
    print(*points)
