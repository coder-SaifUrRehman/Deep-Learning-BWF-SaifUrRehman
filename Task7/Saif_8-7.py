def make_album(artist, album_title, num_tracks=None):
    album = {"artist": artist, "title": album_title}
    if num_tracks:
        album["tracks"] = num_tracks
    return album

album1 = make_album("Artist1", "Album1")
album2 = make_album("Artist2", "Album2 ")
album3 = make_album("Artist3", "Album3")

print(album1)
print(album2)
print(album3)
