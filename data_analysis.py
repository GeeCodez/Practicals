import pandas as pd

data = [
    ["Name", "Category", "Description", "Use_Case"],

    ["Django REST Framework", "Framework", "Powerful toolkit for building REST APIs in Django", "Building scalable REST APIs"],
    ["Django", "Backend Framework", "High-level Python web framework", "Core backend for API development"],
    ["Serializers", "Concept", "Converts complex data to JSON and vice versa", "API data transformation"],
    ["Views", "Concept", "Handles API request/response logic", "Processing API endpoints"],
    ["URLs", "Routing", "Maps endpoints to views", "API endpoint structure"],

    ["JWT Authentication", "Security", "Token-based authentication system", "Secure user login in APIs"],
    ["OAuth2", "Security Protocol", "Authorization framework", "Third-party login systems"],
    ["Session Authentication", "Security", "Uses server-side sessions", "Traditional login systems"],

    ["Postman", "Tool", "API testing tool", "Testing API endpoints"],
    ["Insomnia", "Tool", "REST client for APIs", "Debugging API requests"],

    ["GET Method", "HTTP Method", "Retrieves data from server", "Fetching API data"],
    ["POST Method", "HTTP Method", "Creates new data", "Creating resources"],
    ["PUT Method", "HTTP Method", "Updates entire resource", "Full updates"],
    ["PATCH Method", "HTTP Method", "Partial update of resource", "Partial updates"],
    ["DELETE Method", "HTTP Method", "Removes data", "Deleting resources"],

    ["JSON", "Data Format", "Lightweight data exchange format", "API data structure"],
    ["REST Architecture", "Architecture", "Design style for APIs", "Building scalable APIs"],
    ["GraphQL", "API Type", "Query language for APIs", "Flexible data fetching"],

    ["CORS", "Security", "Controls cross-origin requests", "Frontend-backend communication"],
    ["CSRF Protection", "Security", "Prevents cross-site request forgery", "Securing API requests"],
    ["Rate Limiting", "Security", "Limits number of requests", "Prevent API abuse"],
    ["Input Validation", "Security", "Validates incoming data", "Prevent injection attacks"],

    ["Django Middleware", "Concept", "Processes requests globally", "Logging and security checks"],
    ["ORM", "Database Tool", "Object Relational Mapper", "Database interaction"],
    ["SQLite", "Database", "Lightweight database engine", "Development testing"],
    ["PostgreSQL", "Database", "Advanced relational database", "Production APIs"],

    ["Docker", "DevOps Tool", "Containerization platform", "API deployment"],
    ["CI/CD Pipeline", "DevOps", "Automates deployment process", "Continuous API delivery"],
    ["Swagger / OpenAPI", "Documentation Tool", "API documentation generator", "API documentation"],
    ["Logging", "Monitoring", "Tracks API activity", "Debugging and monitoring"],
    ["Throttling", "Security", "Controls request rate", "Prevent overload"]
]

df = pd.DataFrame(data)


print(df)

# Export to CSV
df.to_csv("api_development_tools.csv", index=False)

print("API dataset CSV created successfully!")


