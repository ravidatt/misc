import paramiko
import os
import hashlib

class SFTPFileLoader:



    def sftpRemoteSSHConnect(self, host, port, username, password, keyfilepath, keyfiletype):
        '''
        :param host:
        :param port:
        :param username:
        :param password:
        :param keyfilepath:
        :param keyfiletype:
        :return:
        '''

        ssh=None
        sftp=None
        key=None

        try:
            if keyfiletype=='DSA':
                key=paramiko.DSSKey.from_private_key_file(keyfilepath)
            else:
                key=paramiko.RSAKey.from_private_key_file(keyfilepath)

            ssh=paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh.connect(host,port,username,password,key)
            sftp=ssh.open_sftp()
            # Keep a reference to the SSH client in the SFTP client as to prevent the former from
            # being garbage collected and the connection from being closed.
            sftp.sshclient=ssh
            return sftp

        except Exception as e:
            print('An error occurred creating SFTP client: %s: %s' % (e.__class__, e))
            if sftp is not None:
                sftp.close()
            if ssh is not None:
                ssh.close()
            pass



    def sftpRemoteConnect(self, host,port,username,password,keyfilepath,keyfiletype):
        sftp=None
        key=None
        transport=None
        try:
                if keyfilepath is not None:
                    if keyfiletype =='DSA':
                        key=paramiko.DSSKey.from_private_key_file(keyfilepath)
                    else:
                        key=paramiko.RSAKey.from_private_key_file(keyfilepath)

                transport=paramiko.Transport(host,port)
                transport.connect(None,username,password,key)
                sftp=paramiko.SFTPClient.from_transport(transport)
                return sftp
        except Exception as e:
                print('An error occurred creating SFTP client: %s: %s' % (e.__class__, e))
                if sftp is not None:
                    sftp.close()
                if transport is not None:
                    transport.close()
                pass


    def md5(self,remote_dir,file,sftpConn):
         conn=sftpConn.open(os.path.join(remote_dir, file), "rb")
         print(conn)
         total_read = 0
         hash = hashlib.md5()
         while True:
             data = conn.read(4096)
             total_read += 4096
             if not data:
                 break
             hash.update(data)
         return hash.hexdigest()

    def localMD5(self,file):
        with open(file,mode='rb') as localFile:
            total_read=0
            hash=hashlib.md5()
            while True:
                data=localFile.read(4096)
                total_read+=4096
                if not data:
                    break
                hash.update(data)
            return  hash.hexdigest()



    def transfer_file(self,sftpConn,remote_dir,local_dir):
         files = [f for f in sftpConn.listdir_attr(remote_dir)]
         for f in files:
              md5=self.md5(remote_dir,f.filename,sftpConn)
              sftpConn.get(remotepath=os.path.join(remote_dir, f.filename),localpath=os.path.join(local_dir, f.filename))
              localMD5=self.localMD5(os.path.join(local_dir, f.filename))
              print(("remoteMD5={} localMD5={}").format(md5,localMD5))
              print(md5==localMD5)





local_dir='C:/Users/rsharma1/Desktop/oldPC/Junk/GoogleAPIs/key'
remote_dir='/home/rdatt/testFiles/'
remote_user='rdatt'
remote_host='35.194.42.58'
remote_port=22
private_key='C:/Users/rsharma1/Desktop/oldPC/Junk/GoogleAPIs/key/rdatt'

sftp=SFTPFileLoader()
sftpclient = sftp.sftpRemoteConnect(remote_host, remote_port, remote_user, "", private_key, 'RSA')
sftp.transfer_file(sftpclient,remote_dir,local_dir)