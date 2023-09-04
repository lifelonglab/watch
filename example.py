import numpy as np

from watch import WATCH

if __name__ == '__main__':
    dummy_data = np.array([[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6],
                           [1000, 1000], [5000, 5000], [10000, 10000],  [1000, 1000], [5000, 5000], [10000, 10000],
                           [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1]])

    watch = WATCH()
    locations = watch.detect(dummy_data)

    print(locations)
