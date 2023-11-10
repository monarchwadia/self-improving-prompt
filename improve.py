from file_utils import read_log, read_system_prompt, write_suggested_improvement
from openai_wrapper import OpenaiWrapper

# First, generate a criticism of the previous system prompt
def improve():
    ow = OpenaiWrapper("gpt-4")
    game_system_prompt = read_system_prompt()
    log = read_log()

    criteria = """
    # The game

    This is an idle game. The user cannot take actions, but can only read the AI's responses. The goal is to realistically simulate a game system, and to generate interesting responses.

    # Criteria for a good game system prompt

    The game is more interesting if the following attributes are met:

    1. USER INPUT OR INTERACTION IS BANNED. This is an idle zero-player game.
    1. There is a hard limit to how many tokens the LLM can take (only 4098 at max). Therefore, it is CRITICAL that the AI's response is short and to the point, while still being interesting.
    1. Adding on to the above point: the AI's response should be VERY short. Focus on the most important information, and leave out the rest.
    1. The AI's response summarizes the economy of the game, so that the user can read the AI's response and understand the state of the game.
    1. The AI generates interesting responses that are not too repetitive.
    1. However, the AI's responses should not be too complex, or else the user will not be able to understand the state of the game.

    # Criteria for a good criticism

    - Do NOT suggest that user input or interaction be added. This is an idle zero-player game.
    - Continuously suggest a high fantasy setting that has magic and dragons.
    - Make sure you point out any inconsistencies with these current criteria.


    """
    criticism = ow.prompt_once("# Game system prompt\n\n```markdown\n\n" + game_system_prompt + "\n```\n\n# Log of the previous game\n\n```markdown\n" + log + "\n```\n\n", "Can you please analyze the game system prompt and the log of the previous game and generate a criticism of the game system prompt, along with suggestions for improvement? \n\n" + criteria)

    print(criticism)

    new_prompt = ow.prompt_once(game_system_prompt, "Improve the game system prompt with the following suggestions:\n\n" + criticism + "\n\n. Output the full and final, improved, game system prompt.")

    # print(new_prompt)
    write_suggested_improvement(new_prompt)