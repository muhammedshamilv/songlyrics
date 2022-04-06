from flask import Flask, render_template
import lyric
app = Flask(__name__)

@app.route("/")
def hello():
    artists = lyric.get_all_artist()
    return render_template("index.html", artists=artists)

@app.route("/songs/<int:aid>")
def list_all_songs(aid):
    songs= lyric.get_all_songs(aid)
    singer=lyric.singer(aid)
    artists = lyric.get_all_artist()
    return render_template("songlist.html",singer=singer, current=aid,artists=artists,songs=songs)

@app.route("/songs/<int:aid>/lyrics/<int:sid>")
def lyrics(aid,sid):
    lyrics= lyric.get_lyrics(sid)
    songs= lyric.get_all_songs(aid)
    singer=lyric.singer(aid)
    artists = lyric.get_all_artist()    
    return render_template("lyrics.html",lyrics=lyrics,artists=artists,songs=songs,singer=singer,current=aid,csong=sid)


if __name__=="__main__":
    app.run(debug=True)