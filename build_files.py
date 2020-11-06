group = '5L'

firstRecessTime = '9, 58'
lunchRecessTime = '12, 2'
afterLunchTime = '12, 47'
lastRecessTime = '13, 57'
endOfDay = '15, 10'

firstRecessTimeED = '9, 58'
lunchRecessTimeED = '12, 2'
afterLunchTimeED = '12, 2'
endOfDayED = '15, 10'

contents = '''
<!DOCTYPE html>
<html>
<!DOCTYPE html>
<html>
  <head>
    <base target='_top'>
  </head>
  <body>
  <p id='countDownParagraph' style="text-align: center; font-size: 700%;"></p>
  <script>
  var x = setInterval(function() {
  var dateNow = new Date();
  var year = dateNow.getFullYear();
  var month = dateNow.getMonth();
  var day = dateNow.getDate();
  if (day < 8 && dateNow.getDay() == 3) { // first Wednesday of the month
    var firstRecessTime = new Date(year, month, day, 
'''+ firstRecessTimeED +'''
, 0);
    var lunchRecessTime = new Date(year, month, day, 
'''+ lunchRecessTimeED +'''
, 0);
    var afterLunchTime = new Date(year, month, day, 
'''+ afterLunchTimeED +'''
, 0);
    var lastRecessTime = new Date(year, month, day, 
'''+ afterLunchTimeED +'''
, 1);
    var endOfDay = new Date(year, month, day, 
'''+ endOfDayED +'''
, 0);
  } else {
    var firstRecessTime = new Date(year, month, day, 
'''+ firstRecessTime +'''
, 0);
    var lunchRecessTime = new Date(year, month, day, 
'''+ lunchRecessTime +'''
, 0);
    var afterLunchTime = new Date(year, month, day, 
'''+ afterLunchTime +'''
, 0);
    var lastRecessTime = new Date(year, month, day, 
'''+ lastRecessTime +'''
, 0);
    var endOfDay = new Date(year, month, day, 
'''+ endOfDay +'''
, 0);
  }
  var untilString = '';
  var difference = firstRecessTime - dateNow;
  if (difference < 0) {difference = lunchRecessTime - dateNow; untilString = 'recess'}
  if (difference < 0) {difference = afterLunchTime - dateNow; untilString = 'class starts';}
  if (difference < 0) {difference = lastRecessTime - dateNow; untilString = 'recess'}
  if (difference < 0) {difference = endOfDay - dateNow; untilString = 'the end of the day'}
  var hours = Math.floor((difference % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
  var minutes = Math.floor((difference % (1000 * 60 * 60)) / (1000 * 60));
  var seconds = Math.floor((difference % (1000 * 60)) / 1000);
  var displayDateTime = dateNow.toString().split(" GMT")[0];
  if (hours > 0) {var countDownString = hours + " h and " + minutes + " m ";}
  else {var countDownString = minutes + " m and " + seconds + " s ";}
  document.getElementById('countDownParagraph').innerHTML = displayDateTime + "<br><br>" + countDownString  + 'until ' + untilString + '.';
  }, 1000); // updating setInterval every second
  </script>
  </body>
</html>
'''

f = open(group+'.html', 'w')
f.write(contents)
f.close()