from math import radians, sin, cos, sqrt, asin, factorial
from itertools import permutations
from time import time

EARTH_RADIUS_KM = 6372.8

def haversine(lat1, long1, lat2, long2, planet_radius=EARTH_RADIUS_KM):
    """Return the shortest distance between two coordinates on a sphere.

    This does "as the crow flies."  We don't need to be 100% accurate, just return
    a reasonable weight for the path.  If this was used for flight planning, there's a bunch
    of other factors at play (geopolitical boundaries, weather, curved path could be shorter).

    Use the geographic coordinate system to get weights for pairs of graticules.
    Convert difference between [l1, l2] lat,long to radians.

    translated from https://en.wikipedia.org/wiki/Haversine_formula
    """

    # get distance between the points
    # use vars here to shorten below calc. doing radian of each would be +2 vars
    phi_Lat = radians(lat2 - lat1)
    phi_Long = radians(long2 - long1)

    lat1 = radians(lat1)
    lat2 = radians(lat2)

    a = sin(phi_Lat/2)**2 + \
        cos(lat1) * cos(lat2) * \
        sin(phi_Long/2)**2

    c = 2 * asin(sqrt(a))
    return planet_radius * c


def generate_weights(data):

    graph_edges = {}

    for city in data:
        graph_edges[city[0]] = []

    for city0, city1 in permutations(data, 2):

        weight = haversine(
            city0[1][0],
            city0[1][1],
            city1[1][0],
            city1[1][1],
            EARTH_RADIUS_KM
        )

        graph_edges[city0[0]].append((city1[0], weight))

    return graph_edges


def calculate_number_edges(graph_length):
    # Graph is G = ( Vertice, Edge )
    # G = (Vn * Vn - 1) / 2)
    _l = (graph_length * (graph_length -1)) / 2
    if _l < 4: _l = 4
    return _l


def calculate_dfs(graph, start_and_end_vertex, iteration_limit=None, DEBUG=True):
    """Calculate the shortest trip through all points in graph starting and ending at start_and_end_vertex

    This does a weighted depth-search.
    """

    # Exit if we've looped more times than solutions exist
    iterations = 0
    if not iteration_limit:
        iteration_limit = float("inf")

    lowest_weight_circuit_cost = float("inf")
    lowest_weight_circuit = []

    stack = [([start_and_end_vertex],0)]

    while stack:

        if DEBUG:
            print("=> Stack status: %s" % len(stack))

        iterations += 1
        if iterations >= iteration_limit:
            raise StopIteration('Number of iterations exceeded limit passed: ' + str(iteration_limit))

        path, dist = stack.pop()

        if DEBUG:
            print(path)

        last_city = path[-1]

        if len(path) < len(graph):
            for (next_city, flight_dist) in graph[last_city]:
                if next_city in path:
                    pass
                else:
                    newpath = path + [next_city]
                    stack.append((newpath, dist + flight_dist))
        else:
            for dest in graph[last_city]:
                if dest[0] == start_and_end_vertex:
                    circuit_length = dist + dest[1]
                    path.append(start_and_end_vertex)
            if DEBUG:
                print('Found a complete path '+str(path) + ' cost ='+ str(circuit_length))

            if circuit_length <= lowest_weight_circuit_cost:
               lowest_weight_circuit_cost = circuit_length
               lowest_weight_circuit = path

    return (lowest_weight_circuit, lowest_weight_circuit_cost)


def calculate_shortest_neighbors_trip(graph, start_and_end_vertex, iteration_limit=None, DEBUG=True):
    """Take shortest-path-to-next-path for all points in graph starting and ending at start_and_end_vertex

    Start at start_and_end_vertex.  When we traverse an edge, we choose the next vertex by closest edge.
    We don't visit the same city twice, but we do have a repeat for the start_and_end_vertex.
    """

    iterations = 0
    if not iteration_limit:
        iteration_limit = float("inf")

    lowest_weight_circuit_cost = float("inf")
    lowest_weight_circuit = []

    current_circuit_cost = 0
    current_circuit_history = []

    current_circuit_history.append(start_and_end_vertex)

    stack = [graph[start_and_end_vertex]]

    while stack:

        if DEBUG:
            print("=> Stack status: %s" % stack)

        iterations += 1
        if iterations >= iteration_limit:
            raise StopIteration

        edges_according_to_vertex = stack.pop()


        cheapest_known_path_weight = float("inf")
        next_edge = None

        for potential_path in edges_according_to_vertex:
            if potential_path[0] not in current_circuit_history:
                if potential_path[1] < cheapest_known_path_weight:
                    cheapest_known_path_weight = potential_path[1]
                    next_edge = potential_path

        if next_edge:

            current_circuit_history.append(next_edge[0])
            current_circuit_cost += next_edge[1]

            next_vertex_valid_vertices = []
            next_vertex_all_edges = graph[next_edge[0]]

            for edge in next_vertex_all_edges:
                if edge[0] not in current_circuit_history:
                    next_vertex_valid_vertices.append(edge)

            if DEBUG:
                print("=>       Edges from %s: %s" % (next_edge[0], next_vertex_valid_vertices))
                print("=>       Visited cities: %s" % current_circuit_history)

            stack.append(next_vertex_valid_vertices)

            if DEBUG:
                print("=> [%s]; Vertex: '%s'; Weight: %s; Total trip weight: %s" %
                      (iterations, next_edge[0], next_edge[1], current_circuit_cost))

            if not next_vertex_valid_vertices:
                if DEBUG:
                    print("=> Routing done. Heading from last location back to start.")

                for edge in graph[next_edge[0]]:
                    if edge[0] == start_and_end_vertex:

                        if DEBUG:
                            print("=>       Returning to %s; Distance: %s" % (start_and_end_vertex, edge[1]))
                        current_circuit_history.append(edge[0])
                        current_circuit_cost += edge[1]
                        break

    if current_circuit_cost <= lowest_weight_circuit_cost:
       lowest_weight_circuit_cost = current_circuit_cost
       lowest_weight_circuit = current_circuit_history
    current_circuit_cost = 0

    return (lowest_weight_circuit, lowest_weight_circuit_cost)


def backend_python(data, approach='dfs', debug=False):
    # incoming data looks like:
    #   ('new york, ny, usa', [40.734838, -73.990810])
    #   ('portland, me, usa', [43.657727, -70.254636])
    #   ('seattle, wa, usa', [47.620410, -122.349368])
    #   ('san fransciso, ca, usa', [37.759936, -122.415058])
    graph_vertices_and_edges = generate_weights(data)

    start_time = time()

    if approach=='dfs':
        iteration_limit = factorial(len(graph_vertices_and_edges))
        result = calculate_dfs(graph_vertices_and_edges, 'new york, ny, usa', iteration_limit, debug)

    else:
        iteration_limit = calculate_number_edges(len(graph_vertices_and_edges))
        result = calculate_shortest_neighbors_trip(graph_vertices_and_edges, 'new york, ny, usa', iteration_limit, debug)

    end_time = time()
    time_elapsed_seconds = format(end_time - start_time, '.6f')
    return result, time_elapsed_seconds