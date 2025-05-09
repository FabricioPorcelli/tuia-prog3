from ..models.grid import Grid
from ..models.frontier import PriorityQueueFrontier
from ..models.solution import NoSolution, Solution
from ..models.node import Node

# función heurística 'manhattan'
# Suma de las diferencias absolutas entre las coordenadas del nodo actual
def manhattan(pos1: tuple[int, int], pos2: tuple[int, int]) -> int:
    return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])

class AStarSearch:
    @staticmethod
    def search(grid: Grid) -> Solution:
        """Find path between two points in a grid using A* Search

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
        explored = {start: 0}

        while not frontier.is_empty():
            node = frontier.pop()

            if node.state == goal:
                return Solution(node, explored)

            for action, pos in grid.get_neighbours(node.state).items():
                g = node.cost + grid.get_cost(pos)
                if pos not in explored or g < explored[pos]:
                    explored[pos] = g
                    f = g + manhattan(pos, goal)
                    child = Node(action, pos, g, parent=node)
                    frontier.add(child, priority=f)

        return NoSolution(explored)