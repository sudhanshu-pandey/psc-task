INFORMATION REGARDING THE CODE

TECHNOLOGIES USED -  
1. ANACONDA PYTHON 3.6
2. FLASK 1.1.2
3. CONNEXION (SWAGGER) 2.7.0
4. HTML 5.0 
5. CSS
6. JAVASCRIPT
7. JQUERY 1.12.4
8. JQUERY UI 1.12.1


System Bakground info - 
The system is used for searching the information about the department details.


Local Host Server Address : http://localhost:5000/
View api info - http://localhost:5000/api/ui/

Curl command for autocomplete api call - curl -X GET --header 'Accept: application/json' 'http://localhost:5000/api/department/get_department/#'

Replace hash with query word.

Eg. - 
curl -X GET --header 'Accept: application/json' 'http://localhost:5000/api/department/get_department/comp'

Note - Please also install swagger ui bundle : pip install swagger-ui-bundle 

