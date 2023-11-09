from file_utils import read_system_prompt, write_log
from openai_wrapper import OpenaiWrapper


# ====================

ow = OpenaiWrapper("gpt-3.5-turbo")

state = """
Day 1

There are 5 humans in the camp.
There are 50 units of food in the camp.
There are 5 units of wood in the camp.
"""
system_prompt = read_system_prompt()

write_log(state)
while True:
    new_state = ow.prompt_once(system_prompt, state)
    print("\n\n" + new_state)
    state = state + "\n\n" + new_state
    write_log(state)
