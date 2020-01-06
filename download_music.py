# не забывать добавлять все через yandex аккаунт (не через авторизацию через google)
from yandex_music.client import Client
print('Start')
print('\n----------\n')

client = Client.from_credentials('aramamilog@yandex.com', '281987hillhald')


box = client.users_likes_playlists()[0]
box2 = client.users_playlists(kind=1000, user_id=785279921)
for ind, music in enumerate(box2[0].tracks):
    find_track = client.tracks(['{}:{}'.format(music['id'], music['album_id'])])[0]
    name_track = "{ind}.{artists} - {title}".format(ind=ind + 1, artists=find_track['artists'][0]['name'], title=find_track['title'])
    music.track.download('The Walking Dead Album/{name_track}.mp3'.format(name_track=name_track))
    print('Download {name_track}, success'.format(name_track=name_track))







# box[11].track.download('{artist_name} - {music_name}.mp3'.format(artist_name=box[11].track['artists'][0]['name'], music_name=box[11].track['title']))
# text = ''
# for ind, item in enumerate(box):
#     music_name = '{ind}.{artist_name} - {music_name}\n'.format(ind=ind, artist_name=box[ind].track['artists'][0]['name'], music_name=box[ind].track['title'])
#     text += music_name
print('\n----------\n')
print('Done')
