import pysftp
import os


def send_sqlite_over_sftp():
    sft_host = os.environ.get('SFTP_HOST')
    sftp_password = os.environ.get('SFTP_PASSWORD')
    sftp_user = os.environ.get('SFTP_USER')
    cnopts = pysftp.CnOpts()
    cnopts.hostkeys = None

    # print(sft_host)
    # print(sftp_password)
    # print(sftp_user)
    with pysftp.Connection(sft_host, username=sftp_user, password=sftp_password, cnopts=cnopts, port=3000) as sftp:
        sftp.put("products.db", "./upload/products.db")

    print('Upload done.')

