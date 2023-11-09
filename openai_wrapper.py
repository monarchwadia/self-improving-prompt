from openai import OpenAI
from dotenv import load_dotenv
load_dotenv()

class OpenaiWrapper:
    def __init__(self, model: str) -> None:
        self.client = OpenAI(
            # defaults to os.environ.get("OPENAI_API_KEY")
        )
        self.model = model
        pass

    def prompt_once(self, system_prompt: str, message: str):
        chat_completion = self.client.chat.completions.create(
            messages=[
                {
                    "role": "system",
                    "content": system_prompt
                },
                {
                    "role": "user",
                    "content": message,
                }
            ],
            model=self.model
        )

        return chat_completion.choices[0].message.content

