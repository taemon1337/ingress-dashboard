import os, subprocess
from flask import Flask, send_from_directory

app = Flask(__name__)
app.config["DEBUG"] = True
app.config["IMAGE_DIR"] = "artwork"
app.config["LINK_PREFIX"] = "/img"

@app.route('/', methods=['GET'])
def list():
  process = subprocess.run(['find', app.config["IMAGE_DIR"], "-name", "*.svg"], check=True, stdout=subprocess.PIPE, universal_newlines=True)
  lines = process.stdout.split("\n")
  images = []
  for line in lines:
    if line.endswith(".svg"):
      images.append(linkify(line))
  return "<ul><li>" + "</li><li>".join(images) + "</ul>" 
    
@app.route('/img/<path:path>', methods=["GET"])
def send_file(path):
    return send_from_directory(app.config["IMAGE_DIR"], path)

@app.route('/search/<name>', methods=["GET"])
def find(name):
  process = subprocess.run(['find', app.config["IMAGE_DIR"], "-name", name+"*.svg"], check=True, stdout=subprocess.PIPE, universal_newlines=True)
  lines = process.stdout.split("\n")

  # 1 - the preferred image is color icon svg
  for line in lines:
    if "icon/color/{name}-icon-color.svg".format(name=name) in line:
      return linkify(line)

  # 2 - prefer icon color svg
  for line in lines:
    if "{name}-icon-color.svg".format(name=name) in line:
      return linkify(line)

  # 3 - prefer icon color svg
  for line in lines:
    if "{name}-icon".format(name=name) in line and line.endswith(".svg"):
      return linkify(line)

  # 4 - next any color svg
  for line in lines:
    if "/color/" in line and name in line and line.endswith(".svg"):
      return linkify(line)

  # 5 - any svg
  for line in lines:
    if line.endswith(".svg"):
      return linkify(line)
  print(process.stdout)
  return ""

def linkify(path):
  href = app.config["LINK_PREFIX"] + path.split(app.config["IMAGE_DIR"]).pop()
  return "<a href={href}>{href}</a>".format(href=href)


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 8080))
    host = os.environ.get('HOST', "0.0.0.0")
    dbg = os.environ.get('DEBUG', False)
    app.run(debug=dbg, host=host, port=port)