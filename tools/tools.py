import json


class Tools:
    """
    A class to analyze and manipulate frame data.
    ## functions

    - len: Returns the length of a list.
    - max: Returns the maximum value in a list.
    - find_missing_frames: Finds missing frames in the frame list.
    - find_frame_gaps: Finds gaps between frames.
    - find_longest_frame_gap: Finds the longest gap between frames.
    - missing_count: Returns the count of missing frames.
    - get_result: Returns a JSON-serialized result of the analysis.
    """

    def __init__(self, frame_list: list[int]):
        self.frame_list = frame_list

    def len(self, number_list: list[int] | None = None) -> int:
        count = 0
        number_list = number_list or self.frame_list
        if type(number_list) is list:
            for i in number_list:
                count += 1
            return count
        return 0

    def max(self, number_list: list[int] | None = None) -> int:
        number_list = number_list or self.frame_list
        if not number_list or self.len(number_list) == 0:
            print("Empty list or None")
            return 0
        max_value = number_list[0]
        for i in number_list:
            if i > max_value:
                max_value = i
        return max_value

    def find_missing_frames(self) -> list[int]:      
        missing_frames = []
        for i in range(1, self.max(self.frame_list) + 1):
            if i not in self.frame_list:
                missing_frames.append(i)
        return missing_frames

    def find_frame_gaps(self) -> list[list[int]]:
        frame_gaps = []
        for i in range(len(self.frame_list) - 1):
            start = self.frame_list[i]
            end = self.frame_list[i + 1]
            if end - start > 1:
                frame_gaps.append([start + 1, end - 1])
        return frame_gaps

    def find_longest_frame_gap(self) -> list[int]:
        gaps = self.find_frame_gaps()
        if not gaps:
            return []
        biggest_gap = gaps[0]
        biggest_gap_number = 0
        for i in gaps:
            if i[1] - i[0] > biggest_gap_number:
                biggest_gap_number = i[1] - i[0]
                biggest_gap = i
        return biggest_gap

    def missing_count(self) -> int:
        return self.len(self.find_missing_frames())

    def get_result(self) -> dict:
        result = {
            "gaps": self.find_frame_gaps(),
            "longest_gap": self.find_longest_frame_gap(),
            "missing_count": self.missing_count(),
        }
        return json.dumps(result)
