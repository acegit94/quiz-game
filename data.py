import http.client
import json

conn = http.client.HTTPSConnection('opentdb.com',)

conn.request('GET', '/api.php?amount=10&difficulty=easy&type=boolean')

response = conn.getresponse()

# print(f"Status: {response.status}")
# print(f"Reason: {response.reason}")

data = response.read().decode("utf-8")

json_data = json.loads(data)

results = json_data['results']

question_data = []

for i in results:
    questions = {"text": i['question'], "answer": i['correct_answer']}
    question_data.append(questions)