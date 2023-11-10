# print x 10 times
from config_reader import ConfigReader
from openai_wrapper import OpenaiWrapper
from sandbox_readwriter import SandboxReadwriter

def print_header(text):
    print("========================", flush=True)
    print(text)
    print("========================", flush=True)

if __name__ == "__main__":
    # Setting up dependencies
    ow35 = OpenaiWrapper("gpt-3.5-turbo")
    ow40 = OpenaiWrapper("gpt-4")
    config_reader = ConfigReader()
    sandbox_readwriter = SandboxReadwriter()

    print_header("Output.")
    output = ow40.prompt_once(
        config_reader.read_output_prompt(),
        sandbox_readwriter.read_artifact()
    )
    print(output)
    sandbox_readwriter.write_output(output)

    print_header("Feedback.")
    feedback = ow40.prompt_once(
        config_reader.read_feedback_prompt(), 
        "# Artifact\n\n{artifact}\n\n========================\n\n# Output\n\n{output}\n\n".format(
            artifact=sandbox_readwriter.read_artifact(), 
            output=sandbox_readwriter.read_output()
        )
    )
    print(feedback)
    sandbox_readwriter.write_feedback(feedback)

    print_header("New Artifact.")
    new_artifact = ow40.prompt_once(config_reader.read_artifact_prompt(), feedback)
    print(new_artifact)
    sandbox_readwriter.write_artifact(new_artifact)

    print("\n\nDone!")