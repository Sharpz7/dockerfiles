sed -i -e "s/XXXXX1/${VOUCHID}/g" /vouch/config/config.yml
sed -i -e "s/XXXXX2/${VOUCHSECRET}/g" /vouch/config/config.yml

echo "Successfully edited config file."
./vouch-proxy