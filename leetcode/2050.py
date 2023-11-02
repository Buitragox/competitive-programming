# 20/10/2023 dd/mm/yyyy
# Jhoan Buitrago
# https://leetcode.com/problems/parallel-courses-iii/

from collections import deque

class Solution:
    def minimumTime(self, n: int, relations: list[list[int]],
                    time: list[int]) -> int:
        """
        This solution uses kahns algorithm to traverse the tree of courses in
        topological order and calculate the end_time of each course. The maximum
        end_time (current_time) is the minimum time required to finish all courses. 

        To decide the end_time of each course, it gets the maximum end_time
        between all the prerequisites and adds the required time to complete the course.

        The current_time is updated if the end_time of the course is 
        greater than the current_time.
        """

        # Create a graph, inverse graph and edge count
        graph = [[] for _ in range(n)]
        inv_graph = [[] for _ in range(n)] #prerequisites of each node.
        edge_count = [0 for _ in range(n)]
        for r in relations:
            graph[r[0] - 1].append(r[1] - 1)
            inv_graph[r[1] - 1].append(r[0] - 1)
            edge_count[r[1] - 1] += 1 # Count existing edges for each node
        
        # start queue with courses that have no prerequisites
        queue = deque([i for i, count in enumerate(edge_count) if count == 0])

        end_time = [0 for _ in range(n)]
        current_time = 0

        while len(queue) > 0:
            node = queue.popleft()

            # get the max end time of the prerequisites
            prev_end_time = 0
            for prev_node in inv_graph[node]:
                prev_end_time = max(prev_end_time, end_time[prev_node])
            
            end_time[node] = time[node] + prev_end_time
            current_time = max(current_time, end_time[node])

            #Reduce edge counts
            for next_node in graph[node]:
                edge_count[next_node] -= 1
                if edge_count[next_node] == 0:
                    queue.append(next_node)

        return current_time



if __name__ == "__main__":
    n = 6
    relations = [[1, 5], [2, 5], [3, 5], [3, 4], [4, 5], [1, 6]]
    time = [1, 2, 3, 4, 7, 12]
    expected = 14

    s = Solution()
    print(f"Expected: {expected}")
    print(f"Result: {s.minimumTime(n, relations, time)}")
