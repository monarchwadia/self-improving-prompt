# This class reads from the /config folder, which contains the following files:
# /config/1.5-output-prompt.md
# /config/2.5-feedback-prompt.md
class ConfigReader:
    def __init__(self) -> None:
        pass

    def read_seed_prompt(self):
        with open("./config/1-seed-prompt.md", "r") as f:
            return f.read()

    def read_output_prompt(self):
        with open("./config/1.5-output-prompt.md", "r") as f:
            return f.read()
    
    def read_feedback_prompt(self):
        with open("./config/2.5-feedback-prompt.md", "r") as f:
            return f.read()
    
    def read_artifact_prompt(self):
        with open("./config/3.5-artifact-prompt.md", "r") as f:
            return f.read()