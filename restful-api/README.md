# RESTful API

## Background
`curl` (Client URL) is a command-line tool that allows users to transfer data to or from a network server using one of the supported protocols (HTTP, HTTPS, FTP, and more). It’s widely used for debugging, testing, and interacting with RESTful web services and APIs. By mastering `curl`, one can quickly prototype API requests, diagnose server issues, and more, all from the command line.

## Objective
At the end of this exercise, you should be able to:
1. Differentiate between HTTP and HTTPS.
2. Understand the basic working and structure of HTTP requests and responses.
3. Recognize and explain the common HTTP methods and status codes.
4. Install and use `curl` from the command line.
5. Construct and execute basic API requests using `curl`, including setting headers and inspecting the output.
6. Interpret the results of common API requests.

## Resources
- [Mozilla Developer Network (MDN) - An Overview of HTTP](https://developer.mozilla.org/en-US/docs/Web/HTTP/Overview)
- [Difference between HTTP and HTTPS](https://www.cloudflare.com/learning/ssl/why-is-http-not-secure/)
- [List of HTTP status codes](https://en.wikipedia.org/wiki/List_of_HTTP_status_codes)
- [curl - Everything curl](https://everything.curl.dev/)
- [Using cURL to interact with HTTP APIs](https://flaviocopes.com/http-curl/)
- Public API to play with: [JSONPlaceholder](https://jsonplaceholder.typicode.com/)

## Instructions

### 0. Basics of HTTP/HTTPS

#### Differentiating HTTP and HTTPS:
- **HTTP**:
  - No encryption: data is transferred in plain text.
  - Uses port 80.
  - URLs start with `http://`.

- **HTTPS**:
  - Encryption: uses SSL/TLS to secure data.
  - Uses port 443.
  - URLs start with `https://`.

#### Understanding HTTP Structure:
1. **HTTP Request**:
   - **Request Line**: Method (e.g., GET), Path (e.g., /index.html), HTTP Version (e.g., HTTP/1.1)
   - **Headers**: Key-value pairs providing additional information (e.g., Host, User-Agent, Accept)
   - **Body**: Optional, used mainly in POST and PUT requests to send data.

2. **HTTP Response**:
   - **Status Line**: HTTP Version, Status Code (e.g., 200), Status Message (e.g., OK)
   - **Headers**: Key-value pairs providing information about the response (e.g., Content-Type, Content-Length)
   - **Body**: Optional, contains the resource requested by the client.

#### Common HTTP Methods:
1. **GET**:
   - Retrieves data from the server.
   - Use case: Fetching a web page or data from an API.

2. **POST**:
   - Sends data to the server to create/update a resource.
   - Use case: Submitting form data or uploading a file.

3. **PUT**:
   - Updates an existing resource or creates a new one if it does not exist.
   - Use case: Updating user information.

4. **DELETE**:
   - Deletes the specified resource.
   - Use case: Removing a user or a post.

#### Common HTTP Status Codes:
1. **200 OK**:
   - The request has succeeded.
   - Scenario: Successfully retrieved a web page or data.

2. **201 Created**:
   - The request has been fulfilled and resulted in a new resource being created.
   - Scenario: Successfully created a new user or post.

3. **400 Bad Request**:
   - The server could not understand the request due to invalid syntax.
   - Scenario: Sending a malformed request.

4. **404 Not Found**:
   - The server can not find the requested resource.
   - Scenario: When a requested page or resource isn’t available on the server.

5. **500 Internal Server Error**:
   - The server encountered an unexpected condition that prevented it from fulfilling the request.
   - Scenario: When the server encounters an unexpected condition.

### 1. Consume Data from an API using Command Line Tools (curl)

#### Installing and Basic Interaction with `curl`

1. **Install `curl`**:
   - For Linux/Mac: Open the terminal and run:
     ```bash
     sudo apt -get install curl  # For Debian-based systems
     brew install curl          # For macOS using Homebrew
     ```
   - For Windows: Consider using Windows Subsystem for Linux (WSL) or download a Windows version of `curl` from [curl.se](https://curl.se/windows/).

2. **Verify Installation**:
   - Run the following command to confirm `curl` is available:
     ```bash
     curl --version
     ```
   - You should see details about the installed version of `curl`, including supported protocols.

3. **Fetch the Content of a Webpage**:
   - Use `curl` to fetch the content of a webpage:
     ```bash
     curl http://example.com
     ```

#### Fetching Data from an API

1. **Retrieve Posts from JSONPlaceholder**:
   - Use `curl` to get data from the API:
     ```bash
     curl https://jsonplaceholder.typicode.com/posts
     ```
   - Observe the output, which should be a JSON array of posts.

#### Using Headers and Other Options with `curl`

1. **Fetch Only the Headers**:
   - Use the `-I` flag to fetch only the headers of the response:
     ```bash
     curl -I https://jsonplaceholder.typicode.com/posts
     ```

2. **Make a POST Request**:
   - Use the `-X` flag to specify the HTTP method and the `-d` flag to send data:
     ```bash
     curl -X POST -d "title=foo&body=bar&userId=1" https://jsonplaceholder.typicode.com/posts
     ```

## Hints
- The `-I` flag in `curl` fetches only the headers of the response, which can be useful to diagnose server settings, cache controls, content type, and more.
- With the `-X` flag, you can specify an HTTP method for your request. For example, `-X POST` will make a POST request.
- The `-d` flag allows you to pass data in your request. In RESTful APIs, this is commonly used with POST, PUT, or PATCH requests to send data to the server.
- If you’re getting a lot of output and want to view it in a more organized way, consider piping the output to a tool like `jq` for JSON formatting and highlighting.

## Expected Output

1. **Running `curl --version`**:
   - Should display details about your installed version of `curl`, including supported protocols.

2. **Fetching Posts from JSONPlaceholder**:
   - Should provide a JSON output of various posts, each having attributes like `userId`, `id`, `title`, and `body`.

3. **Fetching Only Headers**:
   - Should give a concise output showing status codes and headers without the actual content.

4. **Making a POST Request**:
   - Should yield a response from the server acknowledging the reception of the data. For JSONPlaceholder, it typically returns the created post with an `id` of 101 (since it doesn’t actually save the new post, but simulates the creation).

## Practical Examples in Python

### Example 1: Fetching Data from JSONPlaceholder

**Python Code:**
```python code 

    import requests  # Import the requests library for making HTTP requests
    
    # Make an HTTP GET request to the specified URL
    response = requests.get('https://jsonplaceholder.typicode.com/posts/1')

    # Print the status code of the response (e.g., 200 for OK, 404 for Not Found)
    print('Status Code:', response.status_code)

    # Print the body of the response, parsed as JSON
    print('Response Body:', response.json())
   
```

### Example 2: Fetching Only Headers

**Python Code:**
```python code

    import requests  # Import the requests library for making HTTP requests

    # Make an HTTP HEAD request to the specified URL to fetch only the headers
    response = requests.head('https://jsonplaceholder.typicode.com/posts')

    # Print the status code of the response (e.g., 200 for OK, 404 for Not Found)
    print('Status Code:', response.status_code)

    # Print the headers of the response
    print('Headers:', response.headers)

```

### Example 3: Making a POST Request

**Python Code:**
```python code

import requests  # Import the requests library for making HTTP requests

# Data to be sent in the POST request
data = {
    'title': 'foo',
    'body': 'bar',
    'userId': 1
}

# Make an HTTP POST request to the specified URL with the given data
response = requests.post('https://jsonplaceholder.typicode.com/posts', json=data)

# Print the status code of the response (e.g., 201 for Created)
print('Status Code:', response.status_code)

# Print the body of the response, parsed as JSON
print('Response Body:', response.json())

```

## Tasks:

0. [Basics of HTTP/HTTPS](./README.md)

1. [Consume data from an API using command line tools (curl)](./README.md)

2. [Consuming and processing data from an API using Python](./task_02_requests.py)

3. [Develop a simple API using Python with the `http.server` module](./task_03_http_server.py)

4. [Develop a Simple API using Python with Flask](./task_04_flask.py)

5. [API Security and Authentication Techniques](./task_05_basic_security.py)

