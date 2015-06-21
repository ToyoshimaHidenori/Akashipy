import requests

url = 'http://connpass.com/api/v1/event/?keyword='
print('イベントを検索:',end='')
keyword = input()
r = requests.get(url + keyword)

print(r.status_code, r.headers['content-type'])

for event in r.json()['events'][:10]:
    print(event['event_id'] , event['title'],'\n開始時間 : ', event['started_at'] + '\n')

