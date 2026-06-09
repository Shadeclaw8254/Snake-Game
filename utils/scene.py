from utils.game_object import GameObject

class Scene:
    def __init__(self):
        self.object_list: list[GameObject] = []

    def add_object(self, object: GameObject):
        self.object_list.append(object)

    def remove_object(self, object: GameObject):
        self.object_list.remove(object)

    def get_objects(self):
        return self.object_list[::-1]

    def render(self, buffer: list[list[str]]):
        for object in self.object_list:
            object.render(buffer)