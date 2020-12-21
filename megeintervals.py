def mergeInterval(array):
    if len(interval) <= 1:
        return interval
    interval.sort(key=lambda x: x[0])
    # print(interval)
    i = 1
    if interval[i][0] <= interval[i-1][1]:
        interval[i-1][0] = min(interval[i-1][0], interval[i][0])
        interval[i-1][1] = max(interval[i-1][1], interval[i][1])
        interval.pop(i)
    else:
        i += 1
    return interval


if __name__ == "__main__":
    interval = [[1, 3], [8, 10], [2, 6]]
    print(mergeInterval(interval))
