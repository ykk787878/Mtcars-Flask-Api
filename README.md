1 build docker image:
docker build -t mtcars-api .

2 run container:
docker run -p 8080:8080 mtcars-api  

3 test the API:
curl -X POST http://127.0.0.1:8080/predict -H "Content-Type: application/json" -d "{\"cyl\":6, \"disp\":160, \"hp\":110, \"drat\":3.9, \"wt\":2.62, \"qsec\":16.46, \"vs\":0, \"am\":1, \"gear\":4, \"carb\":4}"

   the output should be:
{
  "mpg_prediction": 21.88
}
