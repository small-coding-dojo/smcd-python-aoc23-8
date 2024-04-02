import re


def get_directions_header(test_string):
    newline_position = test_string.find("\n")

    return test_string[:newline_position]




class Node:
    def __init__(self, name, left, right) -> None:
        self.name = name
        self.left = left
        self.right = right

    @staticmethod
    def from_line (input_string):
        match = re.search("(\w+) = \((\w+), (\w+)\)", input_string)
        return Node(match.group(1), match.group(2), match.group(3))

class TestDay8:

    def test_get_directions_header(self):
        test_string = """RLL
        
        AAA = (BBB, ZZZ)
        """
        result = get_directions_header(test_string)
        assert result == "RLL"

    def test_created_node_has_correct_name(self):
        result = Node.from_line("AAA = (BBB, ZZZ)")
        assert result.name == "AAA"

    def test_created_node_has_correct_left(self):
        result = Node.from_line("AAA = (BBB, ZZZ)")
        assert result.left == "BBB"

    def test_created_node_has_correct_right(self):
        result = Node.from_line("AAA = (BBB, ZZZ)")
        assert result.right == "ZZZ"
