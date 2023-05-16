left_frame_background_color = "black"
right_frame_background_color = "#121212"
music_player_bar_background_color = "#242526"

red_color = "#ED1B1B"
dark_red_color = "#520100"
hover_dark_red_color = "#750405"


def get_dir_path():
    import os
    return os.path.dirname(os.path.realpath(__file__)).replace("\\", "/")


def reduce_text(string: str, limit_character: int):
    result = string[:limit_character]
    if len(string) > limit_character:
        result += "..."
    return result
