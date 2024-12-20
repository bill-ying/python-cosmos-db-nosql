from azure.cosmos import CosmosClient

# Initialize the Cosmos client
endpoint = "https://bill-test-cosmos-db.documents.azure.com:443/"
key = "your cosmos db key"
client = CosmosClient(endpoint, key)

# Create a database client
database_name = 'SchoolDB'
database = client.get_database_client(database_name)

# Create a container client
container_name = 'StudentsCoursesContainer'
container = database.get_container_client(container_name)

# 1) Read and print the student names who take course "Advanced Mathematics"
query = "SELECT c.name FROM c WHERE ARRAY_CONTAINS(c.courses, 'C002')"
students = list(container.query_items(query=query, enable_cross_partition_query=True))

print("Students taking 'Advanced Mathematics':")
[print(student['name']) for student in students]

# 2) Delete student2
container.delete_item(item='student2', partition_key='S002')

print("Student 'student2' deleted successfully.")

# 3) Read and print the student names who take course "Advanced Mathematics" again
students_after_delete = list(container.query_items(query=query, enable_cross_partition_query=True))

print("Students taking 'Advanced Mathematics' after deletion:")
[print(student['name']) for student in students_after_delete]
