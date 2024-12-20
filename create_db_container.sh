az cosmosdb sql database create --account-name bill-test-cosmos-db --resource-group <your_resource_group> --name SchoolDB
az cosmosdb sql container create --account-name bill-test-cosmos-db --resource-group <your_resource_group> --database-name SchoolDB --name StudentsCoursesContainer --partition-key-path /studentId

