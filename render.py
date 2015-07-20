import jinja2
import os
from glob import glob

template_dir = "templates"

template_dirs = [os.path.join(os.path.dirname(__file__), directory) for directory in [template_dir, "macros"]]

jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dirs))

def render_document(template_path):
    template = jinja_env.get_template(template_path)
    rendered = template.render().encode('utf8')
    destination = os.path.join("build", template_path)
    f = file(destination, "w")
    f.write(rendered)
    f.close()

templates = [path.replace(template_dir + "/", "") for path in glob(os.path.join(template_dir, "*.html"))]

for template in templates:
    render_document(template)
