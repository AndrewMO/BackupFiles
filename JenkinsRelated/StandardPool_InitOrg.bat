@echo off
set orgname=%1
set curllocation=%2
echo "orgname=%orgname%"
echo "########################################################################################"
set address1="http://perf-activenet-19w.an.active.tan:3000/%orgname%/servlet/adminlogin.sdi"
set address2="http://perf-activenet-20w.an.active.tan:3000/%orgname%/servlet/adminlogin.sdi"
echo "address1=%address1%"
echo "address2=%address2%"
echo "########################################################################################"
echo "---Start initialing---"
cd %curllocation%


curl -i %address1%
curl -i %address2%

echo "---End initialing---"
exit
