class IRange:

    def __init__(self, start, end):
        self.value = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.value >= self.end:
            raise StopIteration
        current = self.value
        self.value += 1
        return current


def i_range(start):
    current = start
    while True:
        yield current
        current += 1


nums = i_range(5)

for num in nums:
    print(num)
