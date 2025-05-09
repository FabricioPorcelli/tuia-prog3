from ..models.grid import Grid
from ..models.frontier import PriorityQueueFrontier
from ..models.solution import NoSolution, Solution
from ..models.node import Node

# función heurística 'manhattan'
# Suma de las diferencias absolutas entre las coordenadas del nodo actual
def manhattan(pos1: tuple[int, int], pos2: tuple[int, int]) -> int:
    return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])

class GreedyBestFirstSearch:
    @staticmethod
    def search(grid: Grid) -> Solution:
        """Find path between two points in a grid using Greedy Best First Search

        Args:
            grid (Grid): Grid of points

        Returns:
            Solution: Solution found
        """
        start = grid.start
        goal = grid.end
        node = Node("", start, 0)

        frontier = PriorityQueueFrontier()
        frontier.add(node, priority=manhattan(start, goal))
        explored = {}

        while not frontier.is_empty():
            node = frontier.pop()
            explored[node.state] = True

            if node.state == goal:
                return Solution(node, explored)

            for action, pos in grid.get_neighbours(node.state).items():
                if pos not in explored:
                    child = Node(action, pos, 0, parent=node)
                    frontier.add(child, priority=manhattan(pos, goal))

        return NoSolution(explored)
