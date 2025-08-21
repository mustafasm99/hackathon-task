````
# Tools Class

A Python utility class to analyze and manipulate **frame data** (lists of integers representing frame numbers).  
This class provides methods for detecting missing frames, identifying gaps, and summarizing frame data.

---

## Features

- **`len`** → Returns the length of a list.  
- **`max`** → Returns the maximum value in a list.  
- **`find_missing_frames`** → Finds missing frames in the frame list.  
- **`find_frame_gaps`** → Finds gaps between consecutive frames.  
- **`find_longest_frame_gap`** → Finds the longest gap between frames.  
- **`missing_count`** → Returns the count of missing frames.  
- **`get_result`** → Returns a JSON string summarizing the analysis.  

---

## Installation

Clone or copy the `Tools` class into your project.  
No external dependencies are required (uses only the Python standard library).

---

## Usage

```python
from tools import Tools   # if saved as tools.py

frames = [1, 2, 3, 7, 8, 12]
tools = Tools(frames)

print("Length:", tools.len())  
print("Max:", tools.max())  
print("Missing Frames:", tools.find_missing_frames())  
print("Frame Gaps:", tools.find_frame_gaps())  
print("Longest Gap:", tools.find_longest_frame_gap())  
print("Missing Count:", tools.missing_count())  
print("Result JSON:", tools.get_result())
````

---

## Example Output

For the input:

```python
frames = [1, 2, 3, 7, 8, 12]
```

The output will be:

```
Length: 6
Max: 12
Missing Frames: [4, 5, 6, 9, 10, 11]
Frame Gaps: [[4, 6], [9, 11]]
Longest Gap: [9, 11]
Missing Count: 6
Result JSON: {"gaps": [[4, 6], [9, 11]], "longest_gap": [9, 11], "missing_count": 6}
```

---

## Methods Overview

### `len(number_list: list[int] | None = None) -> int`

Returns the length of the provided list (or the frame list if none is given).

### `max(number_list: list[int] | None = None) -> int`

Returns the maximum number in the list. If empty, returns `0`.

### `find_missing_frames() -> list[int]`

Finds frames that are missing between `1` and the maximum frame number.

### `find_frame_gaps() -> list[list[int]]`

Finds ranges of missing frames between consecutive frames.
Each gap is returned as `[start, end]`.

### `find_longest_frame_gap() -> list[int]`

Returns the largest missing range as `[start, end]`.
If no gaps exist, returns an empty list.

### `missing_count() -> int`

Returns the total number of missing frames.

### `get_result() -> str`

Returns a JSON string summarizing:

* Gaps
* Longest gap
* Missing frame count
