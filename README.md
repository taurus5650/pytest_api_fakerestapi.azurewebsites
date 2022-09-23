# pytest_api_fakerestapi.azurewebsites


### Overall
- API source from https://fakerestapi.azurewebsites.net/index.html.
- This project would using pytest to testing api.
  - API testing list :
    - a. [GET] /api/v1/Books/{id} 
    - b. [POST] /api/v1/Users
    
    
### `/api/v1/Books/{id}` testing scope
- Schema
  ```schema
  {
  id	integer($int32)
  title	string
    nullable: true
  description	string
    nullable: true
  pageCount	integer($int32)
  excerpt	string
    nullable: true
  publishDate	string($date-time)
  }
  ```
- Scope
![alt text](https://github.com/taurus5650/Drafting-pytest_api_fakerestapi.azurewebsites/blob/main/xmind/get-api-v1-books-id.png)


### /api/v1/Users` testing scope
- Schema
  ```schema
  {
  id	integer($int32)
  userName	string
    nullable: true
  password	string
    nullable: true
  }
  ```
- Scope
![alt text](https://github.com/taurus5650/Drafting-pytest_api_fakerestapi.azurewebsites/blob/main/xmind/post-api-v1-users.png)


### Execution

