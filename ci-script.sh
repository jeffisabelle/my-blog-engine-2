set -xe

echo "Launch the server"
nohup python index.py > /dev/null 2>&1 &

sleep 1

echo "Generate static html files"
python generate-static.py
