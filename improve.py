from file_utils import read_system_prompt, write_suggested_improvement
from openai_wrapper import OpenaiWrapper


improvement_system_prompt = """
# About this program

You will improve the system prompt to make the game more interesting. The system prompt is the text that the AI sees before it generates its response. It is the AI's "context" for the conversation.

"""

ow = OpenaiWrapper("gpt-4")
game_system_prompt = read_system_prompt()

new_prompt = ow.prompt_once(improvement_system_prompt, game_system_prompt)

print(new_prompt)
write_suggested_improvement(new_prompt)