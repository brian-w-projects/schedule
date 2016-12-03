import datetime, re, sys, os, pickle

class Schedule():
    
    def __init__(self, times=None):
        if not times:
            self.times = {'Monday' : [],
                          'Tuesday' : [],
                          'Wednesday': [],
                          'Thursday': [],
                          'Friday': [],
                          'Saturday': [],
                          'Sunday': []
                         }          
        else:
            self.times = times

        
    def next_action(self, display=False):
        now = datetime.datetime.now()
        combine = now
        
        while True:
            for check_time in self.times[combine.strftime('%A')]:
                if combine.strftime('%H:%M:%S') < check_time:
                    s_hour, s_min, s_sec = map(int, check_time.split(':'))
                    combine = datetime.datetime.combine(combine.date(),
                        datetime.time(s_hour, s_min, s_sec))
                    if display:
                        print('Next Text: ' + combine.strftime('%A') + ' ' + str(combine))
                    return(int((combine - now).total_seconds()))
            combine = datetime.datetime.combine(combine.date() + 
                datetime.timedelta(days=1), datetime.time(0))	


    def format_day(self, single_day):
        reg = re.compile(r'(\d{1,2})((:\d{2}){0,2})(pm)?', re.IGNORECASE)

        for i in range(len(single_day)):
            mo = reg.search(single_day[i])

            single_day[i] = ''

            if mo == None:
                continue

            if mo.group(4) or int(mo.group(1)) == 12:
                if 0 < int(mo.group(1)) < 12:
                    single_day[i] = str(int(mo.group(1)) + 12)
                else:
                    single_day[i] = mo.group(1)
            elif int(mo.group(1)) == 12:
                single_day[i] = '00'
            else:
                if len(mo.group(1)) == 1:
                       single_day[i] = '0' + mo.group(1)
                else:
                    single_day[i] = mo.group(1)

            if mo.group(2):
                single_day[i] += mo.group(2)
                if len(mo.group(2)) == 3:
                    single_day[i] += ':00'
            else:
                single_day[i] += ':00:00'

        [single_day.remove(time) for time in single_day if time == '']


    def create_time(self):
        print('Ready to add times.')
        print('Type "list" to see commands')
        print('Type "done" when finished')

        while True:
            print(self)   
            action = input('Action: ')
            if action == 'done':
                break
            if action == 'list':
                self.helper()
                continue
            if action == 'clear':
                self.times = {key: [] for key in self.times}
                continue
            if action.startswith('copy'):
                loaded_schedule = self.load(action[action.index(' ')+1:])
                if loaded_schedule:
                    [self.add_time(key, value) for (key, value) in loaded_schedule.times.items()]
                continue
            
            reg = re.compile('^(del)? ?(\w+) ((.+?(, )?){1,})', re.IGNORECASE)
            mo = reg.search(action)

            if mo == None:
                print('Format not recognized')
                continue

            inc_list = mo.group(3).split(', ')
            self.format_day(inc_list)

            if mo.group(1) == 'del':
                self.delete_time(self.day_translate(mo.group(2)), inc_list)
            else:
                self.add_time(self.day_translate(mo.group(2)), inc_list)
                

    def save(self, file):
        try:
            if not os.path.join(os.getcwd(), 'schedule'):
                os.makedirs(os.path.join(os.getcwd(), 'scehdule'))
        except:
            print('Could not create storage folder.')
            return
        os.chdir('schedule')

        with open(file + '.p', 'wb') as outfile:
            pickle.dump(self, outfile)


    @staticmethod
    def load(filename):
        try:
            with open(os.path.join('schedule', filename + '.p'), 'rb') as infile:
                print('File information added')
                return pickle.load(infile)
        except Exception:
            print('Could not find file')
            

    def delete_time(self, day, inc_list):
        if day == 'All':
            for day in self.times.keys():
                self.times[day] = [x for x in self.times[day] if x not in inc_list]
            [day.sort() for day in self.times.values()]
        else:
            self.times[day] = [x for x in self.times[day] if x not in inc_list]
            self.times[day].sort()

    def add_time(self, day, inc_list):
        if day == 'All':
            for day in self.times.keys():
                [self.times[day].append(t) for t in inc_list if t not in self.times[day]]
            [day.sort() for day in self.times.values()]
        else:
            [self.times[day].append(t) for t in inc_list if t not in self.times[day]]
            self.times[day].sort()


    def day_translate(self, day):
        return { 'M' : 'Monday', 'm' : 'Monday',
                 'T' : 'Tuesday', 't' : 'Tuesday',
                 'W' : 'Wednesday', 'w' : 'Wednesday',
                 'H' : 'Thursday', 'h' : 'Thursday',
                 'F' : 'Friday', 'f' : 'Friday',
                 'S' : 'Saturday', 's' : 'Saturday',
                 'U' : 'Sunday', 'u' : 'Sunday',
                 'A' : 'All', 'a' : 'All'}.get(day, day)

    def helper(self):
        print('day [time], [time],... to add times\n'+
              'del day [time], [time],... to delete times\n'+
              'See readme for acceptable [time] formats\n'+
              'clear to empty list\n'+
              'copy [filename] to add all elements from [filename]\n'+
              'done to finish editing')

    def __str__(self):
        keys = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday',
                'Saturday', 'Sunday']
        to_return = ''
        for day in keys:
            to_return += day.ljust(10) + ' ' + str(self.times[day]) + '\n'
        return to_return

    def __repr__(self):
        return(str(self.times))

if __name__ == '__main__':
    y = Schedule()
    y.create_time()
