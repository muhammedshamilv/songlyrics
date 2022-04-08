from flask import Flask, render_template,jsonify
import lyric
app = Flask(__name__)

@app.route("/")
def hello():
    return render_template("base.html")

@app.route("/artist")
def get_artist():
    artists = lyric.get_all_artist()
    artists_arr = [{'id':i[0], "name":i[1]} for i in artists]
    print(artists_arr)
    return jsonify(artists_arr)

@app.route("/songs/<int:aid>")
def list_all_songs(aid):
    songs= lyric.get_all_songs(aid)
    songs_arr = [{'id':i[1], "name":i[0]} for i in songs]
    singer=lyric.singer(aid)
    print(songs_arr)
    return jsonify(songs_arr)


@app.route("/songs/<int:aid>/lyrics/<int:sid>")
def lyrics(aid,sid):
    lyrics= lyric.get_lyrics(sid)
    songs= lyric.get_all_songs(aid)
    singer=lyric.singer(aid)
    artists = lyric.get_all_artist()    
    return jsonify(lyrics)


if __name__=="__main__":
    app.run(debug=True)