sed -i -e "s/XXXXX1/${VOUCHID}/g" /config/config.yml
sed -i -e "s/XXXXX2/${VOUCHSECRET}/g" /config/config.yml

ls -a

echo "Successfully edited config file."
/vouch-proxy