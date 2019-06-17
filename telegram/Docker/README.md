sudo ssh -i abylay_rsa root@128.199.62.241

sudo scp -i abylay_rsa -r send_to/ root@128.199.62.241:/usr/our

docker-compose up -d
