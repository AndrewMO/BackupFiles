//facility ID list
var facilitylist = [3308,12966,2702,14126,14452,3150,14657,8239,13799,5883,10118,10971,14328,3937,7465,14992,16961];

//random choose count
var min = 1;
var max = facilitylist.length;
var choosecount = Math.round(Math.random()*(max-min+1)+min);



var facilitylistselect = [ ];
var facilitylistselectNum = choosecount;
for (var i = 0; i < facilitylistselectNum; i++) {
    var ran = Math.floor(Math.random() * (facilitylist.length - i));
    facilitylistselect.push(facilitylist[ran]);
    facilitylist[ran] = facilitylist[facilitylist.length - i - 1];
};


logger.debug(facilitylistselect)





function random(min, max) {
    return Math.round(Math.random()*(max-min+1)+min);
}