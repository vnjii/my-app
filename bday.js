var daysUntilMyBirthday = 60;
var myBday = 0;
var sad_msg = "days until my birthday. Such a long time... :(";
var excited_msg = "days until my birthday. Its getting close... :)";
var scream_msg = "DAYS UNTIL MY BIRTHDAY!!!";
var bday_msg = "HAPPY BIRTHDAY TO ME!!!!! :D";

while (daysUntilMyBirthday >= myBday){
  if (daysUntilMyBirthday == myBday){
    console.log(bday_msg);
  }
  else if (daysUntilMyBirthday < 5){
    console.log(daysUntilMyBirthday + " " + scream_msg);
  }
  else if(daysUntilMyBirthday >= 30){
    console.log(daysUntilMyBirthday + " " + sad_msg);
  }
  else if (daysUntilMyBirthday < 30){
    console.log(daysUntilMyBirthday + " " + excited_msg);
  }
  // console.log(daysUntilMyBirthday);
  daysUntilMyBirthday = daysUntilMyBirthday - 1;
}
