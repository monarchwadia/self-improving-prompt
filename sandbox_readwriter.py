# This class reads and writes (always replacing all contents) from the /config folder, which contains the following files:
# /sandbox/1-artifact.md
# /sandbox/2-output.md
# /sandbox/3-feedback.md
class SandboxReadwriter:
    def __init__(self) -> None:
        pass

    def read_artifact(self):
        with open("./sandbox/1-artifact.md", "r") as f:
            return f.read()
    
    def write_artifact(self, artifact):
        with open("./sandbox/1-artifact.md", "w") as f:
            f.write(artifact)
    
    def read_output(self):
        with open("./sandbox/2-output.md", "r") as f:
            return f.read()
    
    def write_output(self, output):
        with open("./sandbox/2-output.md", "w") as f:
            f.write(output)

    def read_feedback(self):
        with open("./sandbox/3-feedback.md", "r") as f:
            return f.read()

    def write_feedback(self, feedback):
        with open("./sandbox/3-feedback.md", "w") as f:
            f.write(feedback)
            