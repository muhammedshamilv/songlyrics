import sys
import psycopg2

def get_all_songs(aid):
    con = psycopg2.connect("dbname=lyrics")
    cmd=con.cursor()
    cmd.execute("select songs.song_name, songs.id from songs,artist where artist.id = songs.artist and artist.id=%s",(aid,))  
    songs= cmd.fetchall()
    return songs
    
def singer(artistid):
    con = psycopg2.connect("dbname=lyrics")
    cmd=con.cursor()
    cmd.execute("select id, name from artist where artist.id=%s",(artistid,))  
    singer= cmd.fetchone()
    return singer


def get_all_artist():
    con = psycopg2.connect("dbname=lyrics")
    cmd=con.cursor()
    cmd.execute("select id,name from artist" )  
    artists= cmd.fetchall()
    return artists

def get_lyrics(sid):
    con = psycopg2.connect("dbname=lyrics")
    cmd=con.cursor()
    cmd.execute("select lyrics,song_name from songs where id=%s",(sid,))
    lyric= cmd.fetchone()
    return lyric
