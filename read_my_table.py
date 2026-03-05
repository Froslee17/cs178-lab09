import boto3

REGION = "us-east-1"
TABLE_NAME = "Playlist"

def get_table():
    """Return a reference to the DynamoDB Movies table."""
    dynamodb = boto3.resource("dynamodb", region_name=REGION)
    return dynamodb.Table(TABLE_NAME)

def print_song(song):
    print(f"Song Title: {song.get('SongTitle')}")
    print(f"Artist: {song.get('Artist')}")
    print(f"Genre: {song.get('Genre')}")
    print("-" * 20)


def print_all_songs():
    table = get_table()
    response = table.scan()
    songs = response.get("Items", [])

    for song in songs:
        print_song(song)


def main():
    print("===== Playlist Table =====")
    print_all_songs()


if __name__ == "__main__":
    main()