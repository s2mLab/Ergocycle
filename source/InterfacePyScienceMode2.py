from pyScienceMode2 import Channel as Ch
import numpy as np


def matrix_to_list_channels(stimulation_matrix):
    list_channels = []
    for i in range(np.shape(stimulation_matrix)[1]):
        channel = Ch.Channel(
            mode="Single",
            no_channel=i + 1,
            amplitude=stimulation_matrix[0][i],
            pulse_width=stimulation_matrix[2][i],
            name=stimulation_matrix[3][i],
        )
        list_channels.append(channel)
    return list_channels
