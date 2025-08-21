from tools.tools import Tools

frame_list = [1, 2, 3, 5, 6, 10, 11, 16]
if __name__ == "__main__":
    tool = Tools(frame_list)
    print(tool.get_result())
