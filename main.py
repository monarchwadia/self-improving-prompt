# print x 10 times
import json
from config_reader import ConfigReader
from model import Artifact
from openai_wrapper import OpenaiWrapper
from model import db
from playhouse.shortcuts import model_to_dict

def print_header(text):
    print("========================", flush=True)
    print(text)
    print("========================", flush=True)

if __name__ == "__main__":
    # Setting up dependencies
    db.connect()
    db.create_tables([Artifact])
    ow35 = OpenaiWrapper("gpt-3.5-turbo")
    ow40 = OpenaiWrapper("gpt-4")
    config_reader = ConfigReader()

    # using Peewee, check if there is an existing azrtifact. if there is one, get the latest one.
    wip_artifact = Artifact.select().where(
        (Artifact.prompt.is_null(False)) &
        (Artifact.output.is_null()) & 
        (Artifact.feedback.is_null())
    ).order_by(
        Artifact.id.desc()
    ).first()

    if (wip_artifact == None):
        wip_artifact = Artifact(prompt=config_reader.read_seed_prompt())
        wip_artifact.save()

    print_header("Output.")
    output = ow40.prompt_once(
        config_reader.read_output_prompt(),
        json.dumps(model_to_dict(wip_artifact))
    )
    print(output)

    wip_artifact.output = output
    wip_artifact.save()

    print_header("Feedback.")
    feedback = ow40.prompt_once(
        config_reader.read_feedback_prompt(), 
        json.dumps(model_to_dict(wip_artifact))
    )
    print(feedback)
    wip_artifact.feedback = feedback
    wip_artifact.save()

    print_header("New Prompt.")
    new_prompt = ow40.prompt_once(
        config_reader.read_artifact_prompt(),
        json.dumps(model_to_dict(wip_artifact))
    )
    print(new_prompt)

    new_artifact = Artifact(prompt=new_prompt, from_artifact=wip_artifact)
    new_artifact.save()

    print("\n\nDone!")