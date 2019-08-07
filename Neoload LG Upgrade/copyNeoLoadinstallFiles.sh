#Copy all files to destination servers

for ((i=27; i<=40;i=i+1))
do 
#  echo "qaneolglin"$i".dev.activenetwork.com"
scp -r /tmp/Neoloadinstallfile ajia@qaneolglin$i.dev.activenetwork.com:/tmp/Neoloadinstallfile

done
