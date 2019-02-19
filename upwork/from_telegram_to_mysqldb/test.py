import requests
import pickle


def main():
    result = requests.get('https://o7planning.org/ru/11463/cache/images/i/7878444.png')
    if result.status_code == 200:
        with open('my_image.txt', 'wb') as f:
            for chunk in result:
                f.write(chunk)


if __name__ == '__main__':
    main()
Message(
    id=1228,
    to_id=PeerUser(user_id=626788182),
    date=datetime.datetime(2019, 2, 15, 16, 15, 21, tzinfo=datetime.timezone.utc),
    message='',
    out=True,
    mentioned=False,
    media_unread=False,
    silent=False,
    post=False,
    from_scheduled=False,
    from_id=390039179,
    fwd_from=None,
    via_bot_id=None,
    reply_to_msg_id=None,
    media=MessageMediaPhoto(
        photo=Photo(
            id=5420193576333191726,
            access_hash=-3919591095116421685,
            file_reference=b'\x03\x00\x00\x04\xcc\\f\xe5\x99\xd6\xd1\xd7R\xff\x17\x02\xacR\x1b\xdf\x19\x86\xb7e\xd5',
            date=datetime.datetime(2019, 2, 15, 15, 26, 55, tzinfo=datetime.timezone.utc),
            sizes=[PhotoStrippedSize(
                type='i',
                bytes=b'\x01(\x14\xd5\x11\x85\x1dO\xaf&\x97h\xaa\xdfk\xceA^*3p\xf1\xbf\xc8\x88\x07\xbehZ\xec\x0fB\xee\xc1ET[\xb9H\x04\x84\x1f\x9d\x15\\\xacW*\xa1\x01\xc9<\xb7\xd6\x96O\xf5\x84\x93\xc7\x1cT\x97*\xdfh}\xacUx\xe8zqH\xb2\x9c|\xc1O\x1dy\xa7\xa2\xd4\x9f!\x81I\x1f~\x8a\xd0\xb7UhA*\t$\xff\x00:(\xe6\x1d\x872D\xc4\x96@I\xeb\xc5 \x8a\x000\x11@\xfaQEAC\xd4\xaa\x8c\x0e\x05\x14Q@\x1f'), PhotoSize(type='m', location=FileLocation(dc_id=2, volume_id=257019647, local_id=18419, secret=-7145282280433293940, file_reference=b'\x03\x00\x00\x04\xcc\\f\xe5\x99\xc11 nu~xJij\x9e\xad\xe2\x94v\x9a'), w=160, h=320, size=15713), PhotoSize(type='x', location=FileLocation(dc_id=2, volume_id=257019647, local_id=18420, secret=-2808513554148255412, file_reference=b'\x03\x00\x00\x04\xcc\\f\xe5\x99jz%\x88\x8aM\xf1?\xe6zXE_\xb0\x02\xe4'), w=400, h=800, size=59207), PhotoSize(type='y', location=FileLocation(dc_id=2, volume_id=257019647, local_id=18417, secret=85188768056928823, file_reference=b'\x03\x00\x00\x04\xcc\\f\xe5\x99 \xd83D\n\x83W\xa8\x84\xdd\xc2*<SY\xd5'), w=640, h=1280, size=94782)], has_stickers=False), ttl_seconds=None), reply_markup=None, entities=[], views=None, edit_date=None, post_author=None, grouped_id=None)

