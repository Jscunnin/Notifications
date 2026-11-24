import requests

'''
This function is to use th entfy app to notify a users phone.
INPUTS: string topic, string message, optional string title
'''
ntfy_retrys = 0
ntfy_lock = 0; #LOCKED IF 1

def notify_phone(topic, message, title="notification"):
	global ntfy_lock, ntfy_retrys
	if (ntfy_lock != 1):
		response = requests.post(
			f"https://ntfy.sh/{topic}",
			data=message.encode('utf-8'),
			headers={
				"Title": title,
				},
			timeout=5
		)
		if response.status_code == 429:
			ntfy_lock = 1
			print("locked")

	#If we have run into a error saying too many requests, ignore the next 10 requests
	else:
		if ntfy_retrys > 10:
			ntfy_lock = 0
			ntfy_retrys = 0
		else:
			ntfy_retrys += 1


if __name__ == "__main__":
	notify_phone("JSCtesting", "testing", "test")
