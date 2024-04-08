# DJANGO REST API ASSIGNMENT - MCDA 5550 - Saint Mary's University

This is a Django application that provides APIs to retrieve a list of hotels stored in the SQLite database and to add a hotel to the list of hotels in the database. The API provides the following methods:

## GET Method to Retrieve a List of Hotels in the Database

The following URL can be used to retrieve a list of hotels from the database:

**API URL:** `http://127.0.0.1:8000/hotels/list_hotels`

**Sample Response:**
```
HTTP 200 OK
Allow: GET, OPTIONS
Content-Type: application/json
Vary: Accept

[
    {
        "id": 1,
        "name": "Grand Hyatt",
        "price": "250.00",
        "availability": true
    },
    {
        "id": 2,
        "name": "Hilton Garden Inn",
        "price": "180.50",
        "availability": true
    }
]
```

### Screenshot of GET Response:
![alt text](API_RESPONSE_GET.png)


## POST Method to Add a Hotel to the Database

The following URL can be used, along with the request body (a JSON object), to add a hotel to the database:

**API URL:** `http://127.0.0.1:8000/hotels/add_hotel`

**Sample Request Body:**
```json
{
    "name": "Radisson Blu",
    "price": 200.25,
    "availability": true
}
```

**Sample Successful Response:**
```
HTTP 200 OK
Allow: OPTIONS, POST
Content-Type: application/json
Vary: Accept

{
    "Message": "Hotel added successfully to the database"
}
```

### Screenshot of Successful POST Method:
![alt text](API_SUCCESS_RESPONSE_POST.png)

**Sample Unsuccessful Response:**
```
HTTP 400 Bad Request
Allow: POST, OPTIONS
Content-Type: application/json
Vary: Accept

{
    "error": "Hotel with name \"Grand Hotel\" already exists"
}
```

### Screenshot of Failed POST Method for Duplicate Hotel:
![alt text](API_FAILED_RESPONSE_POST.png)

## How to Install and Run the Application

### Prerequisites

Before you proceed, ensure you have the following installed on your local machine:

- Python (version 3.6 or higher)
- Git (optional, for cloning the repository)
- SQLite (or any other supported database)

### Installation

1. **Clone the Repository**:
   - Open a terminal or command prompt.
   - Run the following command to clone the repository to your local machine:

     ```bash
     git clone https://github.com/A00431008/hotels_api
     ```

2. **Navigate to the Project Directory**

3. **Create and Activate Virtual Environment** (optional but recommended):
   - Create a virtual environment using:

     ```bash
     python -m venv venv
     ```

   - Activate the virtual environment:
     - On Windows:

       ```bash
       venv\Scripts\activate
       ```

     - On macOS and Linux:

       ```bash
       source venv/bin/activate
       ```

4. **Install Dependencies**:
   - Install the required dependencies by running:

     ```bash
     pip install -r requirements.txt
     ```

### Running the Application

1. **Apply Migrations**:
   - Apply migrations to create the database schema by running:

     ```bash
     python manage.py migrate
     ```

2. **Start the Development Server**:
   - Start the development server by running:

     ```bash
     python manage.py runserver
     ```

3. **Access the Application**:
   - Access the application in your web browser at `http://127.0.0.1:8000/`.

### Testing the APIs

- Use tools like [Postman](https://www.postman.com/) or [curl](https://curl.se/) to test the APIs provided by the application. This can directly by tested from the web browser as well.
- Refer to the API documentation provided above for endpoint URLs and request/response formats.
