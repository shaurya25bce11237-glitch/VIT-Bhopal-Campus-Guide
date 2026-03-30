import collections

campus_map = {
    'Main Gate': ['Security Office', 'Parking'],
    'Security Office': ['Main Gate', 'Academic Block 1'],
    'Parking': ['Main Gate', 'Hostel Block A'],
    'Academic Block 1': ['Security Office', 'Academic Block 2', 'Canteen'],
    'Academic Block 2': ['Academic Block 1', 'Lab Complex', 'Library'],
    'Hostel Block A': ['Parking', 'Hostel Block B', 'Canteen'],
    'Hostel Block B': ['Hostel Block A', 'Sports Complex'],
    'Canteen': ['Academic Block 1', 'Hostel Block A', 'Library'],
    'Library': ['Academic Block 2', 'Canteen'],
    'Lab Complex': ['Academic Block 2', 'Research Wing'],
    'Sports Complex': ['Hostel Block B'],
    'Research Wing': ['Lab Complex']
}

class CampusNavigatorAgent:
    def __init__(self, graph):
        self.graph = graph

    def get_percept(self):
        print("\n--- VIT Bhopal Campus Navigator (BFS Agent) ---")
        print("Available Locations:")
        for location in self.graph:
            print(f"- {location}")
        start = input("\nWhere are you now? ").strip()
        goal = input("Where do you want to go? ").strip()
        return start, goal

    def search(self, start_node, goal_node):
        if start_node not in self.graph or goal_node not in self.graph:
            return None

        queue = collections.deque([[start_node]])
        visited = set([start_node])

        while queue:
            path = queue.popleft()
            current = path[-1]
            if current == goal_node:
                return path
            for neighbor in self.graph.get(current, []):
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(path + [neighbor])
        return None

    def display_result(self, path):
        if path:
            print("\n✅ Destination reached!")
            print("Route:", " -> ".join(path))
            print("Steps:", len(path) - 1)
        else:
            print("\n❌ Sorry, there's no path between those locations.")

def main():
    agent = CampusNavigatorAgent(campus_map)

    while True:
        start, goal = agent.get_percept()

        if not start or not goal:
            print("Hey, you can't leave those empty. Try again.")
            continue

        path = agent.search(start, goal)
        agent.display_result(path)

        again = input("\nWant to find another route? (yes/no): ").strip().lower()
        if again != 'yes':
            print("Exiting Campus Navigator. Safe travels!")
            break

if __name__ == "__main__":
    main()