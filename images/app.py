from subprocess import run, PIPE
from os import environ
from flask import Flask, send_from_directory

app = Flask(__name__)
app.config["DEBUG"] = True
app.config["IMAGE_DIR"] = "artwork"
app.config["LINK_PREFIX"] = "/img"
app.config["LINK_DEFAULT"] = app.config["IMAGE_DIR"] + "/projects/kubernetes/icon/color/kubernetes-icon-color.svg"

@app.route('/', methods=['GET'])
def list():
  process = run(['find', app.config["IMAGE_DIR"], "-name", "*.svg"], check=True, stdout=PIPE, universal_newlines=True)
  lines = process.stdout.split("\n")
  images = []
  for line in lines:
    if line.endswith(".svg"):
      images.append(linkify(line))
  return "<ul><li>" + "</li><li>".join(images) + "</ul>" 
    
@app.route('/img/<path:path>', methods=["GET"])
def send_file(path):
  if '/' in path:
    return send_from_directory(app.config["IMAGE_DIR"], path)
  else:
    print(find(path))
    return send_from_directory(".", find(path))

@app.route('/search/<name>', methods=["GET"])
def search(name):
  return linkify(find(name))

def find(name):
  process = run(['find', app.config["IMAGE_DIR"], "-name", name+"*.svg"], check=True, stdout=PIPE, universal_newlines=True)
  lines = process.stdout.split("\n")

  # 1 - the preferred image is color icon svg
  for line in lines:
    if "icon/color/{name}-icon-color.svg".format(name=name) in line:
      return line

  # 2 - prefer icon color svg
  for line in lines:
    if "{name}-icon-color.svg".format(name=name) in line:
      return line

  # 3 - prefer icon color svg
  for line in lines:
    if "{name}-icon".format(name=name) in line and line.endswith(".svg"):
      return line

  # 4 - next any color svg
  for line in lines:
    if "/color/" in line and name in line and line.endswith(".svg"):
      return line

  # 5 - any svg
  for line in lines:
    if line.endswith(".svg"):
      return line
  return app.config["LINK_DEFAULT"]

def linkify(path):
  href = app.config["LINK_PREFIX"] + path.split(app.config["IMAGE_DIR"]).pop()
  return "<a href={href}>{href}</a>".format(href=href)


if __name__ == "__main__":
    port = int(environ.get('PORT', 8080))
    host = environ.get('HOST', "0.0.0.0")
    dbg = environ.get('DEBUG', False)
    app.run(debug=dbg, host=host, port=port)