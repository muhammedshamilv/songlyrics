from flask import Blueprint,jsonify
import lyric
api = Blueprint('api',__name__)

@api.route("/artist")
def get_artist():
    artists = lyric.get_all_artist()
    artists_arr = [{'id':i[0], "name":i[1]} for i in artists]
    print(artists_arr)
    return jsonify(artists_arr)

@api.route("/songs/<int:aid>")
def list_all_songs(aid):
    songs= lyric.get_all_songs(aid)
    songs_arr = [{'id':i[1], "name":i[0]} for i in songs]
    singer=lyric.singer(aid)
    print(songs_arr)
    return jsonify(songs_arr)


@api.route("/songs/<int:aid>/lyrics/<int:sid>")
def lyrics(aid,sid):
    lyrics= lyric.get_lyrics(sid)
    songs= lyric.get_all_songs(aid)
    singer=lyric.singer(aid)
    artists = lyric.get_all_artist()    
    return jsonify(lyrics)

