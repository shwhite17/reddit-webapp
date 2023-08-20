from flask import Flask, render_template
import requests

app = Flask(__name__, template_folder='templates')

reddit_endpoint = "https://www.reddit.com/r/SUBREDDIT_NAME/new.json?limit=10"

@app.route('/api/threads', methods=['GET'])
def get_threads():
    subreddit_name = "Education"
    response = requests.get(reddit_endpoint.replace("SUBREDDIT_NAME", subreddit_name))
    response_json = response.json()
    print("response body --> ")
    print(response_json)
    threads = []
    if 'data' in response_json and 'children' in response_json['data']:
        for item in response_json['data']['children']:
            thread_data = item['data']
            thread = {
                'title': thread_data['title'],
                'author': thread_data['author'],
                'created_utc': thread_data['created_utc'],
                'link': f"https://www.reddit.com{thread_data['permalink']}"
            }
            threads.append(thread)

    print("threads --> ")
    print(threads)
    return render_template('index.html', threads=threads)

if __name__ == '__main__':
    app.run(debug=True)
