# print x 10 times
from config_reader import ConfigReader
from improve import improve
from openai_wrapper import OpenaiWrapper
from play import play
from sandbox_readwriter import SandboxReadwriter


if __name__ == "__main__":
    # improve()
    # play()
    ow35 = OpenaiWrapper("gpt-3.5-turbo")
    ow40 = OpenaiWrapper("gpt-4")
    config_reader = ConfigReader()
    sandbox_readwriter = SandboxReadwriter()

    artifact = sandbox_readwriter.read_artifact()
    output_prompt = config_reader.read_output_prompt()

    output = ow40.prompt_once(output_prompt, artifact)
    print(output)
    sandbox_readwriter.write_output(output)

    feedback_prompt = config_reader.read_feedback_prompt()
    feedback = ow40.prompt_once(feedback_prompt, "# Artifact\n\n" + artifact + "\n\n========================\n\n# Output\n\n" + output + "\n\n")
    print(feedback)
    sandbox_readwriter.write_feedback(feedback)

    artifact_prompt = config_reader.read_artifact_prompt()
    new_artifact = ow40.prompt_once(artifact_prompt, feedback)
    print(new_artifact)
    sandbox_readwriter.write_artifact(new_artifact)

    print("\n\nDone!")