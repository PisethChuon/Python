from jinja2 import Template

# Create a template string
template = Template("Hello {{ name }}!") # name

# Define the data
data = {"name": "Chanthy"}

# Render template
output = template.render(data)
print(output)
