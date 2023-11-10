# Python code to generate the HTML and CSS for the requested table structure

from config_reader import ConfigReader
from model import Artifact
from playhouse.shortcuts import model_to_dict


# As we don't have access to the SQLite database, I'll simulate the data as a list of dictionaries
# The actual implementation would involve querying the SQLite database and iterating through the results
def get_history():
    history = Artifact.select().order_by(Artifact.id.asc())
    history_json = []
    for artifact in history:
        history_json.append(model_to_dict(artifact))
    return history_json

# Generate table rows with accordion for prompt and feedback
data = get_history()
cr = ConfigReader()
# Generate table rows with accordion for prompt and feedback
table_rows = ""
for row in data:
    table_rows += f"""
    <tr>
        <td>{row["id"]}</td>
        <td>{row["output"]}</td>
        <td>
            <button class="accordion">Details</button>
            <div class="panel">
                <p><strong>Prompt:</strong> {row["prompt"]}</p>
                <p><strong>Feedback:</strong> {row["feedback"]}</p>
            </div>
        </td>
    </tr>
    """

html_output = """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<style>
body {
    font-family: Arial, sans-serif;
}
table {
    width: 100%;
    border-collapse: collapse;
}
th, td {
    padding: 8px;
    text-align: left;
    border-bottom: 1px solid #ddd;
}
tr:hover {background-color: #f5f5f5;}
.accordion {
    background-color: #eee;
    color: #444;
    cursor: pointer;
    padding: 18px;
    width: 100%;
    text-align: left;
    border: none;
    outline: none;
    transition: 0.4s;
}
.active, .accordion:hover {
    background-color: #ccc;
}
.panel {
    padding: 0 18px;
    background-color: white;
    display: none;
    overflow: hidden;
}
</style>
</head>
<body>

<h2>SQLite Table Output</h2>

<h3>Iteration History</h3>

<p>Click on the button to toggle between showing and hiding the panel.</p>

<p style="color: white; background-color: blue"><strong>SEED PROMPT:</strong> """ + cr.read_seed_prompt() + """.</p>

<table>
  <tr>
    <th>Iteration#</th>
    <th>Output</th>
    <th>Details</th>
  </tr>
  <!-- Table rows will be inserted here -->
    """ + table_rows + """
</table>

<script>
var acc = document.getElementsByClassName("accordion");
var i;

for (i = 0; i < acc.length; i++) {
  acc[i].addEventListener("click", function() {
    this.classList.toggle("active");
    var panel = this.nextElementSibling;
    if (panel.style.display === "block") {
      panel.style.display = "none";
    } else {
      panel.style.display = "block";
    }
  });
}
</script>

</body>
</html>
"""

# Output the HTML content to a .html file
html_file_path = './output.html'
with open(html_file_path, 'w') as file:
    file.write(html_output)

html_file_path
