import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Playlist')


def print_song(song):
    print(f"Song Title: {song.get('SongTitle')}")
    print(f"Artist: {song.get('Artist')}")
    print(f"Genre: {song.get('Genre')}")
    print("-" * 20)


def print_all_songs():
    response = table.scan()
    songs = response.get("Items", [])

    for song in songs:
        print_song(song)


def main():
    print("===== Playlist Table =====")
    print_all_songs()


if __name__ == "__main__":
    main()