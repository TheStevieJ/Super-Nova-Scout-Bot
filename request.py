import requests

codes = {
	400: "Bad Request",
	401: "Unauthorized",
	403: "Forbidden",
	404: "Not Found",
	415: "Unsupported Media Type",
	429: "Rate Limit Exceeded",
	500: "Internal Server Error",
	503: "Service Unavailable"
}


def load_key():
	file = open("key.txt","r")
	return file.readline()


def api_request(pre_url):
	url = pre_url + "api_key=" + load_key()
	r = requests.get(url,{})
	data = r.json()
	return data