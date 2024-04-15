import re


class Node:
    def __init__(self, name, left, right) -> None:
        self.name = name
        self.left = left
        self.right = right

    @staticmethod
    def from_line(input_string):
        match = re.search("(\w+) = \((\w+), (\w+)\)", input_string)
        return Node(match.group(1), match.group(2), match.group(3))


class Network:
    def __init__(self, header):
        self.header = header
        self.nodes = []

    @staticmethod
    def from_input(text):
        network = Network(Network.get_directions_header(text))
        create_node = lambda line: Node.from_line((line))
        nodes = [create_node(line) for line in Network.get_network_body(text).strip().splitlines()]
        network.nodes = nodes
        return network

    @staticmethod
    def get_network_body(text):
        return text[text.find("\n") + 1:]

    @staticmethod
    def get_directions_header(test_string):
        newline_position = test_string.find("\n")

        return test_string[:newline_position]


class TestDay8:

    def test_get_directions_header(self):
        test_string = """RLL
        
        AAA = (BBB, ZZZ)
        """
        result = Network.get_directions_header(test_string)
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

    def test_parsing_simple_input_delivers_one_node_network(self):
        result = Network.from_input("""RLL
        
        AAA = (BBB, ZZZ)
        """)
        assert result.header == "RLL"
        assert len(result.nodes) == 1
        assert result.nodes[0].name == "AAA"
        assert result.nodes[0].left == "BBB"
        assert result.nodes[0].right == "ZZZ"

    def test_parsing_simple_input_delivers_one_node_network2(self):
        result = Network.from_input("""L

        CCC = (ZZZ, GGG)
        """)
        assert result.header == "L"
        assert len(result.nodes) == 1
        assert result.nodes[0].name == "CCC"
        assert result.nodes[0].left == "ZZZ"
        assert result.nodes[0].right == "GGG"
