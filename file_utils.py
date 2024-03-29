def read_system_prompt():
    with open("./system_prompt.md", "r") as f:
        return f.read()
    
def read_log():
    with open("./.log.md", "r") as f:
        return f.read()

def write_log(state):
    with open("./.log.md", "w") as f:
        f.write(state)

def write_suggested_improvement(suggested_improvement):
    with open("./system_prompt.md", "w") as f:
        f.write(suggested_improvement)