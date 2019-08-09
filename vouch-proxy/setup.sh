sed -i -e "s/XXXXX1/${VOUCHID}/g" /config.yml
sed -i -e "s/XXXXX2/${VOUCHSECRET}/g" /config.yml

echo "Successfully edited config file."