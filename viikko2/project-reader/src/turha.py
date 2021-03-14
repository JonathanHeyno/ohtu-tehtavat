from urllib import request
from project import Project
import toml
from project_reader import ProjectReader


def suorita():
    url = "https://raw.githubusercontent.com/ohjelmistotuotanto-hy-avoin/python-kevat-2021/main/koodi/viikko3/web-login-robot/pyproject.toml"
    reader = ProjectReader(url)
    reader.get_project()
    #print(reader.get_project())
    #content = request.urlopen(url).read().decode("utf-8")
    #data = toml.load(content)
    #mita = data.values()
    #print(mita)
    #print(toml.load("tyhmatoml.toml"))




if __name__ == "__main__":
    suorita()