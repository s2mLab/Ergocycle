# Unfinished class


class Screen:
    def __init__(self, event_function):
        self.event_function = event_function
        self.window_counter = 0

    def next_window(self):
        self.window_counter += 1
        # print(self.window_counter)

    def next_window_special(self):
        self.window_counter += 4
        # print(self.window_counter)

    def get_amplitude(self):
        return self.amplitude_edit.text()
