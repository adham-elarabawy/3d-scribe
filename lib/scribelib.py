import numpy as np

class Path:
    def __init__(self, input):
        # split the raw GCODE output into discrete letters as scatter points
        filtered_out = np.array(list(filter(lambda i:(type(i) is tuple) or (i == "char_completed"), input)))
        character_indices = np.append(np.array([-1]), np.where(filtered_out=="char_completed"))
        self.characters_points = list()
        for i, _ in enumerate(character_indices[:-1]):
            self.characters_points += [filtered_out[character_indices[i] + 1:character_indices[i+1]]]

        # generate the path from the GCODE input
        print(input)

        # iteratively split into 2 types of moves: draw move and transfer move
        filtered_gcode_commands = np.array(list(filter(lambda i:(type(i) is tuple) or (i == "ON COMMAND") or (i == "OFF COMMAND"), input)))
        prev_command = 'ON COMMAND'
        for command in filtered_gcode_commands:
            

    # def sample(self, time):
    #     return (x, y, z)