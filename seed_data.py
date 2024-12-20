from azure.cosmos import CosmosClient, PartitionKey

# Initialize the Cosmos client
endpoint = "https://bill-test-cosmos-db.documents.azure.com:443/"
key = "your cosmos db key"
client = CosmosClient(endpoint, key)

# Create a database
database_name = 'SchoolDB'
database = client.create_database_if_not_exists(id=database_name)

# Create a container
container_name = 'StudentsCoursesContainer'
container = database.create_container_if_not_exists(
    id=container_name,
    partition_key=PartitionKey(path='/studentId')
)

# Insert course documents
container.create_item(body={
    'id': 'course1',
    'courseId': 'C001',
    'title': 'Introduction to Computer Science',
    'description': 'A beginner course on computer science.'
})

container.create_item(body={
    'id': 'course2',
    'courseId': 'C002',
    'title': 'Advanced Mathematics',
    'description': 'An advanced course on mathematics.'
})

# Insert student documents
container.create_item(body={
    'id': 'student1',
    'studentId': 'S001',
    'name': 'John Doe',
    'age': 20,
    'courses': []
})

container.create_item(body={
    'id': 'student2',
    'studentId': 'S002',
    'name': 'Jane Smith',
    'age': 22,
    'courses': ['C002']
})

# Update a student document
student_item = container.read_item(item='student1', partition_key='S001')
student_item['courses'] = ['C001', 'C002']
container.replace_item(item=student_item['id'], body=student_item)

print("Data inserted and updated successfully.")
