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
        network_body = Network.get_network_body(text)
        nodes = [Node.from_line(_) for _ in network_body.strip().splitlines()]
        network.nodes = nodes
        return network

    @staticmethod
    def from_file(filepath):
        f = open(filepath, "r")
        file_input = f.read() 
        f.close()

        return Network.from_input(file_input)

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

    def test_parsing_simple_input_delivers_two_nodes_network(self):
        result = Network.from_input("""L

        CCC = (ZZZ, GGG)
        ZZZ = (ZZZ, ZZZ)
        """)
        assert result.header == "L"
        assert len(result.nodes) == 2
        assert result.nodes[0].name == "CCC"
        assert result.nodes[0].left == "ZZZ"
        assert result.nodes[0].right == "GGG"
        assert result.nodes[1].name == "ZZZ"
        assert result.nodes[1].left == "ZZZ"
        assert result.nodes[1].right == "ZZZ"

    def test_parsing_file_with_two_nodes_network(self):
        result = Network.from_file("tests/simple_2_nodes_network.txt")
        assert len(result.nodes) == 2

    def test_parsing_mmgs_inputfile_(self):
        print gmtime()
        result = Network.from_file("data/full_input_mmg.txt")
        assert len(result.nodes) == 746
