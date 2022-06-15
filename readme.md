### Start Postgres or SQL Server db and update credentials on `config.py`

## Example endpoints
### Add user 
`curl -d "username=user&password=password" -X POST http://localhost:5000/register`

## Login
### _`Get Token`_
`curl -d "username=user&password=password" -X POST http://localhost:5000/user`

## Add Item
### _`Get Data`_
`curl GET -H "Authorization: Bearer token-here http://localhost:5000/data/`
