from imgurpython import ImgurClient

client_id = 'client_id_here'
client_secret = 'client_secret_here'

client = ImgurClient(client_id, client_secret)


items = client.get_album_images('Qt3XXOA')

for item in items:
    print("\'" + item.link + "\'" + ",")