import requests
import json

job = "Data Analyst"
wuzzuf_search_api = 'https://wuzzuf.net/api/search/job'
headers = {'content-type': 'application/json;charset=UTF-8'}
data = {"startIndex":0,"pageSize":10000,"longitude":"0","latitude":"0","query":job ,"searchFilters":{}}
data = json.dumps(data)
job_search_json = requests.post(wuzzuf_search_api , headers=headers , data=data).json()
with open('job_search.json', 'w', encoding='utf-8') as f: json.dump(job_search_json, f, ensure_ascii=False, indent=4)

job_ids = [job['id'] for job in job_search_json['data']]
wuzzuf_job_api = 'https://wuzzuf.net/api/job?filter[other][ids]=' + ','.join(job_ids)
job_details_json = requests.get(wuzzuf_job_api).json()
with open('job_details.json', 'w', encoding='utf-8') as f: json.dump(job_details_json, f, ensure_ascii=False, indent=4)

company_ids = [company['relationships']['company']['data']['id'] for company in job_details_json['data'] if company['relationships']['company']['data'] !=None]
company_ids = list(set(company_ids))
wuzzuf_company_api = 'https://wuzzuf.net/api/company?filter[id]=' + ','.join(company_ids)
company_details_json = requests.get(wuzzuf_company_api).json()
with open('company_details.json', 'w', encoding='utf-8') as f: json.dump(company_details_json, f, ensure_ascii=False, indent=4)
