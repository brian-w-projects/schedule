# schedule
# Aids in running code at specific days and times

<h2>Overview:</h2>
<p>This program is used to aid in the organization and running of certain code at specfic
days and times. Create and save schedule objects with a dictionary of Day/Times. The
next_action() method will return the number of seconds the program can sleep until
the next scheduled time in the dictionary.</p>

<h2>Times:</h2>
<p>All times are stored in military time but may be entered in a variety of formats.
The format_times() function will address most possible input types. Acceptable input 
formats include:</p>

<ul>
  <li>5am</li>
  <li>12:30am</li>
  <li>5:30am</li>
  <li>7:10pm</li>
  <li>12:30pm</li>
  <li>8:30:10pm</li>
  <li>8:30:10am</li>
  <li>17</li>
  <li>14:20</li>
  <li>19:10:30</li>
</ul>

Repeats and improperly formated entries will be ignored and data will be sorted.

<h2>Days:</h2>
<p>The following formats may be used for any day:</p>

<ul>
  <li>Monday monday M m </li>
  <li>Sunday sunday U u</li>
  <li>All    all    A a</li>
</ul>

<h2>Methods:</h2>
<p><h6>next_action(display)</h6> #Returns number of seconds until next action in dictionary. display
determines where a statement is printed to the console indicating next run date/time.</p>

<ul>
  <li>create_time() #allows user to add, remove and copy times. Actions include:</li>
  <li>[day], [time], [time], [time]... --> adds elemtns to Schedule</li>
  <li>del [day] [time], [time], [time].... --> removes elements to Schedule</li>
  <li>list --> see list of commands</li>
  <li>clear --> remove all elements from times</li>
  <li>copy [filename] --> adds all elements from filename into current Schedule</li>
  <li>done --> complete adding times</li>
</ul>


<h6>save(file) #save Schedule file</h6>

<h6>@staticmethod load(filename) #load Schedule file</h6>

<p><h6>format_day(single_day)</h6>#formats a list of times into xx:xx:xx format. Removes improperly
formated elements from list</p>

<p><h6>delete_time(day, inc_list)</h6> #deletes elements from list</p>

<p><h6>add_time(day, inc_list)</h6> #adds elements to list</p>

<p><h6>day_translate(day)</h6> #formats day input</p>

<p><h6>helper()</h6> #prints command information to console</p>