# schedule
# Aids in running code at specific days and times

Overview:
This program is used to aid in the organization and running of certain code at specfic
days and times. Create and save schedule objects with a dictionary of Day/Times. The
next_action() method will return the number of seconds the program can sleep until
the next scheduled time in the dictionary.

<strong>Times:</strong>
All times are stored in military time but may be entered in a variety of formats.
The format_times() function will address most possible input types. Acceptable input 
formats include:

5am

12:30am

5:30am

7:10pm

12:30pm

8:30:10pm

8:30:10am

17

14:20

19:10:30

Repeats and improperly formated entries will be ignored and data will be sorted.

Days:
The following formats may be used for any day:

Monday monday M m 

Sunday sunday U u

All 	all   A a

Methods:
next_action(display) #Returns number of seconds until next action in dictionary. display
determines where a statement is printed to the console indicating next run date/time.

create_time() #allows user to add, remove and copy times. Actions include:

[day], [time], [time], [time]... --> adds elemtns to Schedule

del [day] [time], [time], [time].... --> removes elements to Schedule

list --> see list of commands

clear --> remove all elements from times

copy [filename] --> adds all elements from filename into current Schedule

done --> complete adding times

save(file) #save Schedule file

@staticmethod
load(filename) #load Schedule file

The below are helper methods and never need to be called directly:
format_day(single_day) #formats a list of times into xx:xx:xx format. Removes improperly
formated elements from list

delete_time(day, inc_list) #deletes elements from list

add_time(day, inc_list) #adds elements to list

day_translate(day) #formats day input

helper() #prints command information to console