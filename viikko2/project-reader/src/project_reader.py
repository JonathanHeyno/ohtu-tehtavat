from urllib import request
from project import Project
import toml


class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")

        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        tieto = toml.loads(content)
        tool = tieto.get("tool")
        poetry = tool.get("poetry")

        return Project(poetry.get("name"), poetry.get("description"), poetry.get("dependencies"), poetry.get("dev-dependencies"))