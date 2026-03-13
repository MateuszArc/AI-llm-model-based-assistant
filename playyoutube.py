import webbrowser, requests, re

firefox = webbrowser.get('C:/Program Files/Mozilla Firefox/firefox.exe %s')

def play_youtube(query):
    search_query = query.replace(" ", "+")
    url = f"https://www.youtube.com/results?search_query={search_query}"

    html = requests.get(url).text
    video_ids = re.findall(r"watch\?v=(\S{11})", html)

    if video_ids:
        video_url = "https://www.youtube.com/watch?v=" + video_ids[0]
        firefox.open(video_url)

