from gremlin_python.structure.graph import Graph
from gremlin_python.process.graph_traversal import __
from gremlin_python.driver.driver_remote_connection import DriverRemoteConnection
from gremlin_python.driver.serializer import GraphSONMessageSerializer

# Connect to JanusGraph
graph = Graph()
serializer = GraphSONMessageSerializer()
connection = DriverRemoteConnection('ws://localhost:8182/gremlin', 'g', message_serializer=serializer)
g = graph.traversal().withRemote(connection)

# Create Game of Thrones graph
print("Creating Game of Thrones graph...")

# Create characters
print("Creating Game of Thrones characters...")
jon_snow = g.addV('Character').property('name', 'Jon Snow').next()
arya_stark = g.addV('Character').property('name', 'Arya Stark').next()
daenerys_targaryen = g.addV('Character').property('name', 'Daenerys Targaryen').next()

# Create houses
print("Creating Game of Thrones houses...")
stark_house = g.addV('House').property('name', 'House Stark').next()
targaryen_house = g.addV('House').property('name', 'House Targaryen').next()

# Create relationships
print("Creating Game of Thrones relationships...")
g.V(jon_snow).addE('belongsTo').to(stark_house).next()
g.V(arya_stark).addE('belongsTo').to(stark_house).next()
g.V(daenerys_targaryen).addE('belongsTo').to(targaryen_house).next()

# Close the connection
connection.close()
print("Done!")
