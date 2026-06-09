from utils.game_object import GameObject

# Define a Scene class
class Scene:
    """
    Scene class
    """

    # An initializer
    def __init__(self):
        """
        :result: Returns nothing

        Initializes an object list
        """

        # Create object list
        self.object_list: list[GameObject] = []

    # Define add_object
    def add_object(self, object: GameObject):
        """
        :object: A GameObject
        :result: Returns nothing

        Adds the object to the scene
        """

        # Append object to object_list
        self.object_list.append(object)

    # Define remove_object
    def remove_object(self, object: GameObject):
        """
        :object: A GameObject
        :result: Returns nothing

        Remove the object from the scene
        """

        # Remove object from object_list
        self.object_list.remove(object)

    def get_objects(self):
        """
        :result: Returns a reversed list of objects
        """

        # Return the list of objects (reversed)
        return self.object_list[::-1]

    def render(self, buffer: list[list[str]]):
        """
        :buffer: A buffer to be rendered onto
        :result: Returns nothing

        Renders the scene
        """

        # For each object in the object_list
        for object in self.object_list:
            # Render it
            object.render(buffer)