#!/usr/bin/env
import numpy as np


def get_collage(frames, count):
    """

    :rtype: path of video to analyze
    """
    nf = int(count)

    print(nf)

    nf = (nf // 3) * 3

    print(nf)

    l1 = nf / 3
    l1 = int(l1)

    print(l1)
    l2 = (nf / 3) * 2
    l2 = int(l2)
    print(l2)
    l3 = nf

    print(l3)
    print(frames[0:l1])

    row1 = np.concatenate(frames[0:l1], axis=1)
    print(row1)
    print(frames[l1:l2])
    row2 = np.concatenate(frames[l1:l2], axis=1)
    print(row2)
    print(frames[l2:l3])
    row3 = np.concatenate(frames[l2:l3], axis=1)
    print(row3)

    collage = np.concatenate((row1, row2, row3), axis=0)
    return collage
